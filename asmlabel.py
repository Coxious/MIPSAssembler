
#Life is short, use python!

import asmpattern     as pattern
import asmexception

lineno = 0
passno = 0
label  = dict()

def parse(code):

	if not code:
		return code

	matchdict = pattern.match(code, pattern.lbl);
	lbl = matchdict['LBL']
	code = matchdict['CODE']

	if not lbl:
		return code

	label[lbl] = lineno

	return parse(code)

def doeval(code):
	if passno == 0:
		return 0

	for lbl in label:
		code = code.replace(lbl, str(label[lbl]))

	return eval(code)

def eval5(code):
	return doeval(code) & 0x1f

def eval16(code):
	return doeval(code) & 0xffff

def evaloff(code):
	if passno == 0:
		return 0

	if code in label:
		target = label[code]
		offset = target - lineno - 1
	else:
		offset = doeval(code)

	print('offset: ' + str(offset))
	return offset

def evaloff16(code):
	return evaloff(code) & 0xffff

def evaljmp26(code):
	return doeval(code) & 0x3ffffff
