import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='hwhpykit',
    version='1.1.6',
    description='Packaging tools for own use',
    author='louishwh',
    author_email='louishwh@gmail.com',
    url='',
    #packages=['hwhpykit.connection'],
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

