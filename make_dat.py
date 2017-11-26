import re

def getval(x):
    a = x.split('=')
    return a[1].replace(';', '').strip()

vals = ('double[][] vectors =',
        'double[][] coefficients = ',
        'double[] intercepts = ',
        'int[] weights =')

nb = re.compile('^.*new Brain.(\d+), (\d+), [^,]+, [^,]+, [^,]+, [^,]+, "([^"]+)", (\d+\.\d+), (\d+\.\d+), (\d+)..*$')

found = {}

with open('Brain.java') as fp:
    for line in fp:
        for val in vals:
            if val in line:
                found[val] = getval(line)
        m = nb.match(line)
        if m:
            for i in range(1, 7):
                print(m.group(i))

for val in vals:
    print(found[val])
