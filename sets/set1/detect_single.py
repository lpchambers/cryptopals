#!/usr/bin/python3
import challenge4

with open('4.txt') as f:
	text = f.read()

lines = text.splitlines()

scores = []
for line in lines:
	d = challenge4.get_printable_xor_score_hex(line)
	if d:
#		print(d)
		scores += [(value[0], value[1], key) for key, value in d.items()]

import pprint
#pprint.pprint(lines)

pprint.pprint(sorted(scores))
