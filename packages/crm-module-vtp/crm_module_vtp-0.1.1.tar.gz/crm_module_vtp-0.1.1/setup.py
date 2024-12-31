from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="crm_module_vtp",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    description="A CRM integration module with VTP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'vtp-client=crm_module_vtp.client:main',  # Example entry point
        ],
    },
)
