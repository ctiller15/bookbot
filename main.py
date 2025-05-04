from stats import count_characters, count_words

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_name = sys.argv[1]
    # file_name = "books/frankenstein.txt"
    with open(file_name) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_counts = count_characters(file_contents)
        print(f"--- Begin report of {file_name} ---")
        print(f"{word_count} words found in the document\n")
        for k, v in sorted(char_counts.items(), key=lambda item: item[1], reverse=True):
            print(f"{k}: {v}")
        print("--- End report ---")

main()