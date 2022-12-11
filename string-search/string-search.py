#!/usr/bin/env python3
import argparse
import re
class StringEdit:
    def __init__(self,
                 search_string,
                 word_list):
        self.search_string = search_string
        self.word_list = word_list

    def perform_string_search(self):
        max_word = ''
        for word in self.word_list:
            regex_word = ''.join([f'{char}[a-z]*' for char in word])
            if re.search(regex_word, self.search_string) and \
               len(word) > len(max_word):
                   max_word = word
        if max_word:
            print(max_word)
        else:
            print("No word found based on the search string and word list.")

def process_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument('search_string',
                        help='The string to generate other strings from.')
    parser.add_argument('reqwords',
                        nargs='+',
                        help='A list of words to add to the words list')
    return parser.parse_args()

def main():
    args = process_parameters()
    string_edit = StringEdit(args.search_string, args.reqwords)
    string_edit.perform_string_search()

if __name__ == '__main__':
    main()
