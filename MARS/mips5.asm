j main;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;
add $zero,$zero,$zero;

//-----------------------------------------------------------------------------------
//                                Interrupt Entry
//-----------------------------------------------------------------------------------
interrupt_entry:

or $k1,$zero,$zero;
lui $k1,0xc000;

lw $k0, 0($k1);
add $s7,$s7,$s7;
add $s7,$s7,$s7;
add $s7,$s7,$s7;
add $s7,$s7,$s7;
add $s7,$s7,$s7;
add $s7,$s7,$s7;
add $s7,$s7,$s7;
add $s7,$s7,$s7;
add $s7,$s7,$k0;

add $k0,$zero,$zero;
lui $k0, 0xefff;
addi $k0, $k0, 0x7fff;
addi $k0, $k0, 0x7ff1;

sw $s7,0($k0);
sw $s7,0($gp);
addi $gp,$gp,4;

addi $k0, $zero, 64;

sw $k0, 1($k1);

eret ;


//-----------------------------------------------------------------------------------
//                             Main Entry Of MIPS Program
//-----------------------------------------------------------------------------------
main:

or $gp, $zero, $zero;
lui $gp,0xb000;

add $at,$zero,$zero;
addi $at, $zero, 64;

or $s0,$zero,$zero;
lui $s0,0xc000;
sw $at, 1($s0);

nor $at, $zero, $zero;

lui $s0,0xb800;
sw $at, 0(s0);

or $s0,$zero,$zero;
lui $s0,0x30fc;
addi $s0,$s0,0x7000;
addi $s0,$s0,0x4000;

or $t9, $0, $0;
lui $t9,0x30f8;

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
