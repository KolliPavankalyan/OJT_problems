'''Write a callable called float_range that acts sort of like the built-in range callable
but it should allow for floating point numbers to be specified as start, stop, and
step values.
>>> r = float_range(0.5, 2.5, 0.5)
>>> r
float_range(0.5, 2.5, 0.5)
>>> list(r)
[0.5, 1.0, 1.5, 2.0]
>>> len(r)
4
>>> for n in r:
... print(n)
...
0.5
1.0
1.5
2.0'''


def foatRaange(start,stop,range):
    while start<stop:
        print(start)
        start+=range
print(foatRaange(0.5,2.5,0.5))