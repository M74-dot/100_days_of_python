import math


def paint_can_calc(height, width, cover):
    no_of_cans = (height * width) / cover
    no_of_cans = math.ceil(no_of_cans)
    print(f'Total nummber of cans required are: {no_of_cans}')


test_h = int(input('Enter Height of Wall '))
test_w = int(input('Enter Width of Wall '))
coverage = 5
paint_can_calc(height=test_h, width=test_w, cover=coverage)