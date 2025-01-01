# setup.py
from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

def read_requirements(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="summarygen",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,  # This is important for including non-Python files
    install_requires=read_requirements('./requirements.txt'),
    extras_require={
        'dev': [
            'pytest>=7.0',
            'pytest-cov>=4.0',
            'pytest-mock>=3.10.0',
            'requests-mock>=1.11.0',
            'black>=22.0.0',
            'twine>=4.0.0',
            'build>=0.10.0',
            'wheel>=0.36.0',
        ],
    },
    entry_points={
        "console_scripts": [
            "summarygen=summarizer.cli:main",
        ],
    },
    author="Soonwook Hwang",
    author_email="hwang@kisti.re.kr",
    description="A command-line tool for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hwang2006/summarygen",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)