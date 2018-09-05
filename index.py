# -*- coding: utf-8 -*-
import ebooklib
from ebooklib import epub

from bs4 import BeautifulSoup
from bs4.element import Tag

book = epub.read_epub('FlavorBible.epub')

book_items_gen = book.get_items()
book_html_gen = book.get_items_of_type(9) # somehow 9 is EpubHtml

# Takes an element and test to see if it is a heading or not
#  def findIngredientHeading(el):
#      if ingredient.

# TODO: Generalize to all chap3
#  for x in book_html_gen:
#      html = book_html_gen.next()
#      if "chap-3" in html.get_name():
#          soup = BeautifulSoup(html.get_content(), 'html.parser')
#          ingredient = soup.find("p", class_="h")
#          print ingredient.get_text()

#          # TODO: Get bold, CAPS BOLD, and *CAPS BOLD ingredients
#          ingredient = ingredient.findNext()
#          while ingredient.findNext()['class'][0] != 'h' :
#              print ingredient
#              ingredient = ingredient.findNext()
#          print ingredient
#          ingredient = ingredient.findNext()
#          print "asd", ingredient

#          break


def jump_to_first_ingredient_header(localSoup):
    ingredient = soup.find("p", class_="h")
    return ingredient

def is_ingredient_header(curr_el):
    if curr_el['class'][0] != 'h':
        return False
    return True

def jump_to_next_ingredient_header(curr_el):
    if len(curr_el.contents) > 3:
        # TODO: Handle this, but for now, SKIP
        #  print "====================== MULTIPLE DETECTED"
        None
    curr_el = curr_el.findNext()
    while is_ingredient_header(curr_el) is False:
        curr_el = curr_el.findNext()
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
        # TODO handle normal
        # TODO handle bold
        # TODO handle BOLD
        # TODO handle *BOLD
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
            #  print cursor
        cursor = cursor.findNext()
        #  print single_flavors

def parse_flavor_affinities(ingredient_header):
    print "TODO: Flavor affinities"
    #  return

for x in book_html_gen:
    html = book_html_gen.next()
    if "chap-3" in html.get_name():
        soup = BeautifulSoup(html.get_content(), 'html.parser')
        ingredientHeader = jump_to_first_ingredient_header(soup)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
        #  print ingredientHeader 
        #  single_flavors = parse_single_flavors(ingredientHeader)
        #  print single_flavors
        #  flavor_affinities = parse_flavor_affinities(ingredientHeader)
        ingredients_list = {}
        while ingredientHeader:
            ingredientHeader = jump_to_next_ingredient_header(ingredientHeader)
            print ingredientHeader.get_text()
            ingredients_list[ingredientHeader.get_text()] = { 'single_flavors': parse_single_flavors(ingredientHeader) }
            #  ingredients_list.append({ 'name': ingredientHeader.get_text(), 'single_flavors': parse_single_flavors(ingredientHeader)})
            # TODO: Parse "Flavor Affinities"
            # TODO ...

print 'KEYS', ingredients_list.keys()
