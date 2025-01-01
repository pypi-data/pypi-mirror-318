from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="modularis",
    version="0.1.0",
    author="Hexakleo",
    author_email="hexakleo@gmail.com",
    description="A Modern, High-Performance HTTP Client Library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hexakleo/modularis",
    project_urls={
        "Bug Tracker": "https://github.com/hexakleo/modularis/issues",
        "Documentation": "https://modularis.readthedocs.io/",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
)
