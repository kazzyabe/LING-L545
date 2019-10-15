all:
	hfst-lexc chv.lexc -o chv.lexc.hfst
	hfst-twolc chv.twol -o chv.twol.hfst
	hfst-compose-intersect -1 chv.lexc.hfst -2 chv.twol.hfst -o chv.gen.hfst
	hfst-invert chv.gen.hfst -o chv.mor.hfst

ava:
	hfst-lexc ava.lexc -o ava.lexc.hfst

fin:
	hfst-lexc fin.lexc -o fin.lexc.hfst

mor:
	hfst-invert chv.gen.hfst | hfst-fst2strings -r 10

paradigm:
	cat noun-paradigm.txt | sed "s/^/у р а м /g"  | hfst-regexp2fst -j > uram.hfst 
	hfst-compose-intersect -2 chv.gen.hfst -1 uram.hfst | hfst-fst2strings 

Chuvash:
	hfst-substitute -i chv.lexc.hfst -o chv.lexc_guesser.hfst  -f '🂡:🂡' -T chv.stem.hfst
	hfst-compose-intersect -1 chv.lexc_guesser.hfst -2 chv.twol.hfst -o chv.gen_guesser.hfst
	echo "лайк<guess><n><pl><ins>" | hfst-lookup -qp chv.gen_guesser.hfst 
	hfst-regexp2fst chv.restrict.regex -o chv.restrict.hfst
	hfst-invert chv.gen_guesser.hfst | hfst-compose -1 - -2 chv.restrict.hfst -o chv.mor_guesser.hfst