#!/usr/bin/env python
#Life is short, use python!

import sys
import deasmclosure
import struct

def parse(code,currentLine):
	intCode = int(code,16)
	op = intCode >> 26
	return deasmclosure.opDict[op](intCode,currentLine)

def compile(instList):
	asmCode = []
	for i in range(len(instList)):
		currentLine = i
		asmCode.append(parse(instList[i],i))
	final = addLableToAsm(asmCode)
	print final 
	return final

def compileCoe(fin,fout):
	asmCode = []
	lines = fin.readlines()
	instList = [x[0:8] for x in lines if x[0] != 'm']
	compile(instList)

def addLableToAsm(asmCode):
	finalAsm = []
	for i in range(len(asmCode)):
		if i in deasmclosure.lableList:
			finalAsm.append("Lable%x:"%i)
		finalAsm.append("\t"+asmCode[i])
	return "\n".join(finalAsm)

def main(argv):
	if len(argv) < 2:
		print('Arguments error!\n')
		sys.exit(-1)

	with open(argv[0], "r") as fin:
		with open(argv[1], "w") as fout:
			compileCoe(fin, fout)

	if len(argv) == 3:
		hextobin.main(argv[1:])

def compileFile(fileIn,fileOut):
	with open(fileIn, "r") as fin:
		with open(fileOut, "w") as fout:
			compileCoe(fin, fout)

if __name__ == '__main__':
	main(sys.argv[1:])
