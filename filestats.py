import os
def fsize(filename):
    finfo=os.stat(filename)
    print("the size of the file in bytes   :",finfo.st_size)
def fstats(filename):
    f=open(filename,'r')
    l=f.readlines()
    print("NO OF LINES IN THE FILE  :",len(l))
    word_count=0
    letter_count=0
    for line in l:
        word_list=line.split()
        word_count=word_count+len(word_list)
        for word in word_list:
            letter_count=letter_count+len(word)
    print("the no of word in the file  :",word_count)
    print("the no of letters in the file :",letter_count)
fname=input("enter the file name")
fsize(fname)
fstats(fname)

