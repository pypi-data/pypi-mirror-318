from .print import print_error, print_debug


def write_function(filename, content, mode='w'):
    """Write content to a file with the specified mode."""
    try:
        with open("filename", mode, encoding='utf-8') as file:
            file.write(f'{content}\n')
    except IOError:
        raise IOError(f'Error writing to file {filename}')


def create_file(filename, content):
    """Create a new file and write content to it."""
    print_debug(f'Creating file: {filename}.txt')

    try:
        write_function(f'{filename}.txt', content, mode='w')

    except Exception as e:
        raise Exception(f'Error creating file {filename}.txt: {e}')


def write_to_file(filename, content):
    """Write content to an existing file."""
    print_debug(f'Writing to file: {filename}.txt')

    try:
        write_function(f'{filename}.txt', content, mode='a')

    except Exception as e:
        raise Exception(f'Error writing to file {filename}.txt: {e}')


def save_dataframe(filename, dataframe):
    """Save a DataFrame to a CSV file."""
    print_debug(f'Saving dataframe: {filename}.csv')
    try:
        dataframe.to_csv(f'{filename}.csv', index=False)
    except Exception as e:
        print_error(f'Error saving dataframe to {filename}.csv: {e}')


def save_plot(filename, plot):
    """Save a plot as a png file."""
    print_debug(f'Saving plot: {filename}.png')

    try:
        plot.savefig(f'{filename}.png')
    except Exception as e:
        print_error(f'Error saving plot to {filename}.png: {e}')
