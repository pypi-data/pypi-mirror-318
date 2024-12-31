import os
import sys
from setuptools import setup, find_packages

NAME = "darwin-moea"
AUTHOR = "qianjiduo"
EMAIL = ""
URL = "https://github.com/qjdbfccc/darwin-moea.git"
LICENSE = "MIT License"
DESCRIPTION = "A multi-objective optimization algorithm library implemented in Python, containing some basic operators and commonly used multi-objective optimization algorithms."

if sys.version_info < (3, 6, 0):
    raise RuntimeError(f"{NAME} requires Python >=3.6.0, but yours is {sys.version}!")

try:
    lib_py = os.path.join(NAME, "__init__.py")
    with open(lib_py, "r", encoding="utf8") as f_v:
        v_line = ""
        for line in f_v.readlines():
            if line.startswith("__version__"):
                v_line = line.strip()
                break
        exec(v_line)  # get __version__ from __init__.py
except FileNotFoundError:
    __version__ = "0.0.4"

try:
    with open("README.md", encoding="utf8") as f_r:
        _long_description = f_r.read()
except FileNotFoundError:
    _long_description = ""

if __name__ == "__main__":
    setup(
        name=NAME,
        version=__version__,
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        description=DESCRIPTION,
        packages=find_packages(),
        include_package_data=True,
        setup_requires=["setuptools>=18.0", "wheel"],
        install_requires=open("./requirements.txt", "r").read().splitlines(),
        long_description=_long_description,
        long_description_content_type="text/markdown",
        entry_points={
            "console_scripts": [
                "package_name=package_name.shell:run"
            ]
        },
        package_data={
            "package_name": ["src/*.txt"]
        },
        zip_safe=True,
        classifiers=[
            "Programming Language :: Python :: 3",
            f"License :: OSI Approved :: {LICENSE}",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.8",
        project_urls={
            "Source": "https://github.com/qjdbfccc/darwin-moea.git"
        }
    )
