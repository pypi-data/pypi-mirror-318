from setuptools import setup, find_packages

setup(
    name="data-auto-profiler",
    version="0.1.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas>=2.2.2",
        "numpy>=1.26.4",
        "plotly>=5.22.0",
        "scipy>=1.13.1",
        "nbformat>=4.2.0"
    ],
    python_requires=">=3.8"
)
