from setuptools import setup, find_packages

setup(
    name="xqywx",
    version="0.2.0",
    packages=find_packages(exclude=["app/*"]),
    install_requires=[
        "requests>=2.25.0"
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="企业微信应用API客户端",
    keywords="企业微信,API,客户端",
    url="http://qy.softinit.com"
) 