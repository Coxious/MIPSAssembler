
#Life is short, use python!

import re

import asmexception

comments = re.compile('//.*')

lbl      = re.compile(r'\s*((?P<LBL>\S+)\s*:)?'
                      r'\s*(?P<CODE>.*)')

op       = re.compile(r'\s*(?P<OP>\S+)'
                      r'\s*(?P<CODE>.*)')

opr0     = re.compile(r'\s*;'
                      r'\s*(?P<CODE>.*)')

opr1     = re.compile(r'\s*[$]?(?P<R0>\S+)\s*;'
                      r'\s*(?P<CODE>.*)')

opr2     = re.compile(r'\s*[$]?(?P<R0>\S+)\s*,'
                      r'\s*[$]?(?P<R1>\S+)\s*;'
                      r'\s*(?P<CODE>.*)')

opr3     = re.compile(r'\s*[$]?(?P<R0>\S+)\s*,'
                      r'\s*[$]?(?P<R1>\S+)\s*,'
                      r'\s*[$]?(?P<R2>\S+)\s*;'
                      r'\s*(?P<CODE>.*)')

opr3off  = re.compile(r'\s*[$]?(?P<R0>\S+)\s*,'
                      r'\s*(?P<R2>[^(]+)'
                      r'[(]\s*[$]?(?P<R1>\S+)\s*[)]\s*;'
                      r'\s*(?P<CODE>.*)')

def delete(code, pattern):
	m = pattern.search(code)
	if m:
		start = m.start()
		#print "start is",start
		code = code[:start]
	return code

def match(code, pattern):
	patternmatch = pattern.match(code)

	if not patternmatch:
		raise asmexception.AsmException

	matchdict = patternmatch.groupdict()
	print(matchdict)
	return matchdict
