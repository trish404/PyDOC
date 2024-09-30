import argparse
import os

# Function to count words in the file
def count_words(file_path: str) -> int:
    """
    Count the total number of words in the given text file.

    Parameters:
        file_path (str): The path to the input text file.

    Returns:
        int: The total number of words in the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        return len(text.split())

# Function to count characters in the file
def count_chars(file_path: str) -> int:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        return len(text)

# Function to count lines in the file
def count_lines(file_path: str) -> int:
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)

# Function to find the frequency of a specific word in the file
def find_word(file_path: str, word: str) -> int:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        return text.lower().split().count(word.lower())

# Function to replace a word in the file and save the new file
def replace_word(file_path: str, old_word: str, new_word: str) -> None:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    new_text = text.replace(old_word, new_word)
    new_file_path = f"updated_{os.path.basename(file_path)}"
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(new_text)
    print(f'"{old_word}" was replaced with "{new_word}" and saved to {new_file_path}')

# Argument parser setup
def main():
    parser = argparse.ArgumentParser(description="Process text files with various operations")
    parser.add_argument('-f', '--file', type=str, required=True, help="The path to the input text file")
    parser.add_argument('-wc', '--word-count', action='store_true', help="Display the total word count")
    parser.add_argument('-cc', '--char-count', action='store_true', help="Display the total character count")
    parser.add_argument('-lc', '--line-count', action='store_true', help="Display the total line count")
    parser.add_argument('-find', type=str, help="Find a specific word in the text file")
    parser.add_argument('-r', nargs=2, metavar=('old_word', 'new_word'), help="Replace a word in the text file with another word")

    args = parser.parse_args()

    if args.word_count:
        print(f"Word Count: {count_words(args.file)}")

    if args.char_count:
        print(f"Character Count: {count_chars(args.file)}")

    if args.line_count:
        print(f"Line Count: {count_lines(args.file)}")

    if args.find:
        word_count = find_word(args.file, args.find)
        print(f'The word "{args.find}" occurs {word_count} times.')

    if args.r:
        replace_word(args.file, args.r[0], args.r[1])

# Running the main function
if __name__ == "__main__":
    main()
