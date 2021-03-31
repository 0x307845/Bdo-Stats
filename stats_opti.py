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

def cost(market_price,Try,cron) :
    cost = (Try*cron+ 1)*2
    if cost > market_price:
        return [False , cost]
    return [True , cost]

def taux_var(p,t) :
    i = 1
    while True :
        a = 1-binom(0,i,p)
        if a >= t:
            break
        i = i + 1
    return i , a

def stats(p,t,m,c) :
    taux = taux_var(p,t)
    cout = cost(m,taux[0],c)
    a = taux[0]
    if cout[0] == True :
        d = a
        while True :
            cout_b = cost(m,d,c)
            d = d +1
            if cout_b[0] == False :
                break
    return [t,a ,cout[0],cout[1] , p , m , d ,c]
a = stats(0.1875,0.70,2000,147)

print("\nProbabilité : " , a[4]*100,'%')
print("Prix du marché :", a[7])
print("Cron par tentative : ", a[7])
print("========================================")
print('Nombre de try pour attendre ', a[0]*100,'% : ' , a[1])
print('Cout total : ', a[3])
print('Rentabilité : ', a[2])
try :
    print('Try max :' , a[6])
except :
    pass
try :
    print('Probabilité max :' , (1-binom(0,8,0.1875))*100)
except :
    pass
print('\n\nPrix en Million !')
