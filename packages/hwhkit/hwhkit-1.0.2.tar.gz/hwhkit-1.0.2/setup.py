import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='hwhkit',
    version='1.0.2',
    description='Packaging tools for own use',
    author='louishwh',
    author_email='louishwh@gmail.com',
    url='',
    #packages=['hwhkit.connection'],
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.10',
    install_requires=[
        'paho-mqtt>=2.1.0',
        'loguru==0.6.0',
        'openai~=1.58.1',
        'anthropic~=0.42.0',
        'httpx==0.25.2',
        'tiktoken==0.8.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

