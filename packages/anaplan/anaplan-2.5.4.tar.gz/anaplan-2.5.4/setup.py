from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Setting Up
setup(
    name="anaplan",
    version="2.5.4",
    author="Hasan Can Beydili",
    author_email="tchasancan@gmail.com",
    description=(
        "* Anaplan is a machine learning library written in Python for professionals, incorporating advanced, unique, new, and modern techniques.\n"
        "* Changes: Anaplan library name changed to 'pyerualjetwork'. Please use this: pip install pyerualjetwork"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=[
        "model evaluation",
        "classification",
        "potentiation learning artificial neural networks",
        "NEAT",
        "genetic algorithms",
        "reinforcement learning",
        "neural networks",
    ],
)