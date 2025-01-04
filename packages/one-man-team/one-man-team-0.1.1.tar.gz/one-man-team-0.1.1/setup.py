from setuptools import setup, find_packages

setup(
    name='one-man-team',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'python-dotenv',
        'lark-oapi',
    ],
    entry_points={
        'console_scripts': [
            'omt=cli:cli',
        ],
    },
    extras_require={
        'completion': ['click-completion'],
        'test': [
            'pytest>=6.0',
            'pytest-cov',
        ],
    },
) 