# coding:utf-8

while True:
    height = raw_input('身長(m)?:')
    if len(height) == 0:
        break
    height = float(height)
    weight = float(raw_input('体重(kg)?:'))
    bmi = weight / pow(height, 2)

    print('BMI値は%0.1fです。' % bmi)
    if bmi < 18.5:
        print('痩せすぎだよ.')
    elif 18.5 <= bmi < 25.0:
        print('標準体型だよ.')
    elif 25.0 <= bmi < 30.0:
        print('太り気味だよ.')
    else:
        print('痩せないとやばいよ.')
