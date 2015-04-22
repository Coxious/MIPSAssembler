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
