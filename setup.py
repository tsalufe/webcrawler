import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="webcrawler",
    version="0.0.1",
    author="Billy Cai",
    author_email="tsalufe@gmail.com",
    description="Crawl web page to find your content using selenium and web driver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tsalufe/webcrawler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)