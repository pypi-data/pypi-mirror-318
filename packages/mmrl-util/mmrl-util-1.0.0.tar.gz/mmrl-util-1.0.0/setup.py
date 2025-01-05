from setuptools import setup, find_packages

setup(
    name="mmrl-util",
    version="1.0.0",
    description="A tool to build your own Magisk Modules Repository",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Der_Googler & Sanmer",
    author_email="jimmy@dergooglr.com",
    url="https://github.com/Googlers-Repo/magisk-modules-repo-util",
    license="GPL-3.0",
    packages=find_packages(),
    install_requires=[
        "pygithub>=1.59.0",
        "python-dateutil>=2.8.2",
        "requests>=2.31.0",
        "tabulate>=0.9.0",
        "gitpython>=3.1.37",
        "validators>=0.28.3",
        "pyyaml>=6.0.2",
        "python-magic>=0.4.27",
    ],
    entry_points={
        "sync": [
            "sync=sync.cli:main",
        ],
    },
    python_requires=">=3.7",
)