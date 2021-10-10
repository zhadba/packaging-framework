import setuptools

with open("README.txt", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zhadba-packaging-framework",
    version="0.0.1",
    author="Zachary Hadba",
    author_email="zhadba@gmail.com",
    description="A skeleton for future packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhadba/packaging-framework",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)