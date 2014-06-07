nor $at, $zero, $zero;

or $s0,$zero,$zero;
lui $s0,0x30fc;
addi $s0,$s0,0x7000;
addi $s0,$s0,0x4000;

or $t9, $0, $0;
lui $t9,0x30f8;

j next;

loop_set:

beq $t9,$s0,next;
sw $t9, 0($t9);
addi $t9,$t9,4;

j loop_set;

next:
or $t9, $0, $0;
lui $t9,0x30f8;

loop_inv:

beq $t9,$s0,next;
lw $t1, 0($t9);
//xor $t1,$t1,$at;
nor $t1,$t1,$zero;
sw $t1, 0($t9);
addi $t9,$t9,4;

j loop_inv;
