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
    #Alle drei Checkboxen(kumuliert, invertiert, und kumuliert Differenz) werden in Variablen gespeichert
    inv = js.document.querySelector("#v").checked
    kum = js.document.querySelector("#k").checked
    kumS = js.document.querySelector("#kS").checked

    #Es kann entweder k oder kS gedrückt werden nicht beides
    if kum:
        js.document.querySelector("#kS").setChecked(unchecked)
    if kumS:
        js.document.querySelector("#k").setChecked(unchecked)   
    x=0
    #Ausgabefeld wird gelöscht
    Element("ergebnis").element.innerHTML = ""

    #Eingabe Überprüfung
    if kum:


