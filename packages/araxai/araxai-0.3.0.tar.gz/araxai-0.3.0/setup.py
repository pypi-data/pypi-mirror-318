import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="araxai",
    version="0.3.0",
    author="(C) Copyright 2021 - 2024 Petr Masa",
    author_email="code@cleverminer.org",
    description="ARAxai is an expainable AI tool based on association rule analysis (therefore ARA).It can be used as XAI method to describe maininfluencers in data as well as to explain model by simplification using association rule analysis. Key influencers of the target variable are extracted.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/petrmasa/araxai",
    project_urls={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=['cleverminer','matplotlib'],
    python_requires=">=3.8"
)