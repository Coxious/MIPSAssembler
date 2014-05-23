
#Life is short, use python!

import asmpattern     as pattern
import asmclosure     as closure
import asmlabel       as lbl
import asmregister    as register

def r(k):
	return register.regdict[k]

asmdict = { 
	'sll'   :closure.Rtype(pattern.opr3   ,   0,   0,lambda m:(          0 , r(m['R1']) , r(m['R0']) , lbl.eval5(m['R2']))),
	'sllv'  :closure.Rtype(pattern.opr3   ,   0,   4,lambda m:( r(m['R2']) , r(m['R1']) , r(m['R0']) , 0                 )),
	'sra'   :closure.Rtype(pattern.opr3   ,   0,   3,lambda m:(          0 , r(m['R1']) , r(m['R0']) , lbl.eval5(m['R2']))),
	'srav'  :closure.Rtype(pattern.opr3   ,   0,   7,lambda m:( r(m['R2']) , r(m['R1']) , r(m['R0']) , 0                 )),
	'srl'   :closure.Rtype(pattern.opr3   ,   0,   2,lambda m:(          0 , r(m['R1']) , r(m['R0']) , lbl.eval5(m['R2']))),
	'srlv'  :closure.Rtype(pattern.opr3   ,   0,   6,lambda m:( r(m['R2']) , r(m['R1']) , r(m['R0']) , 0                 )),
	'add'   :closure.Rtype(pattern.opr3   ,   0,  32,lambda m:( r(m['R1']) , r(m['R2']) , r(m['R0']) , 0                 )),
	'addi'  :closure.Itype(pattern.opr3   ,   8,     lambda m:( r(m['R1']) , r(m['R0']) , lbl.eval16 (m['R2'])           )),
	'addu'  :closure.Rtype(pattern.opr3   ,   0,  33,lambda m:( r(m['R1']) , r(m['R2']) , r(m['R0']) , 0                 )),
	'addiu' :closure.Itype(pattern.opr3   ,   9,     lambda m:( r(m['R1']) , r(m['R0']) , lbl.eval16 (m['R2'])           )),
	'sub'   :closure.Rtype(pattern.opr3   ,   0,  34,lambda m:( r(m['R1']) , r(m['R2']) , r(m['R0']) , 0                 )),
	'subu'  :closure.Rtype(pattern.opr3   ,   0,  35,lambda m:( r(m['R1']) , r(m['R2']) , r(m['R0']) , 0                 )),
	'and'   :closure.Rtype(pattern.opr3   ,   0,  36,lambda m:( r(m['R1']) , r(m['R2']) , r(m['R0']) , 0                 )),
	'andi'  :closure.Itype(pattern.opr3   , 0xc,     lambda m:( r(m['R1']) , r(m['R0']) , lbl.eval16 (m['R2'])           )),
	'clo'   :closure.Rtype(pattern.opr2   ,0x1c,0x21,lambda m:( r(m['R1']) ,          0 , r(m['R0']) , 0                 )),
	'clz'   :closure.Rtype(pattern.opr2   ,0x1c,0x20,lambda m:( r(m['R1']) ,          0 , r(m['R0']) , 0                 )),
	'or'    :closure.Rtype(pattern.opr3   ,   0,  37,lambda m:( r(m['R1']) , r(m['R2']) , r(m['R0']) , 0                 )),
	'ori'   :closure.Itype(pattern.opr3   , 0xd,     lambda m:( r(m['R1']) , r(m['R0']) , lbl.eval16 (m['R2'])           )),
	'xor'   :closure.Rtype(pattern.opr3   ,   0,  38,lambda m:( r(m['R1']) , r(m['R2']) , r(m['R0']) , 0                 )),
	'xori'  :closure.Itype(pattern.opr3   , 0xe,     lambda m:( r(m['R1']) , r(m['R0']) , lbl.eval16 (m['R2'])           )),
	'nor'   :closure.Rtype(pattern.opr3   ,   0,  39,lambda m:( r(m['R1']) , r(m['R2']) , r(m['R0']) , 0                 )),
	'slt'   :closure.Rtype(pattern.opr3   ,   0,  42,lambda m:( r(m['R1']) , r(m['R2']) , r(m['R0']) , 0                 )),
	'sltu'  :closure.Rtype(pattern.opr3   ,   0,  43,lambda m:( r(m['R1']) , r(m['R2']) , r(m['R0']) , 0                 )),
	'slti'  :closure.Itype(pattern.opr3   , 0xa,     lambda m:( r(m['R1']) , r(m['R0']) , lbl.eval16(m['R2'])            )),
	'sltiu' :closure.Itype(pattern.opr3   , 0xb,     lambda m:( r(m['R1']) , r(m['R0']) , lbl.eval16(m['R2'])            )),
	'lui'   :closure.Itype(pattern.opr2   , 0xf,     lambda m:(          0 , r(m['R0']) , lbl.eval16(m['R1'])            )),
	'beq'   :closure.Itype(pattern.opr3   ,   4,     lambda m:( r(m['R0']) , r(m['R1']) , lbl.evaloff16(m['R2'])         )),
	'beqz'  :closure.Itype(pattern.opr2   ,   4,     lambda m:( r(m['R0']) ,          0 , lbl.evaloff16(m['R1'])         )),
	'bgez'  :closure.Itype(pattern.opr2   ,   1,     lambda m:( r(m['R0']) ,          1 , lbl.evaloff16(m['R1'])         )),
	'bgezal':closure.Itype(pattern.opr2   ,   1,     lambda m:( r(m['R0']) ,         17 , lbl.evaloff16(m['R1'])         )),
	'bgtz'  :closure.Itype(pattern.opr2   ,   7,     lambda m:( r(m['R0']) ,          0 , lbl.evaloff16(m['R1'])         )),
	'blez'  :closure.Itype(pattern.opr2   ,   6,     lambda m:( r(m['R0']) ,          0 , lbl.evaloff16(m['R1'])         )),
	'bgtzal':closure.Itype(pattern.opr2   ,   1,     lambda m:( r(m['R0']) ,         16 , lbl.evaloff16(m['R1'])         )),
	'bne'   :closure.Itype(pattern.opr3   ,   5,     lambda m:( r(m['R0']) , r(m['R1']) , lbl.evaloff16(m['R2'])         )),
	'jr'    :closure.Rtype(pattern.opr1   ,   0,   8,lambda m:( r(m['R0']) ,          0 ,          0 , 0                 )),
	'j'     :closure.Jtype(pattern.opr1   ,   2,     lambda m:( lbl.evaljmp26(m['R0'])                                   )),
	'jal'   :closure.Jtype(pattern.opr1   ,   3,     lambda m:( lbl.evaljmp26(m['R0'])                                   )),
	'jalr'  :closure.Rtype(pattern.opr2   ,   0,   9,lambda m:( r(m['R0']) ,          0 , r(m['R1']) , 0                 )),
	'lb'    :closure.Itype(pattern.opr2   ,0x20,     lambda m:(          0 , r(m['R0']) , lbl.evaloff16(m['R1'])         )),
	'lhu'   :closure.Itype(pattern.opr2   ,0x25,     lambda m:(          0 , r(m['R0']) , lbl.evaloff16(m['R1'])         )),
	'lw'    :closure.Itype(pattern.opr3off,0x23,     lambda m:( r(m['R1']) , r(m['R0']) , lbl.evaloff16(m['R2'])         )),
	'lwcl'  :closure.Itype(pattern.opr2   ,0x31,     lambda m:(          0 , r(m['R0']) , lbl.evaloff16(m['R1'])         )),
	'lwl'   :closure.Itype(pattern.opr2   ,0x22,     lambda m:(          0 , r(m['R0']) , lbl.evaloff16(m['R1'])         )),
	'lwr'   :closure.Itype(pattern.opr2   ,0x26,     lambda m:(          0 , r(m['R0']) , lbl.evaloff16(m['R1'])         )),
	'll'    :closure.Itype(pattern.opr2   ,0x30,     lambda m:(          0 , r(m['R0']) , lbl.evaloff16(m['R1'])         )),
	'sb'    :closure.Itype(pattern.opr2   ,0x28,     lambda m:(          0 , r(m['R0']) , lbl.evaloff16(m['R1'])         )),
	'sh'    :closure.Itype(pattern.opr2   ,0x29,     lambda m:(          0 , r(m['R0']) , lbl.evaloff16(m['R1'])         )),
	'sw'    :closure.Itype(pattern.opr3off,0x2b,     lambda m:( r(m['R1']) , r(m['R0']) , lbl.evaloff16(m['R2'])         )),
	'swcl'  :closure.Itype(pattern.opr2   ,0x31,     lambda m:(          0 , r(m['R0']) , lbl.evaloff16(m['R1'])         )),
	'sdcl'  :closure.Itype(pattern.opr2   ,0x3d,     lambda m:(          0 , r(m['R0']) , lbl.evaloff16(m['R1'])         )),
	'swl'   :closure.Itype(pattern.opr2   ,0x2a,     lambda m:(          0 , r(m['R0']) , lbl.evaloff16(m['R1'])         )),
	'swr'   :closure.Itype(pattern.opr2   ,0x2e,     lambda m:(          0 , r(m['R0']) , lbl.evaloff16(m['R1'])         )),
	'sc'    :closure.Itype(pattern.opr2   ,0x38,     lambda m:(          0 , r(m['R0']) , lbl.evaloff16(m['R1'])         )),
	'movn'  :closure.Rtype(pattern.opr3   ,   0, 0xb,lambda m:( r(m['R1']) , r(m['R2']) , r(m['R0']) , 0                 )),
	'movz'  :closure.Rtype(pattern.opr3   ,   0, 0xa,lambda m:( r(m['R1']) , r(m['R2']) , r(m['R0']) , 0                 ))
}
