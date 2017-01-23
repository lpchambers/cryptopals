#!/usr/bin/python3
import base64

def hexstr2bytes(hexstr):
	return bytes([int(hexstr[i:i+2], 16) for i in range(0, len(hexstr), 2)])


# Takes a hex string and converts to base64 bytestring
def hex2base64(hexstr):
	return base64.b64encode(hexstr2bytes(hexstr))


if __name__ == "__main__":
	import sys
	if len(sys.argv) < 2:
		print("require hexstring to convert")
		sys.exit(0)

	print(hex2base64(sys.argv[1]))
