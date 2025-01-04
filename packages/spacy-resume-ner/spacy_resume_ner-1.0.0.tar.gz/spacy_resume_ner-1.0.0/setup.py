from setuptools import setup, find_packages

setup(
    name="spacy-resume-ner",
    version="1.0.0",
    description="A spaCy model for Named Entity Recognition (NER) on resumes",
    author="Ankit Kumar",
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["*.json", "*.cfg"]},
    install_requires=[
        "spacy>=3.0.0,<4.0.0",
        "spacy-transformers>=1.1.5,<1.2.0"
    ],
    python_requires=">=3.9,<3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent",
    ],
)
