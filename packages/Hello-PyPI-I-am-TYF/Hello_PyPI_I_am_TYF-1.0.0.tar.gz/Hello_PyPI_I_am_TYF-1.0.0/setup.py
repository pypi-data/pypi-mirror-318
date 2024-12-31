from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Hello_PyPI_I_am_TYF",  #  用你的用户名替换 "your-username"
    version="1.0.0",
    author="TYF",
    author_email="2354971232@qq.com",
    description="A simple calculator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/calculator", # 替换为你的仓库地址
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
