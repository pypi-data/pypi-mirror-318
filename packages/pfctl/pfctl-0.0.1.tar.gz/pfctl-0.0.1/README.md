# pfctl

Python framework for creating third-party libraries

## Usage

install:

```bash
    pip install pfctl
```
use:
create a a.py file and write some code like this:
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