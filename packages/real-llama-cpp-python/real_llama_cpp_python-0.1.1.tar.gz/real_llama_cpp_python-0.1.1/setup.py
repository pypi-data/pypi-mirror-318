from setuptools import setup, find_packages

setup(
    name="real-llama-cpp-python",
    version="0.1.1",
    description="A simple custom LLM wrapper for llama.cpp with LangChain compatibility.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Minh Tran",
    url="https://github.com/minhtran1309/custom_llm",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "langchain-core",
        "pydantic"
    ],
)