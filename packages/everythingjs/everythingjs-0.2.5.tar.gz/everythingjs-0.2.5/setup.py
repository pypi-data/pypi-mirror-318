import os
import urllib.request
from setuptools import setup, find_packages
from setuptools.command.install import install

class PostInstallCommand(install):
    """Custom post-installation for creating ~/.everythingjs/ directory and saving secrets.regex."""
    def run(self):
        # Call the standard install process first
        install.run(self)

        # Define the directory and file path
        everythingjs_dir = os.path.expanduser('~/.everythingjs/')
        secrets_file_path = os.path.join(everythingjs_dir, 'secrets.regex')

        # Create the directory if it doesn't exist
        os.makedirs(everythingjs_dir, exist_ok=True)

        # URL to the secrets.regex file
        secrets_url = 'https://raw.githubusercontent.com/profmoriarity/everythingjs/refs/heads/main/secrets.regex'

        # Download the file
        try:
            print(f"Downloading {secrets_url} to {secrets_file_path}...")
            urllib.request.urlretrieve(secrets_url, secrets_file_path)
            print(f"File saved to {secrets_file_path}")
        except Exception as e:
            print(f"Failed to download the file: {e}")

setup(
    name='everythingjs',
    version='0.2.5',  # Incremented version for updates
    author='Siva Krishna',
    author_email='krishna.krish759213@gmail.com',
    description='A Python module for working seamlessly with JavaScript files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/profmoriarity/everythingjs',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'beautifulsoup4',  # For HTML parsing
        'requests',        # For HTTP requests
        'tqdm',
        'flask',
        'jsbeautifier',
        'flask-socketio'
    ],
    entry_points={
        'console_scripts': [
            'everythingjs=everythingjs.app:main',  # CLI entry point
        ],
    },
    include_package_data=True,  # Includes files specified in MANIFEST.in
    package_data={
        'everythingjs': [
            'templates/*',    # Include all files in the templates directory
            'secrets.regex',  # Include the secrets.regex file
        ],
    },
    cmdclass={
        'install': PostInstallCommand,
    },
)
