from setuptools import setup, find_packages

setup(
    name="byteai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tiktoken",
        "stripe",
        "aiohttp",
        "numpy"
    ],
    author="Aaron Jerez",
    description="AI development tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)