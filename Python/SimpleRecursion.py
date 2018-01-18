#!/usr/bin/env python
"""
    File name: HojaDeTrabajo6.py
    Author: Jorge Quintero
    Date created: 11/06/2017
    Date last modified: 11/06/2017
    Python version: 3.6
"""


def multiply(num1, num2):
    """Sums a number by itself the number of times defined.

    :param num1: The number that is going to be multiplied.
    :param num2: The number that is gonna multiply the fist one.
    :return: The result of the multiplication betweeen the two numbers.
    """
    if num2 == 1:
        return num1
    return num1 + multiply(num1, num2 - 1)


def in_descending(n):
    """Displays in descend order from a given number to 0, in a 2 by 2 sequence.
    Ete no.

    :param n: The given number in which the function starts.
    :return: None, the function only displays the info.
    """
    if n < 0:
        return
    print(n, end=" ")
    in_descending(n-2)


def division(num1, num2):
    """Algorithm for recursive secession.

    :param num1: The dividend.
    :param num2: The divisor.
    :return: The division of the two parameters in integer.
    """
    if num2 > num1:
        return 0
    return division(num1 - num2, num2) + 1


def harmonic_sum(n):
    """Algorithm for recursive harmonic sum.

    :param n: The limit in which the recursion would stop.
    :return: The harmonic summary of n numbers, starting at n = 1, of 1 / n.
    """
    if n == 1:
        return 1
    return harmonic_sum(n - 1) + (1 / n)


def char_counting(msg, uchar):
    """Algorithm for recursive count of a certain character in a string.

    :param msg: The message of input to test with.
    :param ucarac: The character the function is gonna check.
    :return: The number of times the parameter ucarac appears in msg.
    """
    if not msg:
        return 0
    return (msg[0].lower() == uchar) + char_counting(msg[1:], uchar)


def count_digits(n):
    """Recursive algorithm to count the digits in a given number.

    :param n: The number the function is gonna work with.
    :return: The number of digits the 'n' parameter has.
    """
    if n < 10:
        return 1
    return count_digits(n // 10) + 1


def sum_digits(n):
    """Recursive algorithm that sums the digits of a given number.

    :param n: A user's given number.
    :return: The sum of each digit individually.
    """
    print(n)
    if n < 10:
        return n
    return sum_digits(n // 10) + int((str(n)[-1]))


def vocal_counting(msg):
    """Algorithm that counts the number of vocals in a given msg.

    :param msg: The input msg that the function will check.
    :return: The number of vocals in the msg string.
    """
    if not msg:
        return 0
    return (msg[0].lower() in 'aeiou') + vocal_counting(msg[1:])


def reverse_number(n):
    """Algorithm that reverses the digits in a given number.

    :param n: An integer number the user inputs.
    :return: The 'n' parameter reversed, as a integer.
    """
    print(n)
    if not n:
        return ''
    return int(reverse_number(str(n)[1:]) + str(n)[0])


def decimal2binary(n):
    """Algorithm that recursively converts a decimal integer to a binary one.

    :param n: The number in which the action will be perfomed.
    :return:
    """
    if n == 0:
        return ''
    return str(decimal2binary(n // 2)) + str(n % 2)
