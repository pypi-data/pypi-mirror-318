from setuptools import setup, find_packages

setup(
    name='one-man-team',
    version='0.1.2',
    description='One Man Team CLI Tool',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/atorber/one-man-team',
    author='atorber',
    author_email='atorber@163.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'python-dotenv',
        'lark-oapi',
        'tabulate',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'omt=one_man_team.cli:cli',
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