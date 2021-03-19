from setuptools import setup, find_packages

version = "1.0"

setup(
    name="ApiTestBasic",
    version=version,
    author="lin",
    description="easy graphql api object test",
    packages=find_packages(exclude=("Schema", "test")),
    python_requires='>=3.9',
    install_requires=[
        "sgqlc", "pytest", "Faker", "allure-pytest", "beeprint", "python_utils"
    ],
    entry_points={
        'console_scripts': [
            'api_codegen=ApiTestBasic.graphql_api_codegen:main',
        ],
    },
    zip_safe=False

)
