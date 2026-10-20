def dot(a: complex, b: complex):
	return (a.conjugate() * b).real

def cross(a: complex, b: complex):
	return (a.conjugate() * b).imag

def incircle(p0, p1, p2):
	d0, d1, d2 = abs(p2 - p1), abs(p0 - p2), abs(p1 - p0)
	c = (d0 * p0 + d1 * p1 + d2 * p2) / (d0 + d1 + d2)
	r = abs(cross(p1 - p0, p2 - p0)) / (d0 + d1 + d2)
	return (c, r)

p0 = complex(*map(int, input().split()))
p1 = complex(*map(int, input().split()))
p2 = complex(*map(int, input().split()))
c, r = incircle(p0, p1, p2)
print(f'{c.real:.15f} {c.imag:.15f} {r:.15f}')
