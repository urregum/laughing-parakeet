#!/usr/bin/python3
'''
    Find occurences of keywords and their location in a logfile.

    Test copilot driven code for a simple system shell script
    intended to simulate a triage tool. Use simple command line
    processing for a single target file.
'''
import sys
import os
import unittest
from typing import Optional


class TestMyFile(unittest.TestCase):
    '''
    Unit tests to validate search term cases.

    Tests split into checking a file with no matches,
    and cases with one or more matches. 
    '''
    def setUp(self):
        self.lterms = ["Error", "Warning", "Critical"]

    def test_healthy(self):
        '''
        Verify that we can handle a test file with no 
        occurrences of target words.
        '''
        print("\nHealthy test:")
        tdict = count_words_in_file("./test/healthy_log", self.lterms)
        if tdict is not None:
            self.assertTrue( all(t['count'] == 0 for t in tdict.values()))
        else:
            self.assertIsNotNone(tdict)

    def test_unhealthy(self):
        '''
        Check cases where target words are found.
        '''
        print("\nUnhealthy test:")
        # Check for matching < all terms early.
        tdict = count_words_in_file("./test/head_only_log", self.lterms)
        if tdict is not None:
            self.assertTrue(any(t['count'] > 0 for t in tdict.values()))
        else:
            self.assertIsNotNone(tdict)

        # Check for matching < all terms late.
        tdict = count_words_in_file("./test/tail_only_log", self.lterms)
        if tdict is not None:
            self.assertTrue(any(t['count'] == 0 for t in tdict.values()))
        else:
            self.assertIsNotNone(tdict)

        # Check for matching all passed terms.
        tdict = count_words_in_file("./test/varied_terms_log", self.lterms)
        if tdict is not None:
            self.assertTrue(all(t['count'] > 0 for t in tdict.values()))
        else:
            self.assertIsNotNone(tdict)

    def tearDown(self):
        pass

def count_words_in_file(file_path, words) -> Optional[dict]:
    '''
        Count specific words in file.

        Open path passed from command line, and count the number of times
        all keywords passed occur in said file (case sensitive)
        Print all occurences and line numbers once counting is done.
    '''
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return None

    word_counts = {word: {'count': 0, 'lines': []} for word in words}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            for word in words:
                if word in line:
                    word_counts[word]['count'] += 1
                    word_counts[word]['lines'].append(line_number)

    for word, data in word_counts.items():
        print(f"{word}: {data['count']} occurrences on lines {data['lines']}")

    return word_counts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    target_file = sys.argv[1]
    search_words = ["Error", "Warning", "Critical"]

    count_words_in_file(target_file, search_words)
