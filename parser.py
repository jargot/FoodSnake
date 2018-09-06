# -*- coding: utf-8 -*-

# TODO: Some things don't get parsed correctly, for instance: Shrimp lacks LEMON, Spinach lacks CHEESE
# TODO: AVOID keyword (!? in Sorrel for example)

import ebooklib
from ebooklib import epub

from bs4 import BeautifulSoup
from bs4.element import Tag

book = epub.read_epub('FlavorBible.epub')

book_items_gen = book.get_items()
book_html_gen = book.get_items_of_type(9) # somehow 9 is EpubHtml

def jump_to_first_ingredient_header(localSoup):
    ingredient = localSoup.find("p", class_="h")
    return ingredient

def is_ingredient_header(curr_el):
    if curr_el['class'][0] != 'h':
        return False
    return True

def jump_to_next_ingredient_header(curr_el):
    if len(curr_el.contents) > 3:
        # TODO: Handle this, but for now, SKIP
        #  print "====================== MULTIPLE DETECTED"
        # pass?
        None
    curr_el = curr_el.findNext()
    while is_ingredient_header(curr_el) is False:
        curr_el = curr_el.findNext()
        if curr_el is None:
            # Reached end of chapter
           return None 
    next_el = curr_el
    return next_el

#  <p class="h">SZECHUAN CUISINE <strong class="calibre1">(See also Chinese Cuisine)</strong></p>
#  <p class="bl1"><strong class="calibre1">Volume:</strong> loud</p>
#  <p class="bl1"><strong class="calibre1">Techniques:</strong> braise, pickle, roast, simmer, steam, stir-fry</p>
#  <p class="bl1">bamboo shoots</p>
#  <p class="bl1">beef</p>
#  <p class="bl1">cabbage, Chinese</p>
#  <p class="bl1">chicken</p>
#  <p class="bl1">chile peppers</p>
#  <p class="bl1">chili paste</p>
#  <p class="bl1">duck</p>
#  <p class="bl1">garlic</p>
#  <p class="bl1">ginger</p>
#  <p class="bl1">meats, smoked</p>
#  <p class="bl1">peanuts</p>
#  <p class="bl1"><strong class="calibre1">PORK</strong></p>
#  <p class="bl1">soy sauce</p>
#  <p class="bl1"><strong class="calibre1">*SZECHUAN PEPPER</strong></p>
#  <p class="bl1">tangerine peel, dried</p>
#  <p class="bl1">wine, rice</p>

def parse_single_flavors(ingredient_header):
    cursor = ingredient_header.findNext()
    single_flavors = { 'normal': [], 'bold': [], 'BOLD': [], '*BOLD': [] }
    while is_ingredient_header(cursor) is False:
        text = cursor.get_text()
        if cursor['class'][0] == 'bl1' and not isinstance(cursor.children.next(), Tag):
            single_flavors['normal'].append(text)
        elif cursor['class'][0] == 'calibre1':
            if cursor.get_text() == 'Flavor Affinities':
                # Stop parsing, we reached the end of the single flavors
                return single_flavors
            if cursor.get_text().isupper():
                if cursor.get_text().find("—".decode('utf8')) != -1:
                    pass
                elif cursor.get_text().find('*') != -1:
                    single_flavors['*BOLD'].append(text)
                else:
                    single_flavors['BOLD'].append(text)
            else:
                single_flavors['bold'].append(text)
        cursor = cursor.findNext()

def parse_flavor_affinities(ingredient_header):
    print "TODO: Flavor affinities"
    #  return


def parse_book():
    ingredients_list = {}
    for x in book_html_gen:
        html = book_html_gen.next()
        working_chapters = ["OEBPS/Text/FlavorBible_chap-3a.html", 'OEBPS/Text/FlavorBible_chap-3f.html', 'OEBPS/Text/FlavorBible_chap-3jkl.html', 'OEBPS/Text/FlavorBible_chap-3s.html']

        # NOT WORKING:
        #  OEBPS/Text/FlavorBible_chap-3c_split_000.html
        #  OEBPS/Text/FlavorBible_chap-3d.html
        #  OEBPS/Text/FlavorBible_chap-3h.html
        # "OEBPS/Text/FlavorBible_chap-3nop.html"

        for chapter in working_chapters:
            if chapter in html.get_name():
                soup = BeautifulSoup(html.get_content(), 'html.parser')
                ingredientHeader = jump_to_first_ingredient_header(soup)
                while ingredientHeader:
                    ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
                    if ingredientHeader is None:
                        break
                    ingredients_list[ingredientHeader.get_text()] = { 'single_flavors': parse_single_flavors(ingredientHeader) }
                # TODO: Parse "Flavor Affinities"
            # TODO: Parse general data (Volume, Weight ...), not present in every ingredient
    return ingredients_list

def extract_flavors(ingredients_list, flavor_type):
    flavors = {}
    for ingredient in ingredients_list:
        if ingredients_list[ingredient]['single_flavors'] is not None:
            if ingredients_list[ingredient]['single_flavors'][flavor_type]:
                flavors[ingredient] = ingredients_list[ingredient]['single_flavors'][flavor_type]
    return flavors


