#!/usr/bin/env python3

from collections import Counter

with open('input') as fh:
    data = fh.read()

def load_data(data):
    template_str, rules_str = data.split('\n\n')
    template = template_str.strip()
    rules = {k: v for (k, _, v) in (x.split() for x in rules_str.strip().split('\n'))}
    return template, rules

template, rules = load_data(data)
print(template)
print(rules)

#molecule = template
#for _ in range(10):
#    molecule = polymerize(molecule, rules)#

#counts = Counter(molecule).values()
#part_1 = max(counts) - min(counts)
#print('part_1 =', part_1)

"""
Part 2

Let's not build a string trillions long.
Instead, count frequencies of shingled monomer pairs.
"""

def make_shingle_freqs(molecule):
    return Counter(''.join(pair) for pair in zip(molecule, molecule[1:]))

def make_shingle_rules(insertionrules):
    return {k: (k[0] + v, v + k[1]) for k, v in insertionrules.items()}

def shingle_step(shingle_freqs, shingle_rules):
    c = Counter()
    for s, f in shingle_freqs.items():
        for snew in shingle_rules[s]:
            c[snew] += f
    return c

def shingle_monomer_freqs(shingle_freqs):
    monomer_counts = Counter()
    for k, v in shingle_freqs.items():
        for monomer in k:
            monomer_counts[monomer] += v
    return {k: sum(divmod(v, 2)) for k, v in monomer_counts.items()}

shingle_freqs = make_shingle_freqs(template)
print(shingle_freqs)
shingle_rules = make_shingle_rules(rules)

for _ in range(40):
    shingle_freqs = shingle_step(shingle_freqs, shingle_rules)

monomer_freqs = shingle_monomer_freqs(shingle_freqs)
counts = monomer_freqs.values()
part_2 = max(counts) - min(counts)
print('part_2 = ', part_2)