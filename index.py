# -*- coding: utf-8 -*-

from anki import *
from parser import parse_book, extract_flavors

ingredients_list = parse_book()

#  def debug_write_ingredients_list(ingredients_list):
#      with open('debug.log', 'w') as debug_file:
#          for ingredient in ingredients_list:
#              debug_file.write(ingredient.encode('utf8') + ' ')

#  debug_write_ingredients_list(ingredients_list)
    


STAR_BOLD_flavors = extract_flavors(ingredients_list, '*BOLD')
BOLD_flavors = extract_flavors(ingredients_list, 'BOLD')

generate_flavor_cards(BOLD_flavors, 'BOLD')
generate_flavor_cards(STAR_BOLD_flavors, '*BOLD')
