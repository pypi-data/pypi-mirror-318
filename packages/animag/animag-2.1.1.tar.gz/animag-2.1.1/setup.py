from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='animag',
    version='2.1.1',
    packages=find_packages(exclude=['tests*']),
    install_requires=requirements,
    entry_points={
        'console_scripts': ['animag=animag.cli:main'],
    },
    author='adogecheems',
    author_email='master@mmoe.work',
    description='Anime magnet search library with strong scalability.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/adogecheems/animag',
    license='AGPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='plugin rss torrent scraper scalable scalability magnet-link torrents magnet animes nyaa-magnet-links '
             'nyaa anime-scraper dmhy nyaa-si animetosho tokyotoshokan acgrip dmhy-org acg-rip',
)
