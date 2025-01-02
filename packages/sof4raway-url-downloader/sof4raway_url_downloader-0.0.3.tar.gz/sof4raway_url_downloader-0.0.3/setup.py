from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="sof4raway_url_downloader",
    version="0.0.3",
    description="A Custom Library for Downloading Files from URLs",
    packages=find_packages(exclude=["test"]),
    install_requires=[
        'requests',
        'tqdm'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Operating System :: OS Independent',  # General classifier for OS compatibility
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',  # Specify the Python version
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Muhammad Farid Rahman",
    keywords="URL Downloader",
    url='https://github.com/sof4raway',
    python_requires=">=3.10",
)
