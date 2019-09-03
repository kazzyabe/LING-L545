grep '[^aeiouAEIOU]$' < wiki.words | rev > fconswords.txt
gsed 's/[aeiouAEIOU].*//g' < fconswords.txt > fconsequence.txt
uniq -c < consequence.txt > fseqcount.txt