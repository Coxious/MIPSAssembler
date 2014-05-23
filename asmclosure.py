
#Life is short, use python!

import asmpattern

def decorator(F):
	def new_F(code):
		codebin, codelen = F(code)
		return "%08x" % (codebin), codelen
	return new_F

def Itype(pattern, op, splitfunc):
	inst = op<<26
	@decorator
	def write(code):
		matchdict = asmpattern.match(code, pattern)
		rs, rt, imm = splitfunc(matchdict)
		return (inst + (rs<<21) + (rt<<16) + imm), 1

	return write

def Rtype(pattern, op, funct, splitfunc):
	inst = (op<<26) + funct
	@decorator
	def write(code):
		matchdict = asmpattern.match(code, pattern)
		rs, rt, rd, shamt = splitfunc(matchdict)
		return (inst + (rs<<21) + (rt<<16) + (rd<<11) + (shamt<<6)), 1

	return write

def Jtype(pattern, op, splitfunc):
	inst = op<<26
	@decorator
	def write(code):
		matchdict = asmpattern.match(code, pattern)
		imm = splitfunc(matchdict)
		return (inst + imm), 1

	return write

def Ftype():
	pass;
