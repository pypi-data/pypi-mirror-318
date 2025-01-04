import datetime
import os

def create(name="''",version="0.0.1",author="''",author_email="''",description="''",long_description="''",long_description_content_type="text/markdown",url="''",project_urls={'Bug tracker': '""'},classifiers=['Development Status :: 3 - Alpha', 'Programming Language :: Python :: 3', 'License :: OSI Approved :: MIT License', 'Operating System :: OS Independent'],packages=[""],python_requires=">=3.6",install_requires = [],entry_points="''"):
    # Create a setup.py file
    with open("setup.py", "w") as f:
        f.write(f"""
import pfctl

pfctl.create(
    name="{name}",
    version="{version}",
    author="{author}",
    author_email="{author_email}",
    description="{description}",
    long_description={long_description},
    long_description_content_type="text/markdown",
    url="{url}",
    project_urls={project_urls},
    classifiers={classifiers},
    packages={packages},
    python_requires="{python_requires}",
    install_requires = {install_requires},
    entry_points={entry_points}
)""")

    year = datetime.datetime.now().year

    with open("pyproject.toml", "w", encoding="utf-8") as f:
        f.write(f"""

[build-system]
requires = [
    "setuptools>=42",
    "wheel"
]
build-backend = "setuptools.build_meta"        
        """
        )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(f"# {name}\nwrite your description here")

    with open("LICENSE", "w", encoding="utf-8") as f:
        f.write(f"""
MIT License

Copyright (c) [{year}] [{name}]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")
    #创建文件夹
    os.makedirs(f'./{name}')
    #创建文件
    with open(f'./{name}/__init__.py', 'w') as f:
        f.write('from .pfctl import *')

    with open(f'./{name}/{name}.py', 'w') as f:
        f.write('# write your python code here.')