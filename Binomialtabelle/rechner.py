import math

def bin(n,k):
    nf = math.factorial(n)
    kf = math.factorial(k)
    nkf = math.factorial((n-k))
    return nf//(kf*nkf)

def musig(n,p):
    mu=n*p
    sig=math.sqrt(mu*(1-p))
    return mu, sig

def b(n,p,r):
    return bin(n,r)*pow(p,r)*pow(1-p,n-r)

def f(n,p,r):
    ftotal = 0
    for i in range(r+1):
        ftotal += b(n,p,i)
    return ftotal

def fdiff(n,p,r1,r2):
    return f(n,p,r2)-f(n,p,r1-1)

def sigmaP(sig,n,p):
    mu, sigma = musig(n,p)
    return fdiff(n,p,math.ceil(mu-sig*sigma),math.floor(mu+sig*sigma))

def rechnen():
    x=0
    Element("ergebnis").element.innerHTML = ""
    try:
        n = int(Element("n").value)
    except:
        Element("ergebnis").element.innerHTML = "Bitte für <sub>n</sub> eine natürliche Zahl eingeben.\n"
    else:
        x+=1
    try:
        p = float(Element("p").value)
    except:
        Element("ergebnis").element.innerHTML += "Bitte für p eine Zahl x eingeben für die gilt 0≤x≤1.\n"
    else:
        x+=1
    try:
        r = int(Element("r").value)
    except:
        Element("ergebnis").write("Bitte für r eine natürliche Zahl eingeben.", append=True)
    else:
        if x==2:
            if n>=r:
                x+=1
            else:
                Element("ergebnis").write("Bitte für r eine natürliche Zahl kleiner gleich n eingeben.", append=True)

    if x == 3:
        k = js.document.querySelector("#k").checked
        v = js.document.querySelector("#v").checked

        if k:
            if v:
                Element("ergebnis").write("1 - P(X ≤ " + str(r) + ") = " + str((1 - f(n, p, r)) * 100) + "%")
            else:
                Element("ergebnis").write("P(X ≤ " + str(r) + ") = " + str(f(n, p, r) * 100) + "%")
        if not k:
            if v:
                Element("ergebnis").write("1 - P(X = " + str(r) + ") = " + str((1 - b(n, p, r)) * 100) + "%")
            else:
                Element("ergebnis").write("P(X = " + str(r) + ") = " + str(b(n, p, r) * 100) + "%")
