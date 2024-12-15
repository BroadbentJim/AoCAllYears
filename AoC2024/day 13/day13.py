import math
D = open("input.txt").readlines()

def batcher(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]
        

def calc_determinant(A_X,A_Y,B_X,B_Y):
    return A_X * B_Y - A_Y *B_X

def non_zero_determinant(A_X,A_Y,B_X,B_Y,P_X,P_Y, det) -> tuple[bool, int]:
    top_comp = B_Y*P_X - B_X * P_Y
    bot_comp = -A_Y*P_X+A_X*P_Y
    if top_comp % det != 0 or bot_comp % det != 0:
        return (False, 0)
    sol_X, sol_Y = top_comp // det, bot_comp // det
    if sol_X < 0 or sol_Y < 0:
        return (False,0)
    return (True, 3*sol_X + sol_Y)

def zero_determinant(A_X,A_Y,B_X,B_Y,P_X,P_Y) -> tuple[bool, int]:
    if (A_X,A_Y) == (0,0) or (B_X,B_Y) == (0,0):
        if (A_X,A_Y) == (0,0) and (B_X,B_Y) == (0,0):
            return ((P_X,P_Y) == (0,0), 0)
        if (A_X,A_Y) != (0,0):
            return (calc_determinant(A_X, A_Y, P_X, P_Y) == 0, P_X // A_X)
        if (B_X,B_Y) != (0,0):
            return (calc_determinant(B_X, B_Y, P_X, P_Y) == 0, P_X // B_X)
    if calc_determinant(A_X,B_X,P_X,P_Y) != 0: # Relying a bit on exact integer stuff here
        # May need to migrate to ratios being equal rather than difference == 0
        return (False, 0)
    if A_X > P_X and B_X > P_X:
        return (False, 0)
    if A_X > P_X:
        return (P_X % B_X == 0, P_X // B_X)
    if B_X > P_X:
        return (P_X % A_X == 0, 3* P_X // A_X)
    # A_X <= P_X & B_X <= P_X
    # Not both zero, already covered
    # Ensure we use the non-zero coordinate
    if A_X == 0:
        A_Z = A_Y
        B_Z = B_Y
        P_Z = P_Y
    else:
        A_Z = A_X
        B_Z = B_X
        P_Z = P_X
    d = math.gcd(A_Z, B_X)
    if P_Z % d != 0:
        return (False, 0)
    # P_Z lies in the integer span of (A_Z, B_Z)
    q,r = extended_gcd(A_Z, B_Z)
    if A_Z > 3 * B_Z:
        k = math.floor(q*d / B_Z)
    else:
        k = - math.ceil(d*r / A_Z)
    left_interior = q - k*B_Z//d
    right_interior = r + k *A_Z//d
    return (P_Z // d) * (3*left_interior + right_interior)
    
    
def extended_gcd(a,b) -> tuple[int,int]:
    old_r,r = a,b
    old_s, s = 1,0
    old_t,t = 0,1
    
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t,t = t, old_t - quotient * t
    print(f"GCD {a=},{b=}, {old_r}")
    print(f"Bezout coeffs, q={old_s}, r={old_t}")
    assert math.gcd(a,b) == old_r
    assert old_s * a + old_t * b == old_r
    return old_s, old_t
    

def process_group(A_X,A_Y,B_X,B_Y,P_X,P_Y) -> tuple[bool, int]:
    if (P_X, P_Y) == (0,0):
        return (True, 0)
    det = calc_determinant(A_X,A_Y,B_X,B_Y)
    if det == 0:
        return zero_determinant(A_X,A_Y,B_X,B_Y,P_X,P_Y)
    else:
        return non_zero_determinant(A_X,A_Y,B_X,B_Y,P_X,P_Y, det)        
        

# ans =0
# for batch in batcher(D, n=4):
#     # print(batch)
#     if len(batch) <4:
#         A,B,P, = batch    
#     else:
#         A,B,P,_ = batch
#     A = A.split(":")[1]
#     X_, Y_ = A.split(',')
#     A_X = int(X_.split('+')[1])
#     A_Y = int(Y_.split('+')[1])
#     X_, Y_ = B.split(',')
#     B_X = int(X_.split('+')[1])
#     B_Y = int(Y_.split('+')[1])
#     P = P.split(':')[1]
#     X_, Y_ = P.split(',')
#     P_X = int(X_.split('=')[1])
#     P_Y = int(Y_.split('=')[1])
#     print(A_X,A_Y,B_X,B_Y,P_X,P_Y)
#     can, cost = process_group(A_X,A_Y,B_X,B_Y,P_X,P_Y)
#     print(can,cost)
#     if can:
#         ans += cost
# print(ans)

OFFSET = 10000000000000

ans =0
for batch in batcher(D, n=4):
    # print(batch)
    if len(batch) <4:
        A,B,P, = batch    
    else:
        A,B,P,_ = batch
    A = A.split(":")[1]
    X_, Y_ = A.split(',')
    A_X = int(X_.split('+')[1])
    A_Y = int(Y_.split('+')[1])
    X_, Y_ = B.split(',')
    B_X = int(X_.split('+')[1])
    B_Y = int(Y_.split('+')[1])
    P = P.split(':')[1]
    X_, Y_ = P.split(',')
    P_X = int(X_.split('=')[1])
    P_X += OFFSET
    P_Y = int(Y_.split('=')[1])
    P_Y += OFFSET
    print(A_X,A_Y,B_X,B_Y,P_X,P_Y)
    can, cost = process_group(A_X,A_Y,B_X,B_Y,P_X,P_Y)
    print(can,cost)
    if can:
        ans += cost
print(ans)