def read_file(file_name):
    f = open(file_name, 'r')
    for line in f:
        print("line: "+line, end="")
        print("len : ", len(line))


file = "sample1.py"
read_file(file)
