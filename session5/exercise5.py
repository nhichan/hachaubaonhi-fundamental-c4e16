prices={
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

stock={
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}


for key,value in prices.items():
    for key1,value1 in stock.items():
        if key==key1:
            print(key)
            print('price:',value)
            print('stock:',value1)

total=0
for key,value in prices.items():
    for key1,value1 in stock.items():
        if key==key1:
            total+=value*value1
print('the money I would make if you sold all of food: ',int(total))
