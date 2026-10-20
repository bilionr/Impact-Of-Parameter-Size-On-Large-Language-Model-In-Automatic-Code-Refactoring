# the crossing points of two circles
def circles_cross_points(x1, y1, r1, x2, y2, r2):
    rr0 = (x2 - x1)**2 + (y2 - y1)**2
    xd = x2 - x1
    yd = y2 - y1
    rr1 = r1**2; rr2 = r2**2
    cv = (rr0 + rr1 - rr2)
    sv = (4*rr0*rr1 - cv**2)**.5
    return (
        (x1 + (cv*xd - sv*yd)/(2.*rr0), y1 + (cv*yd + sv*xd)/(2.*rr0)),
        (x1 + (cv*xd + sv*yd)/(2.*rr0), y1 + (cv*yd - sv*xd)/(2.*rr0)),
    )

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
ANS1, ANS2 = circles_cross_points(x1, y1, r1, x2, y2, r2)
if ANS1[0] > ANS2[0]:
    ANS1, ANS2 = ANS2, ANS1
elif ANS1[0] == ANS2[0]:
    if ANS1[1] > ANS2[1]:
        ANS1, ANS2 = ANS2, ANS1
print(*ANS1, *ANS2)

