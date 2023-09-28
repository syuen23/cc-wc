import click
import sys


def get_data(file_data):
    """ Returns the number of bytes, characters, lines, and words in a file

    Parameters:
        file_data (file): file object to read from

    Retruns:
        tuple: number of bytes, characters, lines, and words in file

    Raises:
        None

    """
    byte_count = char_count = line_count = word_count = 0
    for line in file_data:
        byte_count += len(line)
        char_count += len(line.decode("utf-8"))
        line_count += 1
        word_count += len(line.split())

    return byte_count, char_count, line_count, word_count


# setup command line flag arguments
@click.command()
@click.argument("files", nargs=-1, type=click.Path(exists=True))
@click.option(
    "-c",
    "--bytes",
    "count_bytes",  # global boolean variable to show whether or not this flag was included
    is_flag=True,
    help="The number of bytes in each input file is written to standard output",
)
@click.option(
    "-l",
    "--lines",
    "count_lines",
    is_flag=True,
    help="The number of lines in each input file is written to standard output",
)
@click.option(
    "-w",
    "--words",
    "count_words",
    is_flag=True,
    help="The number of words in each input file is written to standard output",
)
@click.option(
    "-m",
    "--characters",
    "count_chars",
    is_flag=True,
    help="The number of characters in each input file is written to standard output"
)


def word_count(files, count_bytes, count_lines, count_words, count_chars):
    """ Reads command line arguments and prints number of bytes, characters, lines, or words based on flags and files input

    Parameters:
        files (list): list of files to read from
        count_bytes (bool): whether or not to count bytes
        count_lines (bool): whether or not to count lines
        count_words (bool): whether or not to count words
        count_chars (bool): whether or not to count characters

    Returns:
        None

    Raises:
        None

    """

    # if no flags, default action is to give count of bytes, lines, and words
    if count_chars:
        pass
    elif not (count_bytes or count_lines or count_words):
        count_bytes = count_lines = count_words = True

    # if no files, default action is to read from stdin
    if not files:
        files = ["-"]

    counts = ""
    for filename in files:
        if filename == "-":
            filename = ""
            data = sys.stdin.buffer
            result = get_data(data)
        else:
            with open(filename, "rb") as file_data:
                result = get_data(file_data)

        byte_count, char_count, word_count, line_count = result

        if count_lines:
            counts += f"{line_count}\t"
        if count_words:
            counts += f"{word_count}\t"
        if count_bytes:
            counts += f"{byte_count}\t"
        if count_chars:
            counts += f"{char_count} "

        counts += f"{click.format_filename(filename)}\n"

    counts.strip()  # remove last newline
    click.echo(counts)


if __name__ == "__main__":
    word_count()
