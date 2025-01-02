from setuptools import setup, find_packages

with open("version", "r") as fh:
    version = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='wireshark_fieldbus_io',
    version=version,
    packages=find_packages(),
    install_requires=required,
    author='mrBrutus',
    description='Extract fieldbus IO data from Wireshark capture files.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/mrBrutus/wireshark_fieldbus_io',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Networking',
    ],
    python_requires='>=3.12',
    license='MIT License',
)
