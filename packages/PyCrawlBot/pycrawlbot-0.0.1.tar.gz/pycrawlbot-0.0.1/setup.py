import setuptools

setuptools.setup(
    name="PyCrawlBot",
    version="0.0.1",
    author="student_v",
    author_email="13974164156@163.com",
    description="A simple web crawler",
    long_description='',
    long_description_content_type="text/markdown",
    url="https://github.com/vtongxue/PyCrawlBot",
    project_urls={'Bug tracker': 'https://github.com/vtongxue/PyCrawlBot/issues'},
    classifiers=['Development Status :: 3 - Alpha', 'Programming Language :: Python :: 3', 'License :: OSI Approved :: MIT License', 'Operating System :: OS Independent'],
    packages=['PyCrawlBot'],
    python_requires=">=3.6",
    install_requires = ['beautifulsoup4', 'requests'],
    entry_points=""
)