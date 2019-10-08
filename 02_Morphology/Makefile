all:
	hfst-lexc chv.lexc -o chv.lexc.hfst
	hfst-twolc chv.twol -o chv.twol.hfst
	hfst-compose-intersect -1 chv.lexc.hfst -2 chv.twol.hfst -o chv.gen.hfst

ava:
	hfst-lexc ava.lexc -o ava.lexc.hfst

fin:
	hfst-lexc fin.lexc -o fin.lexc.hfst