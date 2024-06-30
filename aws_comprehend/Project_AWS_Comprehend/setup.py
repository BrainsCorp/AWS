from setuptools import find_packages, setup

# Replace with your project name
PROJECT_NAME = "Project_AWS_Comprehend"

# AWS SDK for Python (boto3)
AWS_SDK_VERSION = ">=1.26.0"

# Flask framework
FLASK_VERSION = ">=2.2.0"

setup(
    name=PROJECT_NAME,
    version="0.1.0",
    packages=find_packages(exclude=["tests.*", "tests"]),
    install_requires=[
        f"boto3{AWS_SDK_VERSION}",
        f"Flask{FLASK_VERSION}",
    ],
)
