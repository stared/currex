from setuptools import setup, find_packages

setup(
    name="pythonic_money",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests>=2.31.0"],
    python_requires=">=3.10",
    author="Currency Calculator Team",
    description="A Pythonic currency calculator with real-time exchange rates",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pythonic-money",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
