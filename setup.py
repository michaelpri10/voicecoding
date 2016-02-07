from setuptools import setup
import voicecoding

VERSION = voicecoding.__version__

LONG_DESCRIPTION = open("README.rst").read()

setup(
    name="voicecoding",
    packages=[
        "voicecoding",
        "voicecoding/commandfunctions",
        "voicecoding/helpers"
    ],
    install_requires=["SpeechRecognition"],
    version=VERSION,
    license="MIT",
    description="Python program that allows to code with your voice",
    long_description=LONG_DESCRIPTION,
    author="Michael Prieto (michaelpri10)",
    author_email="michaelpri10@gmail.com",
    url="https://github.com/michaelpri10/voicecoding",
    entry_points={
        "console_scripts": ["voicecoding = voicecoding.voicecoding:main"]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development"
    ]
)
