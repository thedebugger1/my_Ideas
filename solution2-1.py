def decimalToBase(dn, db):
    """Convert Desired No(dn) a positive number to desire Base(db)"""
    digits = []
    while dn > 0:
        digits.insert(0, str(dn % db))
        dn = dn / db
    return ''.join(digits)


def baseToDecimal(bn, cb):
    """Convert Base No(bn) a positive number to decimal wrt current Base(cb)"""
    n = 0
    for d in str(bn):
        n = cb * n + int(d)
    return n


def getSubtract(x, y, b):
    if b == 10:
        return int(x) - int(y)

    dx = baseToDecimal(x, b)
    dy = baseToDecimal(y, b)
    dz = dx - dy
    return decimalToBase(dz, b)


b = int(input("Enter base of integer: "))
n = int(input("Enter any number: "), b)
a = str(n)
k = len(a)
c = str
minionID = [n]
ind = 0
for i in minionID:
    desc = "".join(sorted(str(n), reverse=True))
    asc = "".join(sorted(str(n)))
    x = int(desc)
    y = int(asc)
    z = x-y
    if len(str(z)) < k:
        c = (k - len(str(z))) * '0' + str(z)
        minionID.append(c)
        n = c
    else:
        minionID.append(z)
        n = z
    if minionID.count(i) > 1:
        ind = minionID.index(i)
        break

print(minionID)
print(ind)
print((len(minionID) - 1) - ind)
