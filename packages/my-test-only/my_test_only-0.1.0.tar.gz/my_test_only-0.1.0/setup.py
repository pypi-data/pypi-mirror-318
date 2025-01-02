from setuptools import setup, find_packages

setup(
    name="my_test_only",  # 库的名字
    version="0.1.0",
    description="A simple Python library for demonstration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/your_username/my_library",  # 仓库地址
    license="MIT",
    packages=find_packages(),
    install_requires=[],  # 如果有依赖包，写在这里
    python_requires=">=3.6",
)
