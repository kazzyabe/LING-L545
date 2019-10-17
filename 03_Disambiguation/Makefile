all:
	cat UD_Portuguese-GSD/pt_gsd-ud-train.conllu | python conllu-perceptron-tagger/tagger.py -t pt-ud.dat
	cat UD_Portuguese-GSD/pt_gsd-ud-test.conllu | python conllu-perceptron-tagger/tagger.py pt-ud.dat > pt-ud-test.out
	python evaluation_script/conll17_ud_eval.py --verbose UD_Portuguese-GSD/pt_gsd-ud-test.conllu pt-ud-test.out