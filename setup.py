from setuptools import setup, find_packages
from io import open
import os

_version = os.environ.get("CI_COMMIT_TAG", "0.0.2.dev1")
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


requirements = [
    "ta",
]

setup(
    name="FinMind",  # Required
    version=_version,  # Required
    description="financial mining",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/linsamtw",  # Optional
    author="linsam",  # Optional
    author_email="samlin266118@gmail.com",  # Optional
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="financial, python",  # Optional
    packages=find_packages(exclude=["importlib", "pymysql", "ta"]),
    install_requires=requirements,
    project_urls={  # Optional
        "documentation": "https://linsamtw.github.io/FinMindDoc/",
        "Source": "https://github.com/linsamtw/FinMind",
    },
)
