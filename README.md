# parse-wiktionary-html
Starter code for parsing Wiktionary pages -- intended to be used as a starting point when parsing Wiktionary pages. Follows parsing of DOM as of 24 October 2018.

This is a set of 2 simple python functions for parsing a Wiktionary page. 

request_wiktionary_tree(word) -- take word as input and request page from Wiktionary; return None if not found, otherwise return the page DOM tree

parse_wiktionary_tree(tree) -- take tree returned by request_wiktionary_tree and parse, printing out selected elements (edit/adapt as desired).

Sample usage:

```
tree = request_wiktionary_tree('agriculture')
parse_wiktionary_tree(tree)
```

```Out: (['Noun'],[['The art or science of cultivating the ground, including the harvesting of crops, and the rearing and management of livestock']],[])```

```
tree = request_wiktionary_tree('precipitation')
parse_wiktionary_tree(tree)
```

```
Out: (

['Noun'],
[['Any or all of the forms of water particles , whether liquid or solid , that fall from the atmosphere e.g., rain , hail ,
snow or sleet . It is a major class of hydrometeor , but it is distinguished from cloud , fog , dew , rime , frost , etc., in
that it must fall. It is distinguished from cloud and virga in that it must reach the ground.',
   'A hurried headlong fall .',
   'A reaction that leads to the formation of a heavier solid in a lighter liquid ; the precipitate so formed at the bottom of
   the container.',
   'Unwise or rash rapidity ; sudden haste .']],
[['Noun Synonyms', 'See also , Thesaurus:hydrometeor'],
['Noun Derived terms', 'aptaprecipitation, aptoprecipitation, coprecipitation, immunoprecipitation, microprecipitation,
nanoprecipitation, postprecipitation, precipitation hardening, precipitation reaction, reprecipitation']])
```

```
tree = request_wiktionary_tree('hide')
parse_wiktionary_tree(tree)
```

```
Out: 
(['Verb', 'Noun'],
 [['To put something in a place where it will be harder to discover or out of sight .',
   'To put oneself in a place where one will be harder to find or out of sight. 2013 May-June, William E. Conner , “ An
   Acoustic Arms Race ”, in American Scientist , volume 101, number 3, page 206-7: Nonetheless, some insect prey take
   advantage of clutter by hiding in it. Earless ghost swift moths become “invisible” to echolocating bats by forming mating
   clusters close less than half a meter above vegetation and effectively blending into the clutter of echoes that the bat
   receives from the leaves and stems around them.'],
  ['',
   'The skin of an animal .',
   'The human skin.',
   "One's own life or personal safety , especially when in peril .",
   'A covered structure from which hunters, birdwatchers, etc can observe animals without scaring them.',
   'A covered structure to which a pet animal can retreat, as is recommended for snakes .']],
 [['Verb Derived terms',
   "hide and seek,  / , hide-and-seek, hideaway, hideout, , , hide out, hide one's light under a bushel, hider, one can run
   but one can't hide"],
  ['Noun Derived terms',
   "cowhide, damn your hide, have someone's hide, rawhide, tan someone's hide"],
  ['Noun Hyponyms',
   '( ¼ hide, ) , See,  , virgate, ( ⅛ hide, ) , See,  , oxgang, ( 1, /, 16,  hide, ) , nook, farundel']])
