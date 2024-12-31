# 算法模板

重写一个算法模板需要继承算法基类`AlgorithmBase`以规范算法调用接口：

```python
from darwin.ea.base.algorithm import AlgorithmBase
```

以MOEAD为例：

> 注意：
>
> 每一个算法都需要更具一个具体的配置项来运行，这个配置项提供了算法运行的必要参数，框架已经提供了默认的`Settings`对象，该对象默认包含如下信息：
>
> ```python
> class Settings:
>     def __init__(self,
>                  population_num=100, # 种群大小
>                  objectives_num=3, # 目标空间维度
>                  dec_num=30, # 决策空间维度
>                  evaluation=500, # 进化代数
>                  problem=DTLZ1, # 测试问题
>                  encoding="real", # 种群编码类型
>                  visualization=True): # 可视化开关
> 
>         self.population_num = population_num
> 
>         self.objectives_num = objectives_num
> 
>         self.dec_num = dec_num
> 
>         self.evaluation = evaluation
> 
>         self.problem = problem
> 
>         self.encoding = encoding
> 
>         self.visualization = visualization
> ```

```python
class MOEAD(AlgorithmBase):
    def __init__(self,
                 settings=None,
                 n_neighbors=15,
                 crossover=None,
                 mutation=None,
                 prob_neighbor_mating=1,
                 **kwargs):
        # settings必须要定义，如果用户定义为空则获取框架默认配置
        if settings is None:
            settings = Settings()
        # 父类__init__接口，必须调用
        super().__init__(settings=settings,
                         name="MOEAD",
                         crossover=crossover,
                         mutation=mutation)

        self.prob_neighbor_mating = prob_neighbor_mating # 骚操作
        self.n_var = self.settings.dec_num

        self.n_obj = self.settings.objectives_num

        self.problem = settings.problem(self.n_var, self.n_obj)

        self.ref_dirs = UniformReferenceDirection(n_dim=self.n_obj, n_points=self.settings.population_num).do()

        self.pop_size = self.ref_dirs.shape[0] # 由于权重的生成不能满足需求的点，更具绑定的规则个体数量和参考向量的数量要一一对应
        self.settings.population_num = self.ref_dirs.shape[0] # 因为种群大小改变了，所以需要更新配置中的种群大小

        self.pop = Population(random_sampling.float_random_sampling(self.problem.bounds, self.pop_size, self.n_var)) # 初始话种群
        self.pop.refresh(self.problem) # 根据测试问题刷新种群的性状，说白了也就是目标值
        self.ideal_point = np.min(self.pop.F, axis=0) # 设置参考点
        self.n_neighbors = n_neighbors # 设置领域大小
        self.neighbors = np.argsort(cdist(self.ref_dirs, self.ref_dirs), axis=1, kind='quicksort')[:, :self.n_neighbors] # 获得每一个点对应的邻居，注意np.argsort自己百度
        self.decomposition = PBI() # 设置用到的分解方法
 
    # 种群迭代接口，每调用一次就相当于进化一次
    def next(self):
        # moead核心操作，自己理解，该操作目的是更新种群，不需要返回值
        for i in np.random.permutation(self.pop_size):
            N = self.neighbors[i, :]
            if np.random.random() < self.prob_neighbor_mating:
                parents = N[np.random.permutation(self.n_neighbors)][:2]
            else:
                parents = np.random.permutation(self.pop.population_num)[:2]

            off_x = self.crossover.do(self.problem.bounds, genes=self.pop.X[parents])
            off_x = self.mutation.do(self.problem.bounds, genes=off_x)
            off_x = off_x[np.random.randint(0, len(off_x)), None]
            off_pop = Population(off_x)
            off_pop.refresh(self.problem)

            off_f = off_pop.F
            self.ideal_point = np.min(np.vstack([self.ideal_point, off_f]), axis=0)

            FV = self.decomposition.do(self.pop.F[N, :], weights=self.ref_dirs[N, :], utopian_point=self.ideal_point)
            FV_off = self.decomposition.do(off_f, weights=self.ref_dirs[N, :], utopian_point=self.ideal_point)
            I = np.where(FV_off < FV)[0]
            self.pop[N[I]] = off_pop
```
