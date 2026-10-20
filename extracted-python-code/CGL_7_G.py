from math import sqrt
def common_tangent_points(x1, y1, r1, x2, y2, r2):
    result = []
    xd = x2 - x1; yd = y2 - y1
 
    rr0 = xd**2 + yd**2
    if (r1 - r2)**2 <= rr0:
        # 共通外接線
        cv = r1 - r2
        if rr0 == (r1 - r2)**2:
            # 円が内接する場合 => 共通外接線は1本
            result.append((x1 + r1*cv*xd/rr0, y1 + r1*cv*yd/rr0))
        else:
            sv = sqrt(rr0 - cv**2)
            # (x1, y1) + r1/r0*R(±θ)(x2 - x1, y2 - y1)
            result.append((x1 + r1*(cv*xd - sv*yd)/rr0, y1 + r1*(sv*xd + cv*yd)/rr0))
            result.append((x1 + r1*(cv*xd + sv*yd)/rr0, y1 + r1*(-sv*xd + cv*yd)/rr0))
    if (r1 + r2)**2 <= rr0:
        # 共通内接線
        cv = r1 + r2
        if rr0 == (r1 + r2)**2:
            # 円が外接する場合 => 共通内接線は1本
            result.append((x1 + r1*cv*xd/rr0, y1 + r1*cv*yd/rr0))
        else:
            sv = sqrt(rr0 - cv**2)
            # (x1, y1) + r1/r0*R(±θ)(x2 - x1, y2 - y1)
            result.append((x1 + r1*(cv*xd - sv*yd)/rr0, y1 + r1*(sv*xd + cv*yd)/rr0))
            result.append((x1 + r1*(cv*xd + sv*yd)/rr0, y1 + r1*(-sv*xd + cv*yd)/rr0))
    return result

cx1, cy1, r1 = map(int, input().split())
cx2, cy2, r2 = map(int, input().split())
ANS = sorted(common_tangent_points(cx1, cy1, r1, cx2, cy2, r2))
for x, y in ANS:
    print(x, y)
