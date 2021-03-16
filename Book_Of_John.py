work_file = open("book of John text.txt", "r")
read_file = work_file.read()
work_file.close()
read_file = read_file.split()

lookup_words = ["Father", "God", "Christ", "Spirit", "spirit", "life", "man"]

dict = {}

for i in read_file:
    if i in lookup_words:
        count = read_file.count(i)
        dict[i] = count


for k in dict:
    print(k, ": ", dict[k])
