from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    author="hicinformatic",
    author_email="hicinformatic@gmail.com",
    name="django-smart-export",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU General Public License v3 (GPLv3)",
    install_requires=[
        "django>=4.2",
    ],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    url="https://github.com/hicinformatic/django-smart-export",  # Lien vers ton repo GitHub
)
