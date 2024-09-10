from setuptools import setup, find_packages

setup(
    name="parrot",
    version="0.1.0",
    author="hrszpuk",
    description="A Python GUI program to download and run open-source AI models",
    packages=find_packages(),
    install_requires=[

    ],
    entry_points={
        "console_scripts": [
            "parrot = parrot.gui.app:start_gui",  # Start the GUI from the command line
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
