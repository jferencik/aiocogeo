from setuptools import setup

setup(
    name="async-cog-tiler",
    version="0.1",
    author=u"Jeff Albrecht",
    author_email="geospatialjeff@gmail.com",
    url="https://github.com/geospatial-jeff/async-cog-reader",
    license="mit",
    install_requires=[
        "aiohttp",
    ],
    test_suite="tests",
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        "pytest",
        "pytest-asyncio",
        "pytest-cov",
        "rasterio"
    ]
)