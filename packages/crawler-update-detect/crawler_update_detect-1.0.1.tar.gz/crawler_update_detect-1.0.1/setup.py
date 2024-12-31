import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crawler_update_detect",
    version="1.0.1",
    author="Frank",
    # url='xxx',
    # author_email="xxx",
    description="A package to detect whether html ODM and text has been change",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
