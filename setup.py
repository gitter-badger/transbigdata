import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="transbigdata",
    version="0.3.3",
    author="Qing Yu",
    author_email="qingyu0815@foxmail.com",
    description="A Python package developed for transportation spatio-temporal big data processing and analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD",
    url="https://github.com/ni1o1/transbigdata",
    project_urls={
        "Bug Tracker": "https://github.com/ni1o1/transbigdata/issues",
    },
    install_requires=[
        "geopandas","matplotlib","plot_map >= 0.3.6","CoordinatesConverter>=0.1.4"
        ],
    classifiers=[
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    package_dir={'transbigdata': 'src/transbigdata'},
    packages=['transbigdata'],
    python_requires=">=3.7",
)
