# parse-wiktionary-html
Starter code for parsing Wiktionary pages -- intended to be used as a starting point when parsing Wiktionary pages. Follows parsing of DOM as of 24 October 2018.

This is a set of 2 simple python functions for parsing a Wiktionary page. 

request_wiktionary_tree(word) -- take word as input and request page from Wiktionary; return None if not found, otherwise return the page DOM tree

parse_wiktionary_tree(tree) -- take tree returned by request_wiktionary_tree and parse, printing out selected elements (edit/adapt as desired).
