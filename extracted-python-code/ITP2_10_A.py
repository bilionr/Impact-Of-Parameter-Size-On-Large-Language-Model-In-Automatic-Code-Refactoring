inf = 2**32
# print(type(inf), inf)
x = int(input())
x_rev = x ^ 0xffffffff
x_lshift = (x << 1) % inf
x_rshift = x >> 1
print(f'{x:032b}')
print(f'{x_rev:032b}') 
print(f'{x_lshift:032b}') 
print(f'{x_rshift:032b}') 

# print(bi_x.zfill(32))
