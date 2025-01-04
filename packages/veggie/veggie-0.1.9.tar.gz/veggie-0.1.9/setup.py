from setuptools import find_packages, setup

setup(
    name="veggie",
    version="0.1.9",
    author="Theodore Tsitsimis",
    description="A tool to monitor and execute Celery tasks",
    packages=find_packages(),
    install_requires=[
        "dash>=2.5.1",
        "dash-extensions>=1.0.19",
        "dash-mantine-components>=0.15.1",
        "dash-iconify",
        "loguru",
        "celery[redis]",
        "humanize",
    ],
)
