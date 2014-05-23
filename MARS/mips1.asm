ori $v0, $zero, 1
slt $at, $zero, $v0
beq $zero, $zero, lala
lw $at, 4($fp)
lala:
