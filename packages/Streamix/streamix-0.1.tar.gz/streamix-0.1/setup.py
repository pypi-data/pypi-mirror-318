from setuptools import setup, find_packages

setup(
    name="Streamix",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "yt-dlp",
        "pytube"
    ],
    entry_points={
        'console_scripts': [
            'snapstream = SnapStream.index:main',
        ],
    },
)
