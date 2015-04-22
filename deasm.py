#!/usr/bin/env python
#Life is short, use python!

import sys
import deasmclosure
import struct

opDict = {
	0x0	:lambda code,currentLine:(DecodeRtype(code,currentLine,'Rtype' )),
	0x08:lambda code,currentLine:(DecodeItype(code,currentLine,'addi'  )),
	0x09:lambda code,currentLine:(DecodeItype(code,currentLine,'addiu' )),
	0xc :lambda code,currentLine:(DecodeItype(code,currentLine,'andi'  )),
	0x1c:lambda code,currentLine:(DecodeRtype(code,currentLine,'clo'   )), 
	0x1c:lambda code,currentLine:(DecodeRtype(code,currentLine,'clz'   )), 
	 0xd:lambda code,currentLine:(DecodeItype(code,currentLine,'ori'   )), 
	 0xe:lambda code,currentLine:(DecodeItype(code,currentLine,'xori'  )), 
	 0xa:lambda code,currentLine:(DecodeItype(code,currentLine,'slti'  )), 
	 0xb:lambda code,currentLine:(DecodeItype(code,currentLine,'sltiu' )), 
	 0xf:lambda code,currentLine:(DecodeItype(code,currentLine,'lui'   )), 
	   4:lambda code,currentLine:(DecodeItype(code,currentLine,'beq'   )), 
	   4:lambda code,currentLine:(DecodeItype(code,currentLine,'beqz'  )), 
	   1:lambda code,currentLine:(DecodeItype(code,currentLine,'bgez'  )), 
	   1:lambda code,currentLine:(DecodeItype(code,currentLine,'bgezal')),
	   7:lambda code,currentLine:(DecodeItype(code,currentLine,'bgtz'  )), 
	   6:lambda code,currentLine:(DecodeItype(code,currentLine,'blez'  )), 
	   1:lambda code,currentLine:(DecodeItype(code,currentLine,'bgtzal')),
	   5:lambda code,currentLine:(DecodeItype(code,currentLine,'bne'   )), 
	   2:lambda code,currentLine:(DecodeJtype(code,currentLine,'j'     )), 
	   3:lambda code,currentLine:(DecodeJtype(code,currentLine,'jal'   )), 
	0x20:lambda code,currentLine:(DecodeItype(code,currentLine,'lb'    )), 
	0x25:lambda code,currentLine:(DecodeItype(code,currentLine,'lhu'   )), 
	0x23:lambda code,currentLine:(DecodeItype(code,currentLine,'lw'    )), 
	0x31:lambda code,currentLine:(DecodeItype(code,currentLine,'lwcl'  )), 
	0x22:lambda code,currentLine:(DecodeItype(code,currentLine,'lwl'   )), 
	0x26:lambda code,currentLine:(DecodeItype(code,currentLine,'lwr'   )), 
	0x30:lambda code,currentLine:(DecodeItype(code,currentLine,'ll'    )), 
	0x28:lambda code,currentLine:(DecodeItype(code,currentLine,'sb'    )), 
	0x29:lambda code,currentLine:(DecodeItype(code,currentLine,'sh'    )), 
	0x2b:lambda code,currentLine:(DecodeItype(code,currentLine,'sw'    )), 
	0x31:lambda code,currentLine:(DecodeItype(code,currentLine,'swcl'  )), 
	0x3d:lambda code,currentLine:(DecodeItype(code,currentLine,'sdcl'  )), 
	0x2a:lambda code,currentLine:(DecodeItype(code,currentLine,'swl'   )), 
	0x2e:lambda code,currentLine:(DecodeItype(code,currentLine,'swr'   )), 
	0x38:lambda code,currentLine:(DecodeItype(code,currentLine,'sc'    )), 
	0x10:lambda code,currentLine:(DecodeRtype(code,currentLine,'eret'  )), 
}

funcDict={
	(0,   0):'sll'   , 
	(0,   4):'sllv'  ,
	(0,   3):'sra'   ,
	(0,   7):'srav'  ,
	(0,   2):'srl'   ,
	(0,   6):'srlv'  ,
	(0,  32):'add'   ,
	(0,  33):'addu'  ,
	(0,  34):'sub'   ,
	(0,  35):'subu'  ,
	(0,  36):'and'   ,
	(0x1c,0x21):'clo',
	(0x1c,0x20):'clz',
	(0,  37):'or'    ,
	(0,  38):'xor'   ,
	(0,  39):'nor'   ,
	(0,  42):'slt'   ,
	(0,  43):'sltu'  ,
	(0,   8):'jr'    , 
	(0,   9):'jalr'  ,
	(0, 0xb):'movn'  ,
	(0, 0xa):'movz'  ,
	(0,  24):'eret'  
	}
    
regDict= {
	 0:"0",#"zero",
	 1:"1",#"at"  ,  
	 2:"2",#"v0"  ,  
	 3:"3",#"v1"  ,  
	 4:"4",#"a0"  ,  
	 5:"5",#"a1"  ,  
	 6:"6",#"a2"  ,  
	 7:"7",#"a3"  ,  
	 8:"8",#"t0"  ,  
	 9:"9",#"t1"  ,  
	10:"10",#"t2"  ,  
	11:"11",#"t3"  ,  
	12:"12",#"t4"  ,  
	13:"13",#"t5"  ,  
	14:"14",#"t6"  ,  
	15:"15",#"t7"  ,  
	16:"16",#"s0"  ,  
	17:"17",#"s1"  ,  
	18:"18",#"s2"  ,  
	19:"19",#"s3"  ,  
	20:"20",#"s4"  ,  
	21:"21",#"s5"  ,  
	22:"22",#"s6"  ,  
	23:"23",#"s7"  ,  
	24:"24",#"t8"  ,  
	25:"25",#"t9"  ,  
	26:"26",#"k0"  ,  
	27:"27",#"k1"  ,  
	28:"28",#"gp"  ,  
	29:"29",#"sp"  ,  
	30:"30",#"fp"  ,  
	31:"31",#"ra"    
}



global currentLine
lableList = []

def addLable(line):
	if line not in lableList:
		lableList.append(line)

def DecodeItype(code,currentLine,name):
	rs = (code >> 21) & 31
	rt = (code >> 16) & 31
	imme = code & 2**16-1
	if imme & 2**15 != 0:
		imme = -(2**16-imme)
	
	if name[0:2] == "sw" or name[0:2]=="lw":
		return "%s\t$%s,\t%d($%s);"%(name,regDict[rt],imme,regDict[rs])
	elif name == "lui":
		return "%s\t$%s,\t0x%x;"%(name,regDict[rt],imme)
	elif name[0]=='b' and name != 'break':
		target = currentLine+1+imme
		addLable(target)	
		return "%s\t%s,\t%s,\tLable%x;"%(name,regDict[rt],regDict[rs],target)
	else:
		return "%s\t$%s,\t$%s,\t0x%x;"%(name,regDict[rt],regDict[rs],imme)

def DecodeJtype(code,currentLine,name):
	target = code & 2 ** 26 -1
	if target not in lableList:
		lableList.append(target)
	return "%s\tLable%x;"%(name,target)

def DecodeRtype(code,currentLine,name):
	rs = (code >> 21) & 31
	rt = (code >> 16) & 31
	rd = (code >> 11) & 31
	shamt = (code >> 6) & 31
	func = code & 63
	op = code >> 26
	name = funcDict[(op,func)]
	if shamt != 0:
		return "%s\t$%s,\t$%s,\t%d;"%(name,regDict[rd],regDict[rt],shamt)
	else:
		return "%s\t$%s,\t$%s,\t$%s;"%(name,regDict[rd],regDict[rs],regDict[rt])

def convert(codeRaw):
	return codeRaw[2:4]+codeRaw[0:2]+codeRaw[6:8]+codeRaw[4:6]

def parse(code,currentLine):
	intCode = int(code,16)
	op = intCode >> 26
	return opDict[op](intCode,currentLine)

def compile(instList):
	asmCode = []
	for i in range(len(instList)):
		currentLine = i
		asmCode.append(parse(instList[i],i))
	final = addLableToAsm(asmCode)
	print final 
	return final

def compileBin(fin,fout):
	bincode = fin.read().encode('hex')
	global currentLine
	while len(bincode) > 0:
		instList.append(bincode[0:8])
		bincode = bincode[9:-1]
	compile(instList)

def compileCoe(fin,fout):
	asmCode = []
	lines = fin.readlines()
	instList = [x[0:8] for x in lines if x[0] != 'm']
	compile(instList)

def addLableToAsm(asmCode):
	finalAsm = []
	for i in range(len(asmCode)):
		if i in lableList:
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
