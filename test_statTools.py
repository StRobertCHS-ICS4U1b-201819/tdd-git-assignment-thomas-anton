"""
----------------------------------------------------------
Filename: test_tatTools.py
Purpose: tests the functions in statTools.py

Author: Maglietta.T

Created: 31/10/2018
----------------------------------------------------------
"""

import pytest
from statTools import *


test_list_1 = [1, 2, 3, 4]
test_list_2 = [1, 2, 3, 4, 5, 6]
test_list_3 = [1, 2, 3, 4, 5, 6, 7]
test_list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_list_5 = [1, 2, 3]
test_list_6 = [1, 2]
test_list_7 = [1]
test_empty_list = []
test_not_list = 'a'
test_str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# lower quartile tests


def test_lower_q_1():
    assert(lower_quartile(test_list_1) == 1.5)  # corner case -- LQ is the average of 2 numbers


def test_lower_q_2():
    assert(lower_quartile(test_list_2) == 2)  # general case -- returns item from index in list


def test_lower_q_3():
    assert (lower_quartile(test_list_3) == 2.5)  # corner case -- LQ is the average of 2 numbers


def test_lower_q_4():
    assert (lower_quartile(test_list_4) == 3)  # general case -- returns item from index in list


def test_lower_q_5():
    assert (lower_quartile(test_list_5) == 1.5)  # corner case -- list smaller than 4 items


def test_lower_q_6():
    assert (lower_quartile(test_list_6) == 1)  # corner case -- list smaller than 4 items


def test_lower_q_7():
    assert (lower_quartile(test_list_7) == 1)  # corner case -- list smaller than 4 items


def test_lower_q_empty_ls():  # unusual case --  empty list
    with pytest.raises(IndexError) as errmsg:
        lower_quartile(test_empty_list)
    assert ('index is out of range' == str(errmsg.value))


def test_lower_q_not_ls():  # unusual case -- not a list
    with pytest.raises(TypeError) as errmsg:
        lower_quartile(test_not_list)
    assert ('a list of integers was not provided' == str(errmsg.value))


def test_lower_q_str_ls():  # unusual case -- list of strings
    with pytest.raises(TypeError) as errmsg:
        lower_quartile(test_str_list)
    assert ('a list of integers was not provided' == str(errmsg.value))

# upper quartile tests


def test_upper_q_1():
    assert (upper_quartile(test_list_1) == 3.5)  # corner case -- LQ is the average of 2 numbers


def test_upper_q_2():
    assert (upper_quartile(test_list_2) == 5)  # general case -- returns item from index in list


def test_upper_q_3():
    assert (upper_quartile(test_list_3) == 5.5)  # corner case -- LQ is the average of 2 numbers


def test_upper_q_4():
    assert (upper_quartile(test_list_4) == 7)  # general case -- returns item from index in list


def test_upper_q_5():
    assert (upper_quartile(test_list_5) == 2.5)  # corner case -- LQ is the average of 2 numbers


def test_upper_q_6():
    assert (upper_quartile(test_list_6) == 2)  # corner case -- list smaller than 4 items


def test_upper_q_7():
    assert (upper_quartile(test_list_7) == 1)  # corner case -- list smaller than 4 items


def test_upper_q_empty_ls():  # unusual case -- empty list
    with pytest.raises(IndexError) as errmsg:
        upper_quartile(test_empty_list)
    assert ('index is out of range' == str(errmsg.value))


def test_upper_q_not_ls():  # unusual case -- not a list
    with pytest.raises(TypeError) as errmsg:
        upper_quartile(test_not_list)
    assert ('a list of integers was not provided' == str(errmsg.value))


def test_upper_q_str_ls():  # unusual case -- list of strings
    with pytest.raises(TypeError) as errmsg:
        upper_quartile(test_str_list)
    assert ('a list of integers was not provided' == str(errmsg.value))

# median tests


def test_median_1():
    assert (median(test_list_1) == 2.5)  # corner case -- median is the average of 2 numbers


def test_median_2():
    assert (median(test_list_3) == 4)  # general case -- returns item from index in list


def test_median_3():  # corner case -- list size is smaller than 2
    assert (median(test_list_7) == 1)
    
    
def test_median_empty_ls():  # unusual case -- empty list
    with pytest.raises(IndexError) as errmsg:
        median(test_empty_list)
    assert ('index is out of range' == str(errmsg.value))


def test_median_not_ls():  # unusual case -- not a list
    with pytest.raises(TypeError) as errmsg:
        median(test_not_list)
    assert ('a list of integers was not provided' == str(errmsg.value))


def test_median_str_ls():  # unusual case -- list of strings
    with pytest.raises(TypeError) as errmsg:
        median(test_str_list)
    assert ('a list of integers was not provided' == str(errmsg.value))

# mode tests, needs to use different lists


def test_mode_1():
    assert(mode([1, 1, 2]) == [1])  # general case -- has one mode


def test_mode_2():
    assert (mode([1, 1, 2, 2, 2]) == [2])  # general case -- has one mode


def test_mode_3():
    assert (mode([1]) == [1])  # general case -- has one mode


def test_mode_4():
    assert (mode([1, 1, 2, 2, 3]) == [1, 2])  # corner case has more than 1 mode


def test_mode_5():
    assert (mode([]) == [])  # corner case -- empty list has no mode


def test_mode_str_ls():
    assert (mode(['a', 'a', 'b']) == ['a'])  # list of strings can have mode


def test_mode_not_ls(): # unusual case -- not a list
    with pytest.raises(AttributeError) as errmsg:
        mode(1)
    assert ('Must input a list' == str(errmsg.value))


def test_mode_multi_type():  # unusual case -- needs to compare items of various data types
    with pytest.raises(TypeError) as errmsg:
        mode([1, 'a'])
    assert ('Must input a list that contains only 1 data type' == str(errmsg.value))
