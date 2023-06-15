# kosmos-craftroom
A cheerful mess of tools for working with the KOSMOS spectrograph at APO.

# Documentation
Read (draft!) [documentation](https://zkbt.github.io/kosmos-craftroom).

# Installation

For installing this code we assume you have a Python environment set up, into which you can install packages via `pip`. If so, please continue to one of the installation options below.

If this isn't the case, we recommend installing the [Anaconda Python distribution](https://www.anaconda.com/products/distribution), and using `conda` to manage the `python` environment(s) you have installed on your computer. One tutorial (of many) about how to get started with Python and creating `conda` environments is available [here](https://github.com/ers-transit/hackathon-2021-day0).

## Basic Installation

If you want to install into your current environment, the basic installation should be pretty simple. From the Terminal or Anaconda Prompt, please run
```
pip install git+https://github.com/zkbt/kosmos-craftroom
```
and it should install everything, along with all the necessary dependencies.

If you previously installed this package and need to grab a newer version, run
```
pip install --upgrade git+https://github.com/zkbt/kosmos-craftroom
```
to download any officially released updates.

## Developer Installation

If you want to install this code while being able to edit and develop it, you can clone its [GitHub repository](https://github.com/zkbt/thefriendlystars.git) onto your own computer. This allows you to edit it for your own sake and/or to draft changes that can be contributed to the public package (after being added as a collaborator to the project on GitHub).

To install directly as an editable package on your local computer, run
```
git clone git+https://github.com/zkbt/kosmos-craftroom
cd kosmos-craftroom
pip install -e '.[develop]'
```
The `-e .` will point your environment's `kosmoscraftroom` package to your local folder, meaning that any changes you make in the repository will be reflected in what Python sees when it tries to `import kosmoscraftroom`. Including the `[develop]` after the `.` will install both the dependencies for the package itself and the extra dependencies required for development (= testing and documentation).

## Did it work?
You can quickly test whether your installation worked, and what version you have, by running the Python code
