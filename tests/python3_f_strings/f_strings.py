width = 10
precision = 4
value = decimal.Decimal("12.34567")
f"result: {value:{width}.{precision}}"
rf"result: {value:{width}.{precision}}"

foo(f'this SHOULD be a multi-line string because it is '
    f'very long and does not fit on one line. And {value} is the value.')

foo('this SHOULD be a multi-line string, but not reflowed because it is '
    f'very long and and also unusual. And {value} is the value.')

foo(fR"this should NOT be \t "
    rF'a multi-line string \n')
