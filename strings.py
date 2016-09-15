name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mail, mails = list(),list()
count = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
       continue
    mail = line.split()
    mails.append(mail[1])
for item in mails:
    count[item] = count.get(item,0) + 1
biggest = 0
for key,value in count.items():
    if value > biggest:
	biggest = value 
	val = key
print val,biggest
