# Udpipe
```
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |    100.00 |    100.00 |    100.00 |    100.00
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |    100.00 |    100.00 |    100.00 |    100.00
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |     83.93 |     83.93 |     83.93 |     83.93
LAS        |     81.44 |     81.44 |     81.44 |     81.44
```

## Errors
minulle - pronoun: 
Gold: dependent of pupulle Noun 
Test: dependent of Varasin Verb
Both label is conj

sisarentyttärelleni - Noun
Gold: dependent of pupulle Noun 
Test: dependent of Varasin Verb
Both label is conj

pääsi - Verb
Gold: dependent of sisarentyttärelleni Noun
Test: dependent of Varasin Verb
Both label is acl:relcl

kaupunginteatterin - Noun
Gold: dependent of -musikaaliin Noun with nmod:poss
Test: dependent of Laulavat verb with nsubj

sadepisarat - Noun
Gold: dependent of -musikaaliin Noun with compound:nn
Test: dependent of lukemaan Verb with obj

-musikaaliin - Noun
Gold: dependent of liput Noun with nmod
Test: dependent of lukemaan Verb with obl
