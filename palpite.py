#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import sample

def palpite():
    palpite = sample(xrange(1, 61), 6)
    palpite.sort()

    return "%02d %02d %02d %02d %02d %02d" % (palpite[0], palpite[1], palpite[2], palpite[3], palpite[4], palpite[5]) 
