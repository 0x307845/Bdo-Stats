def factorielle(n):
    if n == 0:
        return 1
    else:
        return n  * factorielle(n-1)
def combin(n, k):
    if k > n//2:
        k = n-k
    x = 1
    y = 1
    i = n-k+1
    while i <= n:
        x = (x*i)//y
        y += 1
        i += 1
    return x
def binom(k,n,p) :
    return combin(n,k)*pow(p,k)*pow(1-p,n-k)


def taux_var(p,t) :
    i = 1
    while True :
        a = 1-binom(0,i,p)
        print(a)
        if a >= t:
            break
        i = i + 1
    return [i , a]


def cost(market_price,Try,cron) :
    cost = (Try*cron+ 1)*2
    if cost > market_price:
        return [False , cost]
    return [True , cost]

print(taux_var(0.1875,0.70))
print(cost(2000,6,142))
