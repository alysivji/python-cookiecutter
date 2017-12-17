from setuptools import setup, find_packages

setup(
    name='{{ cookiecutter.project_slug.replace('_','-') }}',
    version='0.0.1',
    description='{{ cookiecutter.project_description }}',
    url='https://github.com/{{ cookiecutter.github_id }}/{{ cookiecutter.project_slug.replace('_','-') }}',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.author_email }}',
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['tests', ]),
    install_requires=[''],
    download_url='https://github.com/{{ cookiecutter.github_id }}/{{ cookiecutter.project_slug.replace('_','-') }}',
)
