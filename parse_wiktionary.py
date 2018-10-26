#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:10:51 2018

@author: mariutzica
"""

import requests
from lxml import html
import re

#parse Wiktionary tree for sections in the English category, as well as defs
# synonyms, derived terms, etc
# edit here to get desired sections
def parse_wiktionary_tree(tree):
    
    header_opt = ['h'+str(i) for i in range(2,7)]
    pos_labels = ['Noun','Verb','Adjective','Adverb']
    rel_term_opt = ['Synonyms', 'Derived terms', 'Hyponyms']
    
    #grab sibling elements from DOM at the content level
    all_elem = tree.xpath('//div[@class="mw-parser-output"]/*')
    lang_tag = ''
    language = ''
    pos = []
    defs = []
    nyms = []
    cur_pos = ''

    for a in all_elem:
        # set language tag
        if a.tag in header_opt and lang_tag == '':
            lang_tag = a.tag

	# if at language tag, and section is English then proceed, else exit (English parsing only)
        if a.tag == lang_tag:
            language = a.xpath('./span[@class="mw-headline"]/text()')[0]
            if (language != 'English'):
                break

        # when a heading tag is reached, determine the category, print its name in a tabbed hierarchy, and, for select
        # sections, print content using nested text content *at the moment*
        if a.tag in header_opt:
            #tabs = int(a.tag[-1]) - int(lang_tag[-1])
            category = a.xpath('./span[@class="mw-headline"]/text()')[0]
            #print('\t'*tabs,category)
            if category in pos_labels and not category in pos:
                cur_pos = category
                pos.append(category)
                d = []
                entries = a.xpath('./following-sibling::ol[1]/li')
                for e in entries:
                    def_text = ' '.join(e.xpath('.//text()'))
                    usage_ex = e.xpath('./*[not(self::a)]')
                    for u in usage_ex:
                        def_text = def_text.replace(' '.join(u.xpath('.//text()')),'')
                    d.append(re.sub('\s+', ' ',def_text.strip()))
                defs.append(d)
            if category in rel_term_opt:
                nyms_text = ', '.join(a.\
                    xpath('./following-sibling::*[1]/descendant::li//text()'))\
                                      .replace('(,','(').replace('),',')')
                nyms.append([cur_pos + ' ' + category, nyms_text])
    return pos, defs, nyms
    

def request_wiktionary_tree(word):  
    base_wiki_url = 'https://en.wiktionary.org/wiki/'
    wiki_url = base_wiki_url + word
    try:
        page=requests.get(wiki_url)
        tree = html.fromstring(page.content)
    except:
        return None
    return tree
