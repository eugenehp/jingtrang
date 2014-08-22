from setuptools import setup, find_packages
import os

here = os.path.abspath(".")
README = open(os.path.join(here, "README.rst")).read()
NEWS = open(os.path.join(here, "NEWS.rst")).read()

setup(
    name="jingtrang",
    version="0.1dev",
    description="Wrapping jing and trang RELAX NG tools into Python script",
    long_description=README + "\n" + NEWS,
    author="Jan Vlcinsky",
    author_email="jan.vlcinsky@tamtamresearch.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pyjing=jingtrang:jing",
            "pytrang=jingtrang:trang"
        ]
    },
    zip_safe=False,
    package_data={"jingtrang": ["*.jar"]}
)
