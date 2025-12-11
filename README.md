Word Count Program

A simple Python-based Word Count tool that reads a text file, converts the content to lowercase, splits it into words, and counts how many times each word appears. This project demonstrates basic Python file handling, string operations, and dictionary usage.

Features

Reads text from a file (story.txt)

Converts all text to lowercase

Splits the content into individual words

Counts how many times each word appears

Displays results as a dictionary

Very beginner-friendly Python project

Shows the power of dictionaries with O(1) lookups

Files Included

word_count.py – Main Python script that performs the word counting

story.txt – A sample text file placed inside the data/ folder

env/ – (Optional) Python virtual environment for running the project

Project Structure
word_count_project/
│
├── env/                 # Virtual environment (optional)
├── data/
│   └── story.txt        # Input file for word counting
└── src/
    └── word_count.py    # Main program code

How to Run

Open a terminal or command prompt

Navigate to the project folder:

cd word_count_project/src


Make sure story.txt is inside the /data folder

Run the Python script:

python word_count.py


The program will print the dictionary containing word counts.

Example Output
Word Count Result:
{'hello': 2, 'world': 1, 'this': 1, 'is': 1, 'sample': 1}

Technologies Used

Python 3 – Core programming language

File Handling – Reading text files

String Methods – .lower(), .split()

Dictionary Operations – Counting words efficiently
