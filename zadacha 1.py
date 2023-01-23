try:
    def ras(yskr):
        def ras1():
            yskr()
            b = v * t
            return b
    def yskr():
        v0 = int(input())
        v = int(input())
        t = int(input())
        d = (v0 - v) / t
        return d
    yskr = ras(yskr)
    print(yskr())
except ValueError:
    print('Даннные не являются числами')

except ZeroDivisionError:
    print('t = 0')

