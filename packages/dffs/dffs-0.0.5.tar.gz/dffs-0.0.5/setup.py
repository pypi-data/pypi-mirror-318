from setuptools import setup, find_packages

setup(
    name='dffs',
    version="0.0.5",
    description="Pipe and diff files: execute shell pipelines against multiple inputs, diff/compare/join results.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=open("requirements.txt").read(),
    entry_points={
        'console_scripts': [
            'diff-x = dffs.diff_x:main',
            'comm-x = dffs.comm_x:main',
            'git-diff-x = dffs.git_diff_x:main',
        ],
    },
    license="MIT",
    author="Ryan Williams",
    author_email="ryan@runsascoded.com",
    author_url="https://github.com/ryan-williams",
    url="https://github.com/runsascoded/dffs",
)
