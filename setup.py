from setuptools import setup, find_packages

setup(
    name="jv-env-cli",
    version="1.0.0",
    author="Sachin Acharya",
    author_email="example@gmail.com",
    description="JV-CLI is a lightweight command-line tool for managing Java environments. Easily switch between Java versions, set JAVA_HOME, persist changes, and configure multiple installations effortlessly.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sachin-acharya-projects/jv-cli",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "jv=jv_cli.__init__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

# python setup.py sdist bdist_wheel
# twine upload dist/*
