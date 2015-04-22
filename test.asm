start:
	addi $1, $0, 1;
	add $2, $1, $1;
	add $3, $1, $2;
	add $4, $3, $2;
	add $5, $4, $3;
	sub $5, $4, $1;

	addi $6, $0, 0x100;
	sw $5, 0($6);
	lw $7, 0($6);

	lui $8, 0xAAAA;
	srl $9, $8, 16;
	ori $10, $0, 0xFFFF;
	and $11, $10, $9;
	or $12, $10, $9;
	andi $13, $10, 0x3333;
	xor $14, $8, $9;
	xor $14, $8, $9;

	add $15, $0, $0;
	addi $16, $0, -1;
loop:
	addi $15, $15, 0x77;
	slt $17, $15, $16;
	sltu $18, $15, $16;
	beq $17, $0, forever;
	bne $17, $0, loop;

forever:
	j forever;


