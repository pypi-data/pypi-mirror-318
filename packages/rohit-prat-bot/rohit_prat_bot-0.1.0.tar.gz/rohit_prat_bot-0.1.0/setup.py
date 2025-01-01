from setuptools import setup, find_packages

setup(
    name="rohit_prat_bot",
    version="0.1.0",
    author="Rohit Prat",
    author_email="legacy.business18@gmail.com",
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rp-bot/rpbot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # Add your package dependencies here
    ],
)
