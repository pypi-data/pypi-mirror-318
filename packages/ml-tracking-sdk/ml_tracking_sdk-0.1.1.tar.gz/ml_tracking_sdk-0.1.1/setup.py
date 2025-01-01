from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ml_tracking_sdk",
    version="0.1.0",
    author="Shepard",
    author_email="zhaoxun@sais.com.cn",
    description="An ml tracking SDK with configuration and decorator support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://gitlab-paas.internal.sais.com.cn/data_intelligence_platform/mlflow_sdk",
    packages=find_packages(),
    install_requires=[
        "mlflow>=2.0.0",
        "PyYAML>=6.0",
        "scikit-learn>=1.2.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
