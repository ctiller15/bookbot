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