#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 2
day = 4

def test_code():
    assert main.letterPos("bazooka", "o") == 4, 'letterPos("bazooka", "o") == 4 failed'
    assert main.letterPos("exterior", "e") == 1, 'letterPos("exterior", "e") == 1 failed'
    assert main.letterPos("alligator", "r") == 9, 'letterPos("alligator", "r") == 9 failed'

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
