#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:10:51 2018

@author: mariutzica
"""

import requests
from lxml import html

def parse_wiktionary_tree(tree):
    
    all_elem = tree.xpath('//div[@class="mw-parser-output"]/*')
    lang_tag = ''
    language = ''
    pos = []
    for a in all_elem:
        # set language tag
        if a.tag in ['h2','h3','h4','h5','h6'] and lang_tag == '':
            lang_tag = a.tag
        if a.tag == lang_tag:
            language = a.xpath('./span[@class="mw-headline"]/text()')[0]
            if (language != 'English'):
                break
        if a.tag in ['h2','h3','h4','h5','h6']:
            tabs = int(a.tag[-1]) - int(lang_tag[-1])
            category = a.xpath('./span[@class="mw-headline"]/text()')[0]
            print('\t'*tabs,category)
            if category in ['Noun','Verb','Adjective','Adverb'] and not category in pos:
                pos.append(category)
                print(' '.join(a.xpath('./following-sibling::ol[1]/li//text()')))
            if category in ['Synonyms']:
                print(' '.join(a.xpath('./following-sibling::*[1]/li//text()')))
            if category in ['Derived terms']:
                print(' '.join(a.xpath('./following-sibling::*[1]/descendant::li//text()')))
    return pos
    

def request_wiktionary_tree(word):  
    base_wiki_url = 'https://en.wiktionary.org/wiki/'
    wiki_url = base_wiki_url + word
    try:
        page=requests.get(wiki_url)
        tree = html.fromstring(page.content)
    except:
        return None
    return tree