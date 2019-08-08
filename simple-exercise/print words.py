page_width=80
words=input('what words do you want to print:')
words_width=int(len(words))
printing_width=words_width+6
front=(page_width-printing_width)//2

print(' '*front,'+','-'*printing_width,'+')
print(' '*front,'|',' '*(words_width+6),'|')
print(' '*front,'|',' '*2,words,' '*2,'|')
print(' '*front,'|',' '*(words_width+6),'|')
print(' '*front,'+','-'*printing_width,'+')
