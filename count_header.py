f = open("Escherichia_coli_str.fasta", "r+")

content = f.readlines()
counter = 0
for i in content:
    if i[0] == ">":
        counter += 1

print(counter)
f.close()

