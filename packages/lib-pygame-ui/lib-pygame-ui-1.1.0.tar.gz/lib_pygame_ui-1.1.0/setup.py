from setuptools import find_packages, setup

with open('requirements.txt') as req:
    install_requirements = req.read().splitlines()

with open('README.md', 'r') as README:
    readme = README.read()

setup(
    name = 'lib-pygame-ui',
    version = '1.1.0',
    description = 'gui/elements for pygame.',
    author = 'azzammuhyala',
    author_email = 'azzammuhyala@gmail.com',
    license = 'MIT',
    python_requires ='>=3.11',
    long_description_content_type = 'text/markdown',
    long_description = readme,
    packages = find_packages(),
    include_package_data = True,
    install_requires = install_requirements,
    keywords = [
        'pyg_ui', 'pygameui', 'pygamegui', 'pygame gui', 'libpygameui', 'lib-pygame-ui'
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)