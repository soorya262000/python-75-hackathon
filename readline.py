import linecache
fname=input("enter the name of the file")
line_no=int(input("enter the line number"))
print("line ",line_no," ",linecache.getline(fname,line_no))
