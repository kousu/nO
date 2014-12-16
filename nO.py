#!/usr/bin/python
"""
catherine: no no no no no
catherine: no No no
catherine: No No No
catherine: how do i write a program so i can have all the character differences for no no no
"""

# one solution: itertools.combinations(itertools.combinations(("N", "n")), itertools.combinations(("O, "o"))) then chained to give three at a time
# two solution: write a function that takes a string, finds all the alpha chars, and walks the bitstrings gives the 2**(# alpha char) dif

import sys
from itertools import product
import argparse

def scream(word, count=3):
	word = [(letter.lower(), letter.upper()) for letter in word] #find all pairs of upper/lowercase of letters in the word
	crazy = product(*word) #all the ways of writing 'word'
	crazy = [str.join("", word) for word in crazy]    #pump the generator and flatten the letters back, since we want to reuse it
	many = product(*([crazy]*count)) #pick out 'count' crazed words
	many = [str.join(" ", shout) for shout in many] #ditto, but instead we're flattening words->sentence instead of letters->word
	return many


if __name__ == '__main__':
	args = argparse.ArgumentParser(epilog="Scream and shout alllll the times")
	args.add_argument("word", nargs="?", default='no', help="what word to shout")
	args.add_argument("count", nargs="?", default=3, type=int, help="and how many times to shout it") 
	args = args.parse_args()
	for shout in scream(args.word, args.count):
		print(shout)
	
