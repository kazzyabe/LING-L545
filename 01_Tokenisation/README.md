## Segmenter
1. segmenter.py: implements sengmenter in the slide
  * output in segmented.txt
2. nltksegmenter.py: used nltk segmenter
  * output nltksegmented.txt
## Tokenizer
1. dictionary_extractor.py: extract surface forms from tree bank (need to run unix command:sort|uniq)
  * extracted to Dictionary.txt
  * post processed version is extracted to Dictionary_uniq.txt
2. ground_truth_extractor.py: extract ground truth from the tree bank
  * extracted to ground_truth.txt
3. maxmatch.py: implementation of maxmatch
  * it's run maxmatch on test.conllu
  * result is extracted to mm_result.txt
4. maxmatch_evaluation.py: use wer to evaluate mm_result.txt
  * output: print the mean wer score in percentage = 8.404337568058088%
  
# Data
  * test.txt : extracted test sentences from test.conllu using test_extractor.py
  * train.txt : extracted train sentences from train.conllu using test_extractor.py
  * UD_Japanese-GSD-master

# WER
  * wer.py: implementation of wer calculatino