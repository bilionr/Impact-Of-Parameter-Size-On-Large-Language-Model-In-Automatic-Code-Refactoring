def ref(p, b, e):
    t = (p - b) / (e - b)
    return t.conjugate() * (e - b) + b

a, b, c, d = map(int, input().split())
query = int(input())
q = complex(a, b)
r = complex(c, d)
for _ in range(query):
    x, y = map(int, input().split())
    p = complex(x, y)
    reflection = ref(p, q, r)
    print(reflection.real, reflection.imag)
 
