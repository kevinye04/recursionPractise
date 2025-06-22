#################################################
# hw9.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_f22_week9_linter
import math, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

def oddCount(L):
    if len(L) == 0:
        return 0
    else:
        count = 0
        if L[0] % 2 != 0:
            count = 1
        return count + oddCount(L[1:])
def oddSum(L):
    if len(L) == 0:
        return 0
    else:
        current = 0
        if L[0] % 2 != 0:
            current = L[0]
        return current + oddSum(L[1:])
def oddsOnly(L):
    if len(L) == 0:
        return []
    else:
        current = []
        if L[0] % 2 != 0:
            current = [L[0]]
        return current + oddsOnly(L[1:])
def maxOdd(L):
    if len(L) == 0:
        return None
    else:
        first = L[0]
        rest_max = maxOdd(L[1:])
        if first % 2 != 0:
            if rest_max is None:
                return first
            else:
                if first > rest_max:
                    return first
                else:
                    return rest_max
        else:
            return rest_max

def hasConsecutiveDigits(n):
    n_str = str(n) 
    if len(n_str) < 2:   
        return False
    else:  
        return (n_str[0] == n_str[1]) or hasConsecutiveDigits(n_str[1:])

def alternatingSum(L):
    if not L: 
        return 0
    if len(L) == 1:  
        return L[0]
    return L[0] - L[1] + alternatingSum(L[2:])

#################################################
# Freddy Fractal Viewer
#################################################

from cmu_112_graphics import *

def appStarted(app):
    pass

def keyPressed(app, event):
    pass

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2,
                       text='Draw your Freddy Fractal here!',
                       font='Arial 24 bold')

def runFreddyFractalViewer():
    print('Running Freddy Fractal Viewer!')
    runApp(width=400, height=400)

#################################################
# Test Functions
#################################################

def testOddCount():
    print('Testing oddCount()...', end='')
    assert(oddCount([ ]) == 0)
    assert(oddCount([ 2, 4, 6 ]) == 0) 
    assert(oddCount([ 2, 4, 6, 7 ]) == 1)
    assert(oddCount([ -1, -2, -3 ]) == 2)
    assert(oddCount([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 6)
    print('Passed!')

def testOddSum():
    print('Testing oddSum()...', end='')
    assert(oddSum([ ]) == 0)
    assert(oddSum([ 2, 4, 6 ]) == 0) 
    assert(oddSum([ 2, 4, 6, 7 ]) == 7)
    assert(oddSum([ -1, -2, -3 ]) == -4)
    assert(oddSum([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 1+3+5+7+9+11)
    print('Passed!')

def testOddsOnly():
    print('Testing oddsOnly()...', end='')
    assert(oddsOnly([ ]) == [ ])
    assert(oddsOnly([ 2, 4, 6 ]) == [ ]) 
    assert(oddsOnly([ 2, 4, 6, 7 ]) == [ 7 ])
    assert(oddsOnly([ -1, -2, -3 ]) == [-1, -3])
    assert(oddsOnly([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == [1,3,5,7,9,11])
    print('Passed!')

def testMaxOdd():
    print('Testing maxOdd()...', end='')
    assert(maxOdd([ ]) == None)
    assert(maxOdd([ 2, 4, 6 ]) == None) 
    assert(maxOdd([ 2, 4, 6, 7 ]) == 7)
    assert(maxOdd([ -1, -2, -3 ]) == -1)
    assert(maxOdd([ 1,2,3,4,5,6,7,8,9,10,0,0,0,11,12 ]) == 11)
    print('Passed!')

def testHasConsecutiveDigits():
  print('Testing hasConsecutiveDigits()...', end='')
  assert(hasConsecutiveDigits(1123) == True)
  assert(hasConsecutiveDigits(-1123) == True)
  assert(hasConsecutiveDigits(1234) == False)
  assert(hasConsecutiveDigits(0) == False)
  assert(hasConsecutiveDigits(1233) == True)
  print("Passed!")

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([1,2,3,4,5]) == 1-2+3-4+5)
    assert(alternatingSum([ ]) == 0)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testOddCount()
    testOddSum()
    testOddsOnly()
    testMaxOdd()
    testHasConsecutiveDigits()
    testAlternatingSum()
    runFreddyFractalViewer()

def main():
    cs112_f22_week9_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()
