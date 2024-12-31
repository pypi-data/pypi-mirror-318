from setuptools import setup, find_packages

setup(
    name="aloha-mysql-query-builder",  # 包名称
    version="0.1.0",  # 版本号
    packages=find_packages(),  # 自动寻找并包括所有包
    install_requires=[  # 列出依赖
        "mysql-connector-python",
        "pytest",  # 如果你有测试依赖
    ],
    entry_points={  # 如果有命令行工具可以添加
        'console_scripts': [
            'aloha-mysql-query-builder = aloha_mysql.query_builder:main',
        ],
    },
    author="Theadore Lee",
    author_email="admin@theadorelee.com",
    description="A MySQL query builder for Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TheadoreL/aloha-mysql",  # 项目的 GitHub 地址
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # 根据你选择的许可证进行调整
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 你的包支持的最低 Python 版本
)
