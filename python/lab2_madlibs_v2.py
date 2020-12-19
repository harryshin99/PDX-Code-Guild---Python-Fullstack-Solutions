"""
Creator: Harry Shin
Date: 15 Dec 2020
"""
import random

noun_list = input("Please enter three nouns separated by commas: ")
# adj_list = input("Please enter three adjectives separated by commas: ")
# verb_list = input("Please enter two verbs separated by commas: ")

snl = noun_list.split(', ')
# sal = adj_list.split(', ')
# svl = verb_list.split(', ')

print(snl)

# print(f'''
# No animal must ever live in a {random.choice(snl)}, or sleep in
# a {random.choice(snl)}, or wear clothes, or drink {random.choice(snl)}, or
# smoke tobacco, or touch money, or engage in
# trade. The habits of Man are {random.choice(sal)}. And, above
# all, no animal must ever {random.choice(svl)} over his own
# kind. Weak or {random.choice(sal)}, clever or {random.choice(sal)}, we are all
# brothers. No animal must ever {random.choice(svl)} any other
# animal. All animals are equal.
# ''')