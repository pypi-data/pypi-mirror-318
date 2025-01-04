from setuptools import setup, find_packages

setup(
    name="hawkpy",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'cryptography>=3.4.7',
        'ipaddress>=1.0.23'
    ],
    author="harimtim",
    author_email="harimtim@icloud.com",
    description="Advanced Python Security & Analysis Framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/harimtim/hawkpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 