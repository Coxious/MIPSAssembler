
#Life is short, use python!

import sys
import binascii
import struct

def compile(fin, fout):
	for line in fin:
		if line:
			if line[0:7] != 'memory_':
				data=binascii.unhexlify(line[0:8])
				code1,code2=struct.unpack(">2H", data)
				fout.write( struct.pack("<2H", code1, code2) )


def main(argv):
	if len(argv) != 2:
		print('Arguments error!\n')
		sys.exit(-1)

	with open(argv[0], "r") as fin:
		with open(argv[1], "wb") as fout:
			compile(fin, fout)

if __name__ == '__main__':
	main(sys.argv[1:])
