from setuptools import setup, find_packages

setup(
    name='mGenS',  # Replace with your package name
    version='0.1.2',  # Initial version
    author='Hathaway Zhang',  # Your name
    author_email='hathawayzhang@gmail.com',  # Your email
    description='Support functions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hathaaaway/mgens',  # URL to your package's repository
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update based on your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify your Python version requirement
)