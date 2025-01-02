from setuptools import setup, find_packages

setup(
    name="TextRefine",
    version="1.0.2",
    description="The TextRefine class provides a set of methods for text preprocessing and cleaning.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Rutul Trivedi",
    author_email="rutultrivedi7@gmail.com",
    url="https://github.com/RutulTrivedi/text-refine.git",
    packages=find_packages(where="TextRefine"),
    package_dir={"":"TextRefine"},
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)