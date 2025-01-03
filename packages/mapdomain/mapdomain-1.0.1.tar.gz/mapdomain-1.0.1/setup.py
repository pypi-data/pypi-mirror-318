from setuptools import setup, find_packages

setup(
    name="mapdomain",
    version="1.0.1",
    author="Mohamed",
    author_email="icn@icneg.com",
    description="A tool for subdomain enumeration and sitemap creation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mohamedicn/mapdomain",
    packages=find_packages(),  
    install_requires=[
        "requests",
        "beautifulsoup4",
        "art",
    ],
    python_requires=">=3.6",
)
