from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PachaMalayalam",  
    version="0.2.0",  
    author="bannawandoor27",
    author_email="bannawandoor@gmail.com",
    description="A transpiler for writing Python code using Malayalam keywords",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bannawanadoor27/PachaMalayalam",  
    packages=find_packages(),  
    include_package_data=True,  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  
    entry_points={
        "console_scripts": [
            "pachalang=pachamalayalam.transpiler:main",  
        ]
    },
    install_requires=[],  
)
