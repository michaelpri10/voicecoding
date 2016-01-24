from setuptools import setup
import voice_coding

VERSION = voice_coding.__version__

LONG_DESCRIPTION = open("README.rst").read()

setup(
    name="VoiceCoding",
    packages=["voice_coding"],
    version=VERSION,
    description="Python program that allows to code with your voice",
    long_description=LONG_DESCRIPTION,
    author="Michael Prieto (michaelpri10)",
    author_email="michaelpri10@gmail.com",
    url="https://github.com/michaelpri10/VoiceCoding",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development"
    ]
)
