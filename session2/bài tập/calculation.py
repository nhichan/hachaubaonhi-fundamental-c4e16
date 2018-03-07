weight=int(input('nhap so can nang cua ban(kg): '))
he=int(input('nhap chieu cao (cm): '))
hei=he/100
bmi=weight/(hei**2)
print('chi so BMI cua ban la: ',bmi)
if bmi<16:
    print('Severely underweight')
elif bmi<18.5:
    print('underweight')
elif bmi<25:
    print('normal')
elif bmi<30:
    print('overweight')
else:
    print('obese')
