from setuptools import setup, find_packages

setup(
    name="jingtrang",
    version="0.1dev",
    description="Wrapping jing and trang RELAX NG into Python script",
    author="Jan Vlcinsky",
    author_email="jan.vlcinsky@tamtamresearch.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pyjing=jingtrang:jing",
            "pytrang=jingtrang:trang"
        ]
    },
    zip_safe=False
)
