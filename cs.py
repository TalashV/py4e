#пробелы лучше, чем таб

x = 20
if x < 2 :
    print ('small')
elif x < 10:
    print ('medium')
else :
    print ('Large')
print("all done")

#try / except
a = 'hello bob'
try:
    b = int(a)
except:
    b = -1

print("first", a)
