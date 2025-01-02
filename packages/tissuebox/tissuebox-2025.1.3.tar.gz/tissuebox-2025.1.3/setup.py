from distutils.core import setup

# Read README.md
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="tissuebox",
    version="2025.01.03",
    description="Tissuebox :: Pythonic payload validator",
    author="nehemiah",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="nehemiah.jacob@gmail.com",
    url="https://github.com/nehemiahjacob/tissuebox.git",
    install_requires=[

    ],
    packages=["tissuebox"],
)
