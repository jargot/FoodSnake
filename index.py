# -*- coding: utf-8 -*-

from anki import *
from parser import parse_book, extract_flavors

ingredients_list = parse_book()

BOLD_flavors = extract_flavors(ingredients_list, 'BOLD')

generate_flavor_cards(BOLD_flavors)


