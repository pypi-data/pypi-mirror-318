from setuptools import setup, find_packages

setup(
    name="BruhScript",
    version="1.0.3",  # Updated version
    author="dimaniojk",
    author_email="your.email@example.com",
    description="A meme-based programming language that's surprisingly powerful.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dimaniojk/BruhScript",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "bruhscript=bruhscript.core:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
