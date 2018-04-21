data_path = '/Users/genepatricks.rible/Desktop/Compilation.txt'
with open(data_path, 'r', encoding='ISO-8859-1') as f:
    lines = f.read().split('\n')
n = ['aa\ta', 'b\tbb', 'ccc', 'ddd\td', 'dddl', 'yyyyy']
lines_1 = reversed(sorted(lines, key=len))
for i in sorted(lines, key=len):
    # print(i)
    print(i, file=open("output.txt", "a"))
