rabbits = [0,1]

for i in range(4):
    rabbit_all = rabbits[-1]+rabbits[-2]
    rabbits.append(rabbit_all)

rabbits=rabbits[2:]

for j in range(4):
    print('Month {}: {} pair(s) of rabbit'.format(j,rabbits[j]))
