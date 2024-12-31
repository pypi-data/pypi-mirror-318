
from setuptools import find_packages, setup

with open("app/README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='mltoarduino',
    version='0.0.7',
    description="See readMe.ma",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bouz1/PypiContributions/tree/main/mltoarduino',
    author="bouz1.github.io",
    author_email="bozzabb1@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    

    #install_requires=[],
    extras_require={
        "dev": ['pyperclip','pandas','numpy'],

    },
    python_requires=">=3.1",
)
