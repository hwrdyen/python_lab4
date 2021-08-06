
fname = 'test_text_parsing.txt'
greetings = open(fname, 'r')

greeting_list = []

line = greetings.readline().replace("\n"," ")
print(line)

