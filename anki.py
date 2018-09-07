# -*- coding: utf-8 -*-

# TODO: Rename all the vars, it's silly
def generate_flavor_cards(flavors, filename):
    with open('cards/' + filename + '.csv', 'w') as the_file:
        for flavor in flavors:
            string = flavor + '\t' + ('<br>'.join(flavors[flavor])).title() + '\n'
            the_file.write(string.encode('utf8'))
        #  the_file.write('Hello\n')
