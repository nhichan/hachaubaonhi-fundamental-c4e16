inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

#creat
inventory['pocket'] = [ 'seashell', 'strange berry', 'lint']

#remove
inventory['backpack'].remove('dagger')

#add more
inventory['gold']=50+500
for key,value in inventory.items():
    print(key,value)
