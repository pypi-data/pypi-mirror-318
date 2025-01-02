from setuptools import setup, find_packages

setup(
    name="xnopay",
    version="0.1.0",
    description="Placeholder package for xnopay.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Chirag Asarpota",
    url="https://github.com/strawberrylabs/xnopay",  # Repository URL
    packages=find_packages(),  # Automatically finds the `xnopay` directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
