from setuptools import setup, find_packages

setup(
    name="singhtech-colabcode-v1",
    version="0.1.0",  # You can update this version
    description="A package for running VS Code on Colab with ngrok",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Shalu Singh",
    author_email="singhtech.10@gmail.com",
    url="https://github.com/shalusingh-tech/colabcode",  # Replace with your GitHub URL
    packages=find_packages(),  # Automatically finds all Python packages in the project
    install_requires=[
        "pyngrok",  # Add any dependencies needed by your package
        "nest_asyncio",
        "uvicorn",
        # "google-colab",  # For Colab-specific functionality (only if needed)
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with your actual license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",  # Specify the required Python version
)
