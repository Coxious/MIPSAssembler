#Life is short, use python!

import re

op       = re.compile(r'\s*(?P<OP>[0-9a-hA-H]{2}])'
                      r'\s*(?P<CODE>.*)')

def match(code, pattern):
	patternmatch = pattern.match(code)

	if not patternmatch:
		return {}

	matchdict = patternmatch.groupdict()
	print(matchdict)
	return matchdict

def compile(fin, fout):
	for line in fin:
		while True:
			matchdict = match(line, op)
			if matchdict:
				hexcode = matchdict['OP']
				fout.write( hexcode )
				line = matchdict['CODE']
			else:
				break;

def main(argv):
	if len(argv) != 2:
		print('Arguments error!\n')
		sys.exit(-1)

	with open(argv[0], "r") as fin:
		with open(argv[1], "w") as fout:
			compile(fin, fout)

if __name__ == '__main__':
	main(sys.argv[1:])
	