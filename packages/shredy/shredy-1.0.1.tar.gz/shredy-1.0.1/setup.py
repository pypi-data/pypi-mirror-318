from setuptools import setup, find_packages

setup(
    name="shredy",  # Package name
    version="1.0.1",  # Version
    author="Cody Shirriff",  # Your name
    author_email="shredy.tax@gmail.com",  # Your email
    description="Create support docs for SR&ED reporting",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/csshirri/shredy_git.git",  # Repository URL
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        "certifi==2024.12.14",
        "charset-normalizer==3.4.0",
        "contourpy==1.3.0",
        "cycler==0.12.1",
        "fonttools==4.55.3",
        "fpdf2==2.8.2",
        "idna==3.10",
        "kiwisolver==1.4.7",
        "matplotlib==3.10.0",
        "numpy==2.2.0",
        "packaging==24.2",
        "pandas==2.2.3",
        "pillow==11.0.0",
        "pyparsing==3.2.0",
        "python-dateutil==2.9.0.post0",
        "pytz==2024.2",
        "requests==2.32.3",
        "seaborn==0.13.2",
        "six==1.17.0",
        "tzdata==2024.2",
        "urllib3==2.2.3",
    ],
    entry_points={
        "console_scripts": [
            "shredy=shredy_git.shredy_git:main",  # CLI command
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

