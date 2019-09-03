grep '^[^aeiouAEIOU]' < wiki.words > conswords.txt
gsed 's/[aeiouAEIOU].*//g' < conswords.txt > consequence.txt
uniq -c < consequence.txt > seqcount.txt