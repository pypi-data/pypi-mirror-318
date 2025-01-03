from setuptools import setup, find_packages

setup(
    name='python_example_sdk_debug',
    version='0.1.2',
    packages=[
        "python_example_sdk_debug",
    ],
    package_dir={"python_example_sdk_debug": "python_example_sdk_debug"},
    install_requires=[
        'requests>=2.25.1,<3.0.0',
        'numpy==2.0.0',
        'random_lib_debug==0.3.2'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A description of your Python Example SDK',
    url='https://github.com/yourusername/python-example-sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
        # ... other classifiers ...
    ],
)