# Coding Challenge - WC

## Description

This is my version of the [Coding Challenges wc Tool](https://codingchallenges.fyi/challenges/challenge-wc)

Libraries Used: Click (CLI)

## Setup

Python version used: 3.9.16

1. Clone repository
    ```
     git clone https://github.com/syuen23/cc-wc.git
    ```
2. CD into cc-wc
    ```
    cd cc-wc
    ```
3. Make a virtual environment and activate
    ```
    python3 -m venv .venv
    ```
    ```
    . .venv/bin/activate
    ```
4. Install Click
    ```
    pip install click
    ```

## Features

This tool provides the ability to get the word count, byte count, line count, or character count from stdin or a file(s).

Command-line arguments:

1. word count: `-w` or `--words`
2. byte count: `-c` or `--bytes`
3. line count: `-l` or `--lines`
4. character count: `-m` or `--characters`

## How to use

For reading from one or more files, run command:

```
python ccwc.py <options> <files>
```

For reading from stdin, run command:

```
cat <filename> | python ccwc.py <options>
```

> **_NOTE:_** If no options are included, the byte, word, and line count will be output.

## Output

For a single file or stdin, the output is ordered as follows:

`line count -> word count -> byte count -> char count -> filename`

> **_NOTE:_** With stdin, no filename is output

For multiple files, the output is multiple lines:

`line count -> word count -> byte count -> char count -> file1`

`line count -> word count -> byte count -> char count -> file2`

`...`
