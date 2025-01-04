# contigion-utils
A library for utility functions common across Contigion projects

[![Pylint](https://github.com/Contigion/utils/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/Contigion/utils/actions/workflows/pylint.yml)
[![Publish to PyPI](https://github.com/Contigion/utils/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/Contigion/utils/actions/workflows/publish.yml)
[![Python Version](https://img.shields.io/pypi/pyversions/contigion-utils?style=flat)](https://pypi.org/project/contigion-utils/)
[![PyPi Version](https://img.shields.io/pypi/v/contigion-utils?style=flat)](https://pypi.org/project/contigion-utils/)

## Installation
To install the library, simply run:

`
pip install contigion-utils
`

## Usage
You can use any of the functions in this library by importing them. For example:


``` python
from contigion_utils.log import create_file, save_dataframe
from contigion_utils.print import print_info, print_error

# Create a new file
create_file('test_file', 'This is a test.')

# Print a message
print_info('This is an informational message.')

# Save a DataFrame
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
save_dataframe('data_file', df)
```

## Modules
The library has the following modules with these functions
### `contigion_utils.log`
  - create_file (filename, content)
  - write_to_file (filename, content)
  - save_dataframe (filename, dataframe)
  - save_plot (filename, plot)

### `contigion_utils.print`
  - print_info (text)
  - print_debug (text)
  - print_warning (text)
  - print_success (text)
  - print_error (text)


## Contributions

Contributions are welcome! 
If you find any issues or want to improve the library, feel free to submit an issue.
