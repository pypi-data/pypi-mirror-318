from setuptools import setup, find_packages

setup(
    name="rag_eval_tool",  # Your library's name
    version="0.1.8",  # Initial version
    description="A comprehensive evaluation toolkit for RAG and LLMs.",
    long_description=open("README.md").read(),  # Long description from README
    long_description_content_type="text/markdown",  # README file format
    author="Pratik Bhande",  # Replace with your name
    author_email="pratikbhande2@gmail.com",  # Replace with your email
    packages=find_packages(),  # Automatically find sub-packages
    install_requires=[
        "torch",
        "sacrebleu",
        "rouge-score",
        "bert-score",
        "transformers",
        "nltk",
        "textstat",
        "scikit-learn",
        "numpy",
        "protobuf",
        "tqdm"
    ],  # List of dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Minimum Python version
)



