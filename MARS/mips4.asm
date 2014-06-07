or $at,$0,$0;

loop:

addi $at, $at, 1;
addi $at, $at, -1;
addi $at, $at, 1;
addi $at, $at, -1;
addi $at, $at, 1;
addi $at, $at, -1;
addi $at, $at, 1;
addi $at, $at, -1;
addi $at, $at, 1;
addi $at, $at, -1;
addi $at, $at, 1;
addi $at, $at, -1;
addi $at, $at, 1;
addi $at, $at, -1;
addi $at, $at, 1;
addi $at, $at, -1;

sw $at, 0( $0 );

j loop;