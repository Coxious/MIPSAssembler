
//Life is short, use python!

//	lui $ra, 0x3000;
//	jr $ra;

	add	$zero,$zero,$zero;
	add	$zero,$zero,$zero;
	lui	$v1,0xffff;
	addi	$v1,$zero,-256;
	addi	$s4,$zero,0x3f;
	lui	$t0,0x8000;
	add	$a0,$v1,$v1;
	addi	$v0,$zero,1;
	nor	$at,$zero,$zero;
	add	$t2,$at,$zero;
	addi	$a3,$zero,3;
	nor	$a3,$a3,$a3;
	addi	$a2,$zero,0x7FFF;
	add	$s1,$zero,$zero;
	addi	$a1,$zero,0x2AB;
	sw	$a1,0($v1);
	addi	$s2,$zero,2;
	sw	$zero,4($v1);
	lw	$a1,0($v1);
	add	$a1,$a1,$a1;
	add	$a1,$a1,$a1;
	sw	$a1,0($v1);
	sw	$a2,4($v1);
	lui	$t5,0xffff;

loc_00000060:
	lw	$a1,0($v1);
	add	$a1,$a1,$a1;
	add	$a1,$a1,$a1;
	sw	$a1,0($v1);
	lw	$a1,0($v1);
	and	$t3,$a1,$t0;
	addi	$t5,$t5,1;
	beq     $t3,$t0,loc_000000d4;

loc_00000080:
	lw	$a1,0($v1);
	addi	$s2,$zero,24;
	and	$t3,$a1,$s2;
	beqz    $t3,loc_000000a4;
	beq     $t3,$s2,loc_000000bc;
	addi	$s2,$zero,8;
	beq     $t3,$s2,loc_000000c8;
	sw	$t1,0($a0);
	j       loc_00000060;
		
loc_000000a4:
	beq     $t2,$at,loc_000000ac;
	j       loc_000000b4;
		
loc_000000ac:
	nor	$t2,$zero,$zero;
	add	$t2,$t2,$t2;
		
loc_000000b4:
	sw	$t2,0($a0);
	j       loc_00000060;
		
loc_000000bc:
	lw	$t1,672($s1);
	sw	$t1,0($a0);
	j       loc_00000060;
		
loc_000000c8:
	lw	$t1,608($s1);
	sw	$t1,0($a0);
	j       loc_00000060;
	
loc_000000d4:
	lui	$t5,0xffff;
	add	$t2,$t2,$t2;
	or	$t2,$t2,$v0;
	addi	$s1,$s1,4;
	and	$s1,$s1,$s4;
	addi	$t1,$t1,1;
	beq     $t1,$at,loc_000000f4;
	j       loc_000000f8;
		
loc_000000f4:
	addi	$t1,$t1,5;
		
loc_000000f8:
	lw	$a1,0($v1);
	add	$t3,$a1,$a1;
	add	$t3,$t3,$t3;
	sw	$t3,0($v1);
	sw	$a2,4($v1);
		
loc_0000010c:
	lw	$a1,0($v1);
	and	$t3,$a1,$t0;
	beq     $t3,$t0,loc_0000010c;
	j       loc_00000080;
