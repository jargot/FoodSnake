# -*- coding: utf-8 -*-

from anki import *
from parser import parse_book, extract_flavors

ingredients_list = parse_book()
print extract_flavors(ingredients_list, 'BOLD')


