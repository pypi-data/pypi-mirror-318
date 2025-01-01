from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='polaris-cli-tool',
    version='1.0.9',  # Increment version
    description='Polaris CLI - Modern Development Workspace Manager for Distributed Compute Resources',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Polaris Team',
    author_email='mubarakabanadda68@gmail.com',
    url='https://github.com/BANADDA/polaris-cli',
    packages=['polaris_cli'],  # Only include polaris_cli package
    include_package_data=True,
    install_requires=[
        'click==8.1.3',
        'tabulate==0.8.10',
        'click-spinner',
        'rich',
        'inquirer',
        'requests',
        'xlsxwriter',
        'pyyaml',
        'psutil',
        'python-dotenv',
        'pid',
        'communex==0.1.36.4',
    ],
    entry_points={
        'console_scripts': [
            'polaris=polaris_cli.cli:cli',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)