import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CrawlUpDetec",
    version="1.0.3",
    author="Frank",
    # url='xxx',
    # author_email="xxx",
    description="a package help detect website update or not",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)