from setuptools import setup, find_packages

setup(
    name="totindex",
    version="1.0.0",
    description="A sample Python package",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your-repo/totindex",
    packages=find_packages(),  # 自动发现所有 Python 包
    include_package_data=False,  # 不包含额外的非代码文件
    install_requires=[
        # 添加你的依赖包，例如:
        # "numpy>=1.20.0",
    ],
    entry_points={
        "console_scripts": [
            "totindex=totindex.main:main",  # 命令行入口
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
