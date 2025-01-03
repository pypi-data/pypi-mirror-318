import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='hwhkit',
    version='1.0.0',
    description='Packaging tools for own use',
    author='louishwh',
    author_email='louishwh@gmail.com',
    url='',
    #packages=['hwhkit.connection'],
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.10',
    install_requires = [
        'paho-mqtt>=2.0.0',
        'loguru==0.6.0',
        'anthropic[bedrock]~=0.23.1',
        'openai~=1.3.8'
    ],
    classifiers=[  # PyPI 分类
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

