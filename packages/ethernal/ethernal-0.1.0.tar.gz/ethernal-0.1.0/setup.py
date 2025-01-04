# setup.py
import io
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ethernal",                 # PyPI에 등록될 패키지명 (유니크해야 함)
    version="0.1.0",                 # 버전
    author="ethernal",
    author_email="ethernal@github.com",
    description="Ethernal - Enterprise AI Agent Cloud Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ethernalcloud/ethernal",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "motor",
        "solana",
        "solders",
        "openai",
        "docker",
        "kubernetes",
        "passlib",
        "PyJWT",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: FastAPI",
        "License :: OSI Approved :: MIT License",  # 또는 원하는 라이선스
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.1",

)
