bacteria = int(input('how many bacterias out there? '))
time = int(input('how much time in minute will we wait? '))

exponent = time//2
duplicate_time = 2**exponent
duplicate_bacteria = bacteria*duplicate_time

print('after',time,'minutes, we would have',duplicate_bacteria,'bacterias')
