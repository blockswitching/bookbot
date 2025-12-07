# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a simple command-line tool that analyzes a text file (such as a book) and reports:

Total number of words

Frequency of each alphabetical character (sorted from most common to least)

The project consists of two main files:

main.py — handles command-line input, reads the file, and displays results

stats.py — contains helper functions for counting words and characters

Features

Counts total words in a text file

Counts occurrences of every character (case-insensitive)

Sorts characters by frequency in descending order

Displays only alphabetical characters in the result

Project Structure
bookbot/
│
├── main.py        # The main program that prints results
├── stats.py       # Helper functions (word count, char count, sorting)
└── README.md      # Project documentation

Usage

Run the program from the terminal:

python3 main.py <path_to_text_file>


Example:

python3 main.py books/frankenstein.txt


If you do not provide exactly one argument, the program prints:

Usage: python3 main.py <path_to_book>

How It Works
main.py

Reads the file path from command-line arguments

Loads the text

Calls functions from stats.py

Prints word count

Prints character frequencies (only letters)

stats.py

Contains three main functions:

get_num_words(text)
Splits the text into words and returns how many exist.

count_characters(text)
Counts each character (converted to lowercase).

sort_characters(count)
Builds a list of { "char": x, "num": y } and sorts it by frequency.

Example Output
============ BOOKBOT ============
Analyzing book found at books/sample.txt...
----------- Word Count ----------
Found 54231 total words
--------- Character Count -------
e: 42412
t: 30551
a: 27735
o: 27118
...
============= END ===============

Requirements

Python 3.x

A plain text file to analyze