from setuptools import setup, find_packages

setup(
    name="Proofly",
    version="1.2.4",
    description="Enterprise-grade health metrics analysis and prediction engine",
    author="Mohammed Ufraan",
    author_email="kurosen930@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "dataclasses",
        "typing",
        "datetime",
    ],
    extras_require={
        "dev": ["pytest"],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
