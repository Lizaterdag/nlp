#!/usr/bin/env python3
import re, doctest
from collections import Counter


def validate1(s):
    """
    Checks whether the string is a valid employee ID using a single regular expression.
    An employee ID is valid if and only if it consists
    only of 6-10 alphabetic characters (letters), followed by 2 numeric digits.

    (Assumes s is a string without any non-ASCII characters.
    Otherwise, does not make any assumptions about the string.)

    The lines below give example inputs and correct outputs using doctest notation,
    and can be run to test the code. Passing these tests is NOT sufficient
    to guarantee your implementation is correct. You may add additional test cases.

    >>> validate1('AbCdEf00')
    True
    >>> validate1('$0RQLpCHz49')
    False
    """
    # regex start with any alphabetic char that matches the sizes between 6-10, followed by 2 digits
    EMPLOYEE_RE = "^[a-zA-Z]{6,10}\\d{2}$"
    if re.search(EMPLOYEE_RE, s):
        return True
    return False

def validate2(s):
    """
    >>> validate2('AbCdEf00')
    True
    >>> validate2('$0RQLpCHz49')
    False
    """

    # split ID into 2 strings, first 6-10 chars second the 2 digits
    t =[s[i:i+(len(s)-2)] for i in range(0, len(s), len(s)-2)]

    # check for the first 6-10 chars if it contains any violations(digits, special chars)
    if len(t[0]) >= 6 and len(t[0]) <= 10:
        for i in t[0]:
            if i.isdigit():
                return False
            elif not i.isalnum():
                return False
        
        #check if last 2 chars in string are digits
        if len(t[1]) == 2:
            return t[1].isdigit()
    else:
         return False
        

def dna_prob(seq):
    """
    Given a sequence of the DNA bases {A, C, G, T},
    stored as a string, returns a conditional probability table
    in a data structure such that one base (b1) can be looked up,
    and then a second (b2), to get the probability p(b2 | b1)
    of the second base occurring immediately after the first.
    (Assumes the length of seq is >= 3, and that the probability of
    any b1 and b2 which have never been seen together is 0.
    Ignores the probability that b1 will be followed by the
    end of the string.)

    >>> tbl = dna_prob('ATCGATTGAGCTCTAGCG')
    >>> tbl['T']['T']
    0.2
    >>> tbl['G']['A']
    0.5
    >>> tbl['C']['G']
    0.5
    """
    # assuming dna string size is >= 3
    if len(seq) >= 3:
        t = []
        # pairwise
        iterator = iter(seq)
        a = next(iterator, None)
        for b in iterator:
            t.append(f'{a}{b}')
            a = b
        # count duplicate pairs
        count = Counter(t)

     # conditional probability table
    tbl = {}
    dna = ['A', 'C', 'G', 'T']
    for b1 in dna:
        tbl[b1] = {}
        total = sum(count[b1 + b2] for b2 in dna)
        for b2 in dna:
            if total > 0:
                tbl[b1][b2] = count[b1 + b2] / total
            else:
                tbl[b1][b2] = 0.0
    return tbl


def dna_bp(seq):
    """
    Given a string representing a sequence of DNA bases,
    returns the paired sequence, also as a string,
    where A is always paired with T and C with G.

    >>> dna_bp('ATCGATTGAGCTCTAGCG')
    'TAGCTAACTCGAGATCGC'
    """
    # Do not use any libraries.
    # Hint: this can be done in one line. (More than one line is OK too.)
    return seq.translate(str.maketrans('ATCG', 'TAGC'))

if __name__=='__main__':
    # This runs the doctests and prints any failures.
    doctest.testmod()
