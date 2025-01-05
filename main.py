def count_words(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> dict:
    counter = {}
    text = text.lower()
    for c in text:
        if c.isalpha():
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

    return counter

def main():
    file_name = "books/frankenstein.txt"
    with open(file_name) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_counts = count_characters(file_contents)
        print(f"--- Begin report of {file_name} ---")
        print(f"{word_count} words found in the document\n")
        for k, v in sorted(char_counts.items(), key=lambda item: item[1], reverse=True):
            print(f"The '{k}' character was found {v} times")
        print("--- End report ---")

main()