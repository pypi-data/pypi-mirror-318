from setuptools import setup, find_packages

# get requirements from requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='xlate',
    version='0.0.1',
    description='Advanced translation',
    author='xlate',
    author_email='dyllan@xlate.ai',
    url='https://xlate.ai',
    packages=find_packages(),
    install_requires=required,
    entry_points={
        'console_scripts': [
            'xlate=xlate.cli:main',  # Assuming your CLI code will be in gitxdb/cli.py
        ],
    },
    python_requires='>=3.11',
    # classifiers=[
    #     'Development Status :: 3 - Alpha',
    #     'Intended Audience :: Developers',
    #     'License :: OSI Approved :: MIT License',
    #     'Programming Language :: Python :: 3',
    #     'Programming Language :: Python :: 3.6',
    #     'Programming Language :: Python :: 3.7',
    #     'Programming Language :: Python :: 3.8',
    #     'Programming Language :: Python :: 3.9',
    # ],
)