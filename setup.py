import setuptools

# with open("README.md", "r") as fh:
    # long_description = fh.read()

setuptools.setup(
    name="asd",
    version="0.0.1",
    author="theunderdog",
    author_email="ahmedbonumstelio@gmail.com",
    description="if it takes more than 90secs Automate it!",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/theunderdog/asd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts':['asd=asd.asd:main']
        }
)
