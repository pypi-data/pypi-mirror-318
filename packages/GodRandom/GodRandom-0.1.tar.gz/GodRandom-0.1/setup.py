from setuptools import find_packages, setup

setup(
    name="GodRandom",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    test_suite="tests",
    author="Rodionov Andrew",
    author_email="dron3915work@gmail.com",
    description="Simple library for random generations",
    long_description=open("README.md", encoding="utf-8").read(),  # Указываем кодировку
    long_description_content_type="text/markdown",
    url="https://github.com/Dron3916/GodRandom",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
