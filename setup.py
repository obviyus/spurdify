import setuptools
import re
import os.path


def get_file(*paths):
    path = os.path.join(*paths)
    try:
        with open(path, 'rb') as f:
            return f.read().decode('utf8')
    except IOError:
        pass


def get_version():
    init_py = get_file(os.path.dirname(__file__), 'googletrans', '__init__.py')
    pattern = r"{0}\W*=\W*'([^']+)'".format('__version__')
    version, = re.findall(pattern, init_py)
    return version


def get_description():
    init_py = get_file(os.path.dirname(__file__), 'googletrans', '__init__.py')
    pattern = r'"""(.*?)"""'
    description, = re.findall(pattern, init_py, re.DOTALL)
    return description


with open("README.md", "r") as fh:
    long_description = fh.read()


def install():
    setuptools.setup(
        name="spurdify",  # Replace with your own username
        version=get_version(),
        description=get_description(),
        author="obviyus",
        author_email='hi' '@' 'obviy.us',
        long_description_content_type="text/markdown",
        url="https://github.com/obviyus/spurdify",
        packages=setuptools.find_packages(exclude='tests'),
        keywords='spurdo spurdify regex',
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GPLv3",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )


if __name__ == "__main__":
    install()
