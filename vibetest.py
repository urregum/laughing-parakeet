#!/usr/bin/python3
import sys
import os

def count_words_in_file(file_path, words):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    word_counts = {word: {'count': 0, 'lines': []} for word in words}

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            for word in words:
                if word in line:
                    word_counts[word]['count'] += 1
                    word_counts[word]['lines'].append(line_number)

    for word, data in word_counts.items():
        print(f"{word}: {data['count']} occurrences on lines {data['lines']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    target_file = sys.argv[1]
    search_words = ["Error", "Warning", "Critical"]
 
    count_words_in_file(target_file, search_words)
