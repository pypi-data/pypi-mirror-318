from setuptools import setup, find_packages

setup(
    name='com-chery-pom-root',
    version='0.0.1',
    packages=[
        'com_chery',
        'chery_pom_tool',
    ],
    include_package_data=True,
    install_requires=[
        'requests',
        'python-dotenv',
    ],
    description='temp package, will be deleted later 2025-01-02',
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    # author='Your Name',
    # author_email='your.email@example.com',
    # url='https://example.com/com_example_root',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
