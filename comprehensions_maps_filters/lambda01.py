#! /usr/bin/env python3
# lambda functions can only be used when a function can be written as an expression
# They don’t support multi-statement functions or functions that don’t return a value.
print (lambda numerator, denominator: numerator / denominator)(10,15)