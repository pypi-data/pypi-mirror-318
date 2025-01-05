from setuptools import setup, find_packages

setup(
    name="reqs-checker",
    version="1.0.0",
    description="A tool to check installed Python package versions against requirements.txt and PyPI.",
    author="Benevolence Messiah",
    author_email="benevolencemessiah@gmail.com",
    url="https://github.com/BenevolenceMessiah/reqs-checker",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "packaging>=21.0"
    ],
    entry_points={
        "console_scripts": [
            "reqs-checker=reqs_checker.checker:main",  # CLI command
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)