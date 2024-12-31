from setuptools import setup, find_packages

setup(
    name="byteai",
    version="0.1.4",
    packages=find_packages(),
    install_requires=[
        "tiktoken",
        "stripe",
        "aiohttp",
        "numpy"
    ],
    author="Aaron Jerez",
    author_email="aaronjerez1@gmail.com",
    description="AI development tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)