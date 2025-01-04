
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pfctl",
    version="0.0.1",
    author="student_v",
    author_email="13974164156@163.com",
    description="Python framework for creating third-party libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vtongxue/pfctl',
    project_urls={'Bug tracker': 'https://github.com/vtongxue/pfctl/issues'},
    classifiers=['Development Status :: 3 - Alpha', 'Programming Language :: Python :: 3', 'License :: OSI Approved :: MIT License', 'Operating System :: OS Independent'],
    packages=["pfctl/"],
    python_requires=">=3.6",
    install_requires = ['setuptools'],
    entry_points=""
        )