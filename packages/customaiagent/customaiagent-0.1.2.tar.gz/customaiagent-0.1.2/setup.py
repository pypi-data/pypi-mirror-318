from setuptools import setup, find_packages

setup(
    name="agent_sdk",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "cryptography",
        "huggingface_hub",
        "openai",
        "streamlit"
    ],
)