import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='hwhpykit',  # 包名字
    version='1.1.1',  # 包版本
    description='Packaging tools for your own use',  # 简单描述
    author='louishwh',  # 作者
    author_email='louishwh@gmail.com',  # 作者邮箱
    url='',  # 包的主页
    #packages=['hwhpykit.cache']
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.10',
    install_requires = [
        'redis>=3.5.3',
        'pymysql>=1.1.0',
        'paho-mqtt>=2.0.0'
    ],
    classifiers=[  # PyPI 分类
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

