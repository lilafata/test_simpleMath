##########################################################################################################
#
# DATE  :      01/29/2025
# AUTHOR:      Lila Fata
# FILE  :      test_simpleMath.py
# DESCRIPTION: This script file contains simple pytest fixtures and test functions:
#                  pytest -v test_simpleMath.py
#
# NOTE:
# 1) This program was executed using the IDLE Python 3.7 Shell on a Windows 10 laptop
# 2) Test was executed with following command:
#        pytest -v test_simpleMath.py > test_simpleMath_SAMPLEOutput.txt
# 3) Sample output 'test_simpleMath_SAMPLEOutput.txt' is included
#
##########################################################################################################

import pytest
import os
import math
import re


@pytest.fixture
def input1():
    input = 39
    return input
@pytest.fixture
def input2():
    input = 25
    return input
@pytest.fixture
def input3():
    input = 3
    return input
@pytest.fixture
def input4():
    input = 4
    return input


def test_factor_2(input2):
    assert input2 % 2 == 0

def test_factor_4(input2):
    assert input2 % 4 == 0
    
def test_factor_3(input1):
    assert input1 % 3 == 0

def test_factor_6(input1):
    assert input1 % 6 == 0

def test_prime_3(input3):

    isPrime = False
    cnt = 0
    for i in range(1, int(input3)+1):
        if input3 % i == 0:
            cnt=cnt+1
            if cnt > 2:
                isPrime = False
                break
    if input3 <= 1 or cnt > 2:
        assert False
    else:
        assert True

def test_prime_4(input4):

    isPrime = False
    cnt = 0
    for i in range(1, int(input4)+1):
        if input4 % i == 0:
            cnt=cnt+1
            if cnt > 2:
                isPrime = False
                break
    if input4 <= 1 or cnt > 2:
        assert False
    else:
        assert True
