from setuptools import setup, find_packages

setup(
    name="Azelia-hash",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "argon2-cffi==21.1.0",
        "bcrypt==3.2.0",
        "mysql-connector-python==8.0.27",
        "pymysql==1.0.2",
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="john chris",
    author_email="idiomajohnchris049@gmail.com",
    description="A combination of 2 hashing algorithms",
    url="https://github.com/Penuts8773/Azelia-hash",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
