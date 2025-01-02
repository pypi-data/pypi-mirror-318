from setuptools import setup, find_packages

setup(
    name="deja-file",
    version="1.5.1",
    packages=find_packages(),
    description="A tool for finding duplicate files using MD5",
    long_description_content_type="text/markdown",
    author="Kartik Jain",
    author_email="kartik@yeezus.live",
    url="https://github.com/kartikjain14/deja-file",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'deja-file = deja_file.cli:main',
        ],
    },
    install_requires=[
        'pyopenssl',
    ],
)
