from setuptools import setup, find_packages

setup(
    name="LTPpyTools",  # 包名稱
    version="0.2.1",     # 版本號
    author="LTPLAX",
    author_email="leoverysmallno10@gmail.com",
    description="A python package for any python program develop.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LightingXT/Tools?tab=MIT-1-ov-file",  
    packages=find_packages(),  # 自動尋找子模組
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
