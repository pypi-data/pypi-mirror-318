# `<bomb>HTML</bomb>`

simple html/css templating / static site generator system written in python

# Alpha warning

things may break or will not work properly. Things may break, so consider making a backup of your work the first time trying to use this.

## Usage

### Install/update

**NOTE**: you might want to make this in a virtual environment.
```shell
$ pip install -U wheel
$ pip install -U bombhtml
```

Create a python file in the root of your repository. For example call it `build.py`
```shell
$ touch build.py
```
this file should be in the following structure:
```python
import bombhtml

### CONFIG ###

build = bombhtml.Build()

build.source = "src" # directory from where the files should be taken

build.destination = "public" # where the compiled files should be taken

build.template_prefix = "_._" # which prefix the filler files or directories use to be distinguished. You still can use files that not use this syntax, but that will result in degraded performance when using nested includes, and will result in the fillers remaining in the final build.destination folder

build.regex_placeholder = r"\{\{[^}]*\}\}" # the REGEX string to match placeholders

build.no_output = False # wheter or not print an output to console. Will not apply in case of errors or exceptions.

## BUILDING ###

build.start() # starts the build process

```
the above shown config options are the defaults. If not set, it will use that as option.

Therefore

```python
import bombhtml

build = bombhtml.Build()

build.start()

```
would be the config file using only defaults.

How it works: in this case, it will replace every instance of `{{path_here}}` with the contents of the file of the specified path. The path should be relative to the repositorys root. It is recommended to have each file that gets included that way to have it or it's parent directory begin with `build.template_prefix`, the default being `_._`; so that the used files get removed afterwards. So for example `{{./_._includes/filler.html}}`. The file type doesn't matter, as long as it is a text file.

If you want to skip wrong formatted placeholders (because for example you have another instance of the placeholder you are using) you can use

```python
try:
    build.start() # starts the build process
except TypeError: # skips the file in case of invalid placeholders
    pass
```
instead of

```python
build.start() # starts the build process
```
. This is though not recommended - this will skip the entire file as of now.

You can start the generetor by simply running the config file:

```shell
$ python3 build.py
```

## Development

This guide assumes you have already a virtual enviroment set up and activated.

You can for example us [emailbomb/bombdotemail](https://codeberg.org/emailbomb/bombdotemail) to test your changes, as the repository uses this build system.

1. Build
```shell
$ python3 -m build
```

2. Load the package
```shell
$ pip install --force-reinstall dist/bombhtml-v.v.v-py3-none-any.whl
```
*replace v.v.v with the actual version number. The version number can be found in `./shark_games/__init__.py`*

3. Test pypi *only required before upload un actual pypi* **PLEASE NOTE:** make sure only one version is inside the dist directroy
```shell
$ python3 -m twine upload --repository testpypi dist/*
```

4. Run the tests
```shell
$ test test test
``` 
*not available yet*

## LICENSE

Copyright (C) 2024  sophie (itsme@itssophi.ee)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
