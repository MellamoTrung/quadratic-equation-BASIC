'''
   Enter in this format:
   ax^2 +bx +c = dx^2 +ex +k(Order is not important).
   3x^2 +3x -5 = 15x -11 -3x^2
   If you don't enter the '=' part, it will be 0:
   -x^2 -2x +1 will be -x^2 -2x +1 = 0
   You can enter more than 3 numbers:
   -x^2 -x^2 +x +2 -3x = -4x^2 -2
   
   Known bugs:
   -If you multiply output and numbers are irrational,it could be a little different from input.
   -If solutions are imaginary,code can't factor input.
   
   You can enter more than one equations.
   
   Please comment input if the output is wrong.
'''

from math import sqrt
from cmath import sqrt as sqr
from fractions import gcd
from functools import reduce
import re


def IsInt(n):return True if not n%1 else False
def abc(i):
    i = i.split()
    _a,_b,_c = [],[],[]
    for z in range(len(i)):
        if "^" in i[z]:
            a = re.sub(r"[a-zA-Z+]\^2","",i[z])
            if a =='-':_a.append(-1)
            elif not a and not a==0:_a.append(1)
            else:
                try:_a.append(int(a)) if not "." in a else _a.append(float(a))
                except: raise
        else:
            try:_c.append(int(i[z])) if not"." in i[z] else _c.append(float(i[z]))
            except:
                b = re.sub(r"[a-zA-Z+]","",i[z]) 
                if b =='-':_b.append(-1)
                elif not b and not b==0:_b.append(1)
                else:
                    try:_b.append(int(b)) if not "." in b else _b.append(float(b))
                    except:raise
                    
    try: a = sum(_a)
    except: a = 0
    try: b = sum(_b)
    except: b = 0
    try: c = sum(_c)
    except: c = 0
    
    return [a,b,c]
    


while 1:

    try:del a,b,c;print("\n\n")
    except:pass
    try:i = input()
    except EOFError:break
    if "=" in i:
        i = i.split("=")
        left=abc(i[0])
        right = abc(i[1])
        a,b,c = [l-r for l,r in zip(left,right)]

    else:
        a,b,c = [abc(i)[x] for x in range(3)]


    try:
        if a==0 and b!=0:print("The solution is: {}".format(-c/b if not IsInt(-c/b) else int(-c/b)));continue
        print('Solve the quadratic equation: ' + str(a)*(a!=1)+'x^2 '+(b>=0)*'+'+str(b)+'x ' +(c>=0)*'+'+str(c) +' = 0')
        if type(a)==float or type(b)==float or type(c)==float:
            q = 1
            while not (IsInt(a) and IsInt(b) and IsInt(c)):
                a,b,c,q=a*10,b*10,c*10,q/10
        
            a,b,c = int(a),int(b),int(c)
        delta = (b**2) - (4*a*c)
        if delta<0:
            print("The solutions are {} and {}".format((-b-sqr(delta))/(2*a), (-b+sqr(delta))/(2*a)))
        else:
            if delta>0:
                solution1 = ((-b-sqrt(delta))/(2*a))
                solution2 = ((-b+sqrt(delta))/(2*a))
                solution1 = int(solution1) if IsInt(solution1) else solution1
                solution2 = int(solution2) if IsInt(solution2) else solution2
                print('The solutions are {0} and {1}'.format(solution1, solution2))
            else:
                solution = (-b)/(2*a)
                solution = int(solution) if IsInt(solution) else solution
                print('The solution is {}'.format(solution) if not IsInt(solution) else 'The solution is {}'.format(int(solution)))
    except:
        print("Sorry, no solutions were found")
        continue
    try:
        q*=1
        if delta<0:
            print("Sorry, I can't factor this")
            continue
        elif delta==0:
            n = reduce(gcd,[a,b,c])
            a, b, c =a//n, b//n, c//n
            an = int(sqrt(a)) if IsInt(sqrt(a)) else sqrt(a)
            cn = sqrt(c) if b>0 else -sqrt(c)
            cn = int(cn) if IsInt(cn) else cn

            if n==1: print("{}({}x{}{})^2".format(q,an,"+" if cn>=0 else "",cn) if an != 1 else "{}(x{}{})^2".format(q,"+" if cn>=0 else "",cn))
            else:print("{}({}x{}{})^2".format(n*q,an,"+" if cn>=0 else "",cn) if an != 1 else "{}(x{}{})^2".format(n*q,"+" if cn>=0 else "",cn))
            continue
        else:
            if c==0:
                e = abs(gcd(a,b))
                if e == 1:print("{}x({}x{}{})".format(q,a,'+' if b>0 else '',b) if a//e != 1 else "{}x(x{}{})".format(q,'+' if b>0 else '',b));continue
                else:print("{}x({}x{}{})".format(q*e,a//e, '+' if b//e>0 else '',b//e) if a//e!=1 else "{}x(x{}{})".format(q*e,'+' if b//e>=0 else '',b//e));continue
            l = [w for w in range(1,a+1) if not a%w]
            s1 = solution1*-1
            s2 = solution2*-1
            f = [[1,s1],[1,s2]]
            for a,b in zip(l,l):
                if not IsInt(f[0][0]) or not IsInt(f[0][1]):
                    if IsInt(f[0][1]*a) and IsInt(f[0][0]*a):
                        f[0][0] *= a
                        f[0][1] *= a
                if not IsInt(f[1][0]) or not IsInt(f[1][1]):
                    if IsInt(f[1][1]*b) and IsInt(f[1][0]*b):
                        f[1][0] *= b
                        f[1][1] *= b
            for x in range(len(f)):
                for y in range(len(f[x])):
                    if IsInt(f[x][y]):f[x][y] = int(f[x][y])
            if f[0][0] != 1 and a!=1 and( not IsInt(f[0][1]) or not IsInt(f[1][1])):
                if f[1][0] != 1:
                    w = a/(f[0][0]*f[1][0])
                    w = int(w) if IsInt(w) else w
                    print("{}({}x{}{})({}x{}{})".format(q*w,f[0][0],"+" if f[0][1] >= 0 else '',f[0][1],f[1][0],'+' if f[1][1]>=0 else '',f[1][1]))
                    continue
                else:
                    w = a/(f[0][0])
                    w = int(w) if IsInt(w) else w
                    print("{}({}x{}{})(x{}{})".format(q*w,f[0][0],'+' if f[0][1]>=0 else '',f[0][1],'+' if f[1][1]>=0 else '',f[1][1]))
                    continue
            elif a!=1 and f[1][0] != 1 and (not IsInt(f[0][1]) or not IsInt(f[1][1])):
                w = a/(f[1][0])
                w = int(w) if IsInt(w) else w
                print("{}(x{}{})({}x{}{})".format(w*q,'+' if f[0][1]>=0 else '', f[1][0],'+' if f[1][1]>=0 else '',f[1][1]))
                continue
            elif a!=1 and f[0][0] == 1 and f[1][0] == 1 and (not IsInt(f[0][1]) or not IsInt(f[1][1])):
                print("{}(x{}{})(x{}{})".format(a*q,'+' if f[0][1]>=0 else '',f[0][1],'+' if f[1][1]>=0 else '',f[1][1]))
                continue
            elif a==1 and (not IsInt(f[0][1]) or not IsInt(f[1][1])):
                print("{}(x{}{})(x{}{})".format(q,'+' if f[0][1]>=0 else '',f[0][1],'+' if f[1][1]>=0 else '',f[1][1]));continue
            else:
                if f[0][0]==1:
                    if f[1][0]==1:
                        print("{}(x{}{})(x{}{})".format(q,"+" if f[0][1]>=0 else "", f[0][1],"+" if f[1][1]>=0 else "",f[1][1]));continue
                    else:print("{}(x+{})({}x+{})".format(q,f[0][1],f[1][0],f[1][1]));contiñue
                else:
                    if f[1][0]==1:
                        print("{}({}x{}{})(x{}{})".format(q,f[0][0],'+' if f[0][1] >= 0 else '',f[0][1],"+" if f[1][1]>=0 else '' ,f[1][1]));continue
                    else: print("{}({}x{}{})({}x{}{})".format(q,f[0][0],'+' if f[0][1]>=0 else '', f[0][1],f[1][0],'+' if f[1][1]>=0 else '', f[1][1]));continue
    except:pass
    
    if delta<0:
            print("Sorry, I can't factor this")
            continue
    elif delta==0:
        n = reduce(gcd,[a,b,c])
        a, b, c =a//n,b//n, c//n
        
        an = int(sqrt(a)) if IsInt(sqrt(a)) else sqrt(a)
        cn = sqrt(c) if b>0 else -sqrt(c)
        cn = int(cn) if IsInt(cn) else cn

        if n==1: print("({}x{}{})^2".format(an,"+" if cn>=0 else "",cn) if an != 1 else "(x{}{})^2".format("+" if cn>=0 else "",cn))
        else:
            print("{}({}x{}{})^2".format(n,an,"+" if cn>=0 else "",cn) if an != 1 else "{}(x{}{})^2".format(n,"+" if cn>=0 else "",cn))
        continue
    else:
        if c==0:
            e = abs(gcd(a,b))
            if e == 1:print("x({}x{}{})".format(a,'+' if b>0 else '',b) if a != 1 else "x(x{}{})".format('+' if b>0 else '',b));continue
            else:print("{}x({}x{}{})".format(e,a//e, '+' if b//e>0 else '',b//e) if a//e!=1 else "{}x(x{}{})".format(e,'+' if b//e>=0 else '',b//e));continue
        l = [w for w in range(1,a+1) if not a%w]
        s1 = solution1*-1
        s2 = solution2*-1
        f = [[1,s1],[1,s2]]
        for a,b in zip(l,l):
            if not IsInt(f[0][0]) or not IsInt(f[0][1]):
                if IsInt(f[0][1]*a) and IsInt(f[0][0]*a):
                    f[0][0] *= a
                    f[0][1] *= a
            if not IsInt(f[1][0]) or not IsInt(f[1][1]):
                if IsInt(f[1][1]*b) and IsInt(f[1][0]*b):
                    f[1][0] *= b
                    f[1][1] *= b
        for x in range(len(f)):
            for y in range(len(f[x])):
                if IsInt(f[x][y]):f[x][y] = int(f[x][y])
        if f[0][0] != 1 and a!=1 and( not IsInt(f[0][1]) or not IsInt(f[1][1])):
            if f[1][0] != 1:
                w = a/(f[0][0]*f[1][0])
                w = int(w) if IsInt(w) else w
                print("{}({}x{}{})({}x{}{})".format(w,f[0][0],"+" if f[0][1] >= 0 else '',f[0][1],f[1][0],'+' if f[1][1]>=0 else '',f[1][1]))
                continue
            else:
                w = a/(f[0][0])
                w = int(w) if IsInt(w) else w
                print("{}({}x{}{})(x{}{})".format(w,f[0][0],'+' if f[0][1]>=0 else '',f[0][1],'+' if f[1][1]>=0 else '',f[1][1]))
                continue
        elif a!=1 and f[1][0] != 1 and (not IsInt(f[0][1]) or not IsInt(f[1][1])):
            w = a/(f[1][0])
            w = int(w) if IsInt(w)else w
            print("{}(x{}{})({}x{}{})".format(w,'+' if f[0][1]>=0 else '', f[1][0],'+' if f[1][1]>=0 else '',f[1][1]))
            continue
        elif a!=1 and f[0][0] == 1 and f[1][0] == 1 and (not IsInt(f[0][1]) or not IsInt(f[1][1])):
            print("{}(x{}{})(x{}{})".format(a,'+' if f[0][1]>=0 else '',f[0][1],'+' if f[1][1]>=0 else '',f[1][1]))
            continue
        elif a==1 and (not IsInt(f[0][1]) or not IsInt(f[1][1])):
            print("(x{}{})(x{}{})".format('+' if f[0][1]>=0 else '',f[0][1],'+' if f[1][1]>=0 else '',f[1][1]))
        else:
            if f[0][0]==1:
                if f[1][0]==1:
                    print("(x{}{})(x{}{})".format("+" if f[0][1]>=0 else "", f[0][1],"+" if f[1][1]>=0 else "",f[1][1]))
                else:print("(x{}{})({}x{}{})".format('+'if f[0][1]>=0 else '',f[0][1],f[1][0],'+' if f[1][1]>=0 else '',f[1][1]))
            else:
                if f[1][0]==1:
                    print("({}x{}{})(x{}{})".format(f[0][0],'+' if f[0][1] >= 0 else '',f[0][1],"+" if f[1][1]>=0 else '' ,f[1][1]))
                else: print("({}x{}{})({}x{}{})".format(f[0][0],'+' if f[0][1]>=0 else '', f[0][1],f[1][0],'+' if f[1][1]>=0 else '', f[1][1]))
