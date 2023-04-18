import math

def bin(n,k):
    nf = math.factorial(n)
    kf = math.factorial(k)
    nkf = math.factorial((n-k))
    return nf//(kf*nkf)

def b(n,p,r):
    return bin(n,r)*pow(p,r)*pow(1-p,n-r)

def f(n,p,r):
    ftotal = 0
    for i in range(r+1):
        ftotal += b(n,p,i)
    return ftotal

def rechnen():
    try:
        n = int(Element("n").value)
    except ValueError:
        Element("ergebnis").write("Bitte für n eine natürliche Zahl eingeben.")
    try:
        p = float(Element("p").value)
    except ValueError:
        Element("ergebnis").write("Bitte für p eine Zahl x eingeben für die gilt 0≤x≤1.", append=True)
    try:
        r = int(Element("r").value)
    except ValueError:
        Element("ergebnis").write("Bitte für r eine natürliche Zahl eingeben.", append=True)

    k = js.document.querySelector("#k").checked

    if k:
        Element("ergebnis").write("(P ≤ "+str(r)+") = "+str(f(n,p,r)*100)+"%")
    if not k:
        Element("ergebnis").write("(P = "+str(r)+") = "+str(b(n,p,r)*100)+"%")
