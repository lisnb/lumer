#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Email:  lixipeng.ict@hotmail.com
# @Date:   2015-12-04 18:39:10
# @Last Modified by:   LiSnB
# @Last Modified time: 2015-12-04 19:11:22
from django.db import models

import json
from datetime import datetime, timedelta
# Create your models here.

class Plan(models.Model):
    """The plan"""
    PLAN_CHOICES = (
        (1, u'套餐1'),
        (2, u'套餐2'),
        (3, u'套餐3'),
        (4, u'套餐4'),
        (5, u'套餐5'),
        (6, u'套餐6'),
        (7, u'套餐7'),
    )
    plan_set = models.CharField(max_length=1, choices = PLAN_CHOICES)
    name = models.CharField(max_length=60)
    duration = models.DurationField(default = timedelta(28))
    weekdays = models.CharField(max_length = 100)
    def setweekdays(self, x):
        self.weekdays = json.dumps(x)
    def getweekdays(self):
        return json.loads(self.weekdays)