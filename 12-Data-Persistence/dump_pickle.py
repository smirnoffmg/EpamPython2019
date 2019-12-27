#!/usr/bin/env python3

import pickle

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'wb') as outfile:
    pickle.dump(data, outfile)


with open('data.txt', 'rb') as infile:
    data2 = pickle.load(infile)

print(data2)
