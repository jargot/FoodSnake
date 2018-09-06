# -*- coding: utf-8 -*-

# TODO: Rename all the vars, it's silly
def generate_flavor_cards(flavors):
    with open('cards/bold.csv', 'w') as the_file:
        for flavor in flavors:
            string = flavor + ';' + ('<br>'.join(flavors[flavor])).title() + '\n'
            print string
            the_file.write(string.encode('utf8'))
        #  the_file.write('Hello\n')
