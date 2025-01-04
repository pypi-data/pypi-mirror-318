# pfctl

Python framework for creating third-party libraries

## How to use

install:

```bash
    pip install pfctl
```
use:
1. create a a.py file and write some code like this:
```python
    import pfctl
    pfctl.create(
        name="",
        version="0.0.1",
        author="",
        author_email="",
        description="",
        long_description_content_type="text/markdown",
        url="",
        project_urls={'Bug tracker': ''},
        classifiers=['Development Status :: 3 - Alpha', 'Programming Language :: Python :: 3', 'License :: OSI Approved :: MIT License', 'Operating System :: OS Independent'],
        packages=[""],
        python_requires=">=3.6",
        install_requires = [],
        entry_points=""
    )
```

2. write this command in the terminal and download the package:
```bash
    pip install build
    pip install twine
```

3. write this command in the terminal to build the package:
```bash
    python -m build
```

4. write this command in the terminal to upload the package:
```bash
    python -m twine upload dist/*
```

5. write your username and password in the terminal, or write your APItoken in the terminal and upload the package:
```bash
    username:***
    password:***
```
or
```bash
    APItoken:***
```

Then the package will be uploaded to the pypi server.

## How to download your package

1. write this command in the terminal to download the package:
```bash
    pip install your_package_name
```

2. write this command in the terminal to use the package:
```bash
    import your_package_name
```

## Version change

------ 0.0.1: first version

------ 0.0.2: fix some bugs in the setup.py file