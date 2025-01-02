from setuptools import setup, find_packages

setup(
    name="TerminatorCore",  # 包名
    version="0.1.14",    # 包的版本
    packages=find_packages(include=['TerminatorBaseCore', 'TerminatorBaseCore.*']),  # 自动发现包内的所有模块
    install_requires=[   # 依赖项
        "annotated-types==0.7.0",
        "asgiref==3.8.1",
        "django-cors-headers==4.6.0",
        "django-redis==5.4.0",
        "djangorestframework==3.15.2",
        "ecdsa==0.19.0",
        "PyMySQL==1.1.1",
        "mysqlclient==2.2.5",
        "pyasn1==0.6.1",
        "PyJWT==2.10.1",
        "redis==5.2.0",
        "requests==2.32.3",
        "rsa==4.9",
        "setuptools==75.6.0",
        "six==1.16.0",
        "sqlparse==0.5.1",
        "tzdata==2024.2",
    ],
    author="bw.song",  # 作者
    author_email="tyj003@163.com",  # 作者邮箱
    description="django增强",  # 包的简短描述
    long_description=open('TerminatorBaseCore/README.md', encoding='utf-8').read(),  # 从 README 文件读取更详细的描述
    long_description_content_type="text/markdown",  # README 文件格式
    classifiers=[  # 项目分类，用于 PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',  # 兼容的 Python 版本
    license="MIT",
    keywords="Terminator,SONG"
)
