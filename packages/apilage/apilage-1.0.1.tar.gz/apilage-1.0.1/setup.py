from setuptools import setup, find_packages

setup(
    name="apilage",  # Updated package name
    version="1.0.1",  # Version
    description="A beginner-friendly programming language.",
    long_description=open("README.md").read(),  # Load README content
    long_description_content_type="text/markdown",
    author="Pasindu Dewviman",
    author_email="your-email@example.com",  # Replace with your email
    url="https://github.com/yourusername/apilage",  # GitHub link
    packages=find_packages(include=["apilage", "apilage.*"]),
    entry_points={
        'console_scripts': [
            'apilage=apilage.interpreter:main',  # CLI command
        ],
    },
    install_requires=[],  # Add dependencies if needed
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
