from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="irisool-calculator",  #  用你的用户名替换 "your-username"
    version="1.0.1",
    author="irisool",
    author_email="liul75433@gmail.com",
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
