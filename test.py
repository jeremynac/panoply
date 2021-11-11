#!/usr/bin/python
from fast_autocomplete import AutoComplete
words = {'book': {}, 'burrito': {}, 'pizza': {}, 'pasta':{}}
autocomplete = AutoComplete(words=words)
autocomplete.search(word='b', max_cost=3, size=3)
autocomplete.search(word='bu', max_cost=3, size=3)
autocomplete.search(word='barrito', max_cost=3, size=3)
