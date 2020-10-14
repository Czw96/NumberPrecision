# NumberPrecision
Perform addition, subtraction, multiplication and division operations precisely using python

## Why
```python
0.1 + 0.2 = 0.30000000000000004
1.0 - 0.9 = 0.09999999999999998
```

## Install
```python
pip install number_precision
```

## Methods
```python
NP.plus(num1, num2, num3, ...)   // addition, num + num2 + num3, two numbers is required at least.
NP.minus(num1, num2, num3, ...)  // subtraction, num1 - num2 - num3
NP.times(num1, num2, num3, ...)  // multiplication, num1 * num2 * num3
NP.divide(num1, num2, num3, ...) // division, num1 / num2 / num3
NP.round(num, ratio)  // round a number based on ratio
```

## Usage
```python
from number_precision import NP

NP.plus(0.1, 0.2)             // = 0.3, not 0.30000000000000004
NP.plus(2.3, 2.4)             // = 4.7, not 4.699999999999999
NP.minus(1.0, 0.9)            // = 0.1, not 0.09999999999999998
NP.times(3, 0.3)              // = 0.9, not 0.8999999999999999
NP.times(0.362, 100)          // = 36.2, not 36.199999999999996
NP.divide(1.21, 1.1)          // = 1.1, not 1.0999999999999999
NP.round(0.105, 2)            // = 0.11, not 0.1
NP.plus(0.1, 0.005, round=2)  // = 0.11, not 0.1
```

## License
MIT