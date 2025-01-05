# API Key Locator (APIKL) #

## What is this? ##
This module allows you to check your project for API keys.

## Quick Guide ##
The module is based on the following structure:

    files = ['...']
    probability = 6
    locator = APIKL(files, probability)
    locator.find_keys()

***files*** is for files you want to check *(blank to check the current folder)*\
***probability*** defines level of keys to show *(from 1 to 10, 5 is default)*

----------


### Using ###

Using the library is as simple and convenient as possible:

First, import everything from the library (use the `from `...` import *` construct).

Examples of all operations:

Finding keys in *files_to_check*  `find_keys(files_to_check: list)` \
If *files_to_check* is blank, it will check for keys in _locator.files_to_check_ which is defined in constructor

    files = ['path/to/file1', 'path/to/file2']
    locator.find_keys(files)



----------


## Developer ##
My site: https://github.com/VitalyKalinsky