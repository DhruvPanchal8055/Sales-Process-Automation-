from setuptools import setup
import subprocess
import sys


def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])


install_requirements()


subprocess.run([sys.executable, "main.py"])

setup(
    name="SalesAutomation",
    version="1.0",
    packages=['SalesAutomation'],  # Adjust this to your package structure if needed
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pandas',
        'openpyxl',
        'rich',
        'scrapingdog',
        'serpapi',
    ],
)
