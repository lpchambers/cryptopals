#!/usr/bin/python3
"""
Do problem 4 with some more rigor around operating with bytes
"""

import string
from collections import defaultdict
bytes_string_printable = string.printable.encode('ascii')

english_char_freq = {'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 'u': 0.02758, 'v': 0.00978, 'w': 0.0236,  'x': 0.0015, 'y': 0.01974, 'z': 0.00074}

def _check_type(obj, expected_type):
	if type(obj) is not expected_type:
		raise ValueError("Got type {}, expected type {}", (type(obj), expected_type))

"""
Converts a hexstr to a bytestring <class 'bytes'>
"""
def hex2bytes(hexstr):
	return bytes([int(hexstr[i:i+2], 16) for i in range(0, len(hexstr), 2)])

def bytes2hex(bytestr):
	return "".join(["{:02x}".format(byte) for byte in bytestr])

def string2bytes(string, encoding=None):
	if encoding is None:
		return string.encode()
	else:
		return string.encode(encoding)


def bytes2string(bytestr, encoding=None):
	if encoding is None:
		return bytestr.decode()
	else:
		return bytestr.decode(encoding)


"""
Takes 2 byte strings of the same length and returns the XOR of the 2
"""
def xor(s1, s2):
	_check_type(s1, bytes)
	_check_type(s2, bytes)
	if len(s1) != len(s2):
		raise ValueError("Error: Strings should have the same length", (s1, s2, len(s1), len(s2)))

	return bytes([c1 ^ c2 for c1, c2 in zip(s1, s2)])


"""
XOR every char in a bytestring with a single char
@param: bytestr - a byte string
@param: char - the int in range [0-255] for the xor
"""
def single_char_xor(bytestr, char):
	return xor(len(bytestr) * bytes([char]), bytestr)

"""
In repeating-key XOR, you'll sequentially apply each byte of the key, then loop the key
"""
def repeating_char_xor(bytestr, repeat_bytestr):
	lb = len(bytestr)
	lr = len(repeat_bytestr)
	repeat_length_bytestr = (lb // lr) * repeat_bytestr + repeat_bytestr[:lb % lr]
	return xor(bytestr, repeat_length_bytestr)


def string_is_printable(bytestr):
	for char in bytestr:
		if char not in bytes_string_printable:
			return False
	return True


"""
Takes a bytestring as argument and returns a dictionary with key: xor-char and value xored-bytestring for each key that returns a printable string.
"""
def find_printable_xor(bytestr):
	_check_type(bytestr, bytes)
	printable = {}
	for key in range(256):
		xor_str = single_char_xor(bytestr, key)
		if string_is_printable(xor_str):
			printable[key] = xor_str
	return printable


"""
Returns the character frequency of the bytestring as an absolute number
"""
def get_byte_freq_abs(bytestr):
	d = defaultdict(lambda: 0)
	for char in bytestr.lower():
		d[char] += 1
	return d

"""
Returns the character frequency of the bytestring as a percentage
"""
def get_byte_freq_percent(bytestr):
	d_abs = get_byte_freq_abs(bytestr)
	l = len(bytestr)
	d_per = {char: num/l for char, num in d_abs.items()}
	return d_per

"""
Gets the score
"""
def get_char_freq_score(bytestr):
	byte_freq_percent = get_byte_freq_percent(bytestr)
	char_freq_percent = {chr(byte): value for byte, value in byte_freq_percent.items()}
	score = 0
	for char in english_char_freq:
		score += abs(english_char_freq[char] - char_freq_percent.get(char, 0))
	return score


"""
Returns the scores of all printable xor
"""
def get_printable_xor_score(bytestr):
	printable = find_printable_xor(bytestr)
	for char in printable:
		xor_str = printable[char]
		score = get_char_freq_score(xor_str)
		printable[char] = (score, xor_str)
	return printable


def get_printable_xor_score_hex(hexstr):
	return get_printable_xor_score(hex2bytes(hexstr))
