#!/usr/bin/env python
#Life is short, use python!

import sys

import asmpattern     as pattern
import asmclosure     as closure
import asminstruction as inst
import asmlabel       as lbl
import hextobin

lineno_base = 0xC000000

def parse(code):
	code = pattern.delete(code, pattern.comments)
	code = lbl.parse(code)
	if not code:
		return ""

	matchdict = pattern.match(code, pattern.op);
	codehex, codelen = inst.asmdict[matchdict['OP']](matchdict['CODE'])
	lbl.lineno += codelen
	return codehex

def compile(fin, fout):
	lbl.lineno = lineno_base
	for line in fin:
		hexcode = parse(line)
	lbl.passno = 1
	lbl.lineno = lineno_base
	fin.seek(0,0)
	fout.write('memory_initialization_radix=16;\n')
	fout.write('memory_initialization_vector=\n')
	init = True
	for line in fin:
		hexcode = parse(line)
		if hexcode:
			if not init: fout.write( ',\n' )
			fout.write( hexcode )
			init = False
	fout.write( ';\n' )

def main(argv):
	if len(argv) < 2:
		print('Arguments error!\n')
		sys.exit(-1)

	with open(argv[0], "r") as fin:
		with open(argv[1], "w") as fout:
			compile(fin, fout)

	if len(argv) == 3:
		hextobin.main(argv[1:])


if __name__ == '__main__':
	main(sys.argv[1:])
	