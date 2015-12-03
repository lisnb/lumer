#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2015-12-03 20:33:43
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-12-03 21:17:05

import random
import string

def generate_customer(cnt):
    i = 0
    names = string.uppercase+string.digits
    while i<cnt:
        i+=1
        name = u'吉{}{}'.format(random.choice(string.uppercase), ''.join(random.sample(names, 4)))
        yield (name, random.randint(1, 3))



def generate_plan(cnt):
    customers = list(generate_customer(cnt))
    customers.sort(key=lambda x:-x[1])
    # print customers
    weekdays = [[] for x in range(6)]
    # print customers
    print
    for i, customer in enumerate(customers):
        print u'%2d 车牌： %s, 套餐：%s'%(i, customer[0], customer[1])
    print
    for customer in customers:
        if customer[1] == 3:
            weekdays[0].append(customer)
            weekdays[2].append(customer)
            weekdays[4].append(customer)
        elif customer[1] == 2:
            least_day = (0, 3)
            least_cars = len(weekdays[0])+len(weekdays[3])
            w_25 = len(weekdays[1])+len(weekdays[4])
            if w_25 < least_cars:
                least_day = (1, 4)
                least_cars = w_25
            w_36 = len(weekdays[2])+len(weekdays[5])
            if w_36 < least_cars:
                least_day = (2, 5)
                least_cars = w_36
            weekdays[least_day[0]].append(customer)
            weekdays[least_day[1]].append(customer)
        else:
            least_day = weekdays.index(min(weekdays, key=lambda x:len(x)))
            weekdays[least_day].append(customer)
    print
    for i, weekday in enumerate(weekdays):
        print u'周 %s, 洗车：%s辆'%(i, len(weekday))
        for customer in weekday:
            print u'车牌： %s, 套餐：%s'%customer
        print



if __name__ == '__main__':
    # for card in generate_customer(10):
        # print card
    generate_plan(20)
