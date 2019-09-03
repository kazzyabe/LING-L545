grep '[^aeiouAEIOU]$' < wiki.words | rev > fconswords.txt
gsed 's/[aeiouAEIOU].*//g' < fconswords.txt | rev > fconsequence.txt
uniq -c < consequence.txt > fseqcount.txt