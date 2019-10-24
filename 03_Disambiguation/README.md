Tagger is in https://github.com/kazzyabe/conllu-perceptron-tagger.git

# Added i-3 feature (POS and Word information for i-3rd word)
## Before adding features
```
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     96.26 |     96.26 |     96.26 |     96.26
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     96.26 |     96.26 |     96.26 |     96.26
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
```

## After adding i-3 feature
```
Metrics    | Precision |    Recall |  F1 Score | AligndAcc<br>
-----------+-----------+-----------+-----------+-----------<br>
Tokens     |    100.00 |    100.00 |    100.00 |<br>
Sentences  |    100.00 |    100.00 |    100.00 |<br>
Words      |    100.00 |    100.00 |    100.00 |<br>
UPOS       |     96.28 |     96.28 |     96.28 |     96.28<br>
XPOS       |    100.00 |    100.00 |    100.00 |    100.00<br>
Feats      |    100.00 |    100.00 |    100.00 |    100.00<br>
AllTags    |     96.28 |     96.28 |     96.28 |     96.28<br>
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00<br>
UAS        |    100.00 |    100.00 |    100.00 |    100.00<br>
LAS        |    100.00 |    100.00 |    100.00 |    100.00<br>
```