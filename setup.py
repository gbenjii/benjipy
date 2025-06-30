from setuptools import setup, find_packages

setup(
    name="benjipy",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
    ],
    author="Benjii",
    description="Adatok lekérésére és viccek lekérésére szolgáló Python könyvtár.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gbenjii/benjipy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)