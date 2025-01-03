from setuptools import setup, find_packages

setup(
    name="simple_ml_api",  # Package name
    version="0.1.0",  # Version of the package
    author="Your Name",  # Author name
    description="A simple Flask API for doubling a value",  # Description
    packages=find_packages(),  # Automatically finds packages in the directory
    install_requires=["flask"],  # Dependencies
    entry_points={
        "console_scripts": [
            "simple_api=ml_package.api:app.run",  # Running the Flask app
        ],
    },
    python_requires=">=3.7",  # Python version requirement
)
