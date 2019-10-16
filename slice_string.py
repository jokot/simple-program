

console = "XBOX 360 | $250 | New"

#1
name = console[0:console.index("|")-1]
print(name)
price = console[console.index("|")+1:]
price = price[1:price.index("|")]
print(price)
condition = console[console.index("|")+1:]
condition = condition[condition.index("|")+2:]
print(condition)

#2
print(console[:console.find("|")-1])
print(console[console.find("|")+2:console.find("|",console.find("|")+1)])
print(console[console.find("|",console.find("|")+1)+2:])

#3
#print(console.split(" | "))
list_console = console.split(" | ")
print(list_console[0])
print(list_console[1])
print(list_console[2])



def reverse(a):
    j=""
    for i in a:
        j = i + j
    return j

print(reverse(console))
print(console[::-1])


