import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="star_jwt",
    version="0.3.2",
    author="retnikt",
    author_email="_@retnikt.uk",
    description="JSON Web Token authenticator backend for Starlette's authentication system.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/retnikt/starlette_jwt",
    packages=["star_jwt"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Internet :: WWW/HTTP",
        "Typing :: Typed",
    ],
    python_requires='>=3.8',
    install_requires=[
        "starlette >= 0.9.6",
        "pyjwt >= 1.0.1"
    ]
)
