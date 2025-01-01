from pathlib import Path

import setuptools

VERSION = "0.0.1"  # PEP-440

NAME = "translatium"

INSTALL_REQUIRES = [
    "pyyaml",
]


setuptools.setup(
    name=NAME,
    version=VERSION,
    description="A pure Python i18n library for your Python projects.",
    url="https://github.com/CEOXeon/Translatium",
    project_urls={
        "Source Code": "https://github.com/CEOXeon/Translatium",
    },
    author="Louis Zimmermann (@CEOXeon)",
    author_email="louis-github@tutanota.com",
    license="Apache-2.0",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
    #python_requires=">=3.8",
    # Requirements
    install_requires=INSTALL_REQUIRES,
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
)