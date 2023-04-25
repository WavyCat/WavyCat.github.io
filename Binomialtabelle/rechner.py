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
    
    #Checksummen für kum und kumS
    x1=0
    x2=0

    #Ausgabefeld wird gelöscht
    Element("ergebnis").element.innerHTML = ""

    #Eingabe Überprüfung
    try:
        n = int(Element("n").value)
    except:
        Element("ergebnis").element.innerHTML += "Bitte für n eine natürliche Zahl eingeben.<br />"
    else:
        x1+=1
        x2+=1

    try:
        p = float(Element("p").value)
    except:
        Element("ergebnis").element.innerHTML += "Bitte für p eine reele Zahl zwischen 0 und 1 eingeben.<br />"
    else:
        x1+=1
        x2+=1

    try:
        r = int(Element("r").value)
    except:
        Element("ergebnis").element.innerHTML += "Bitte für r eine natürliche Zahl eingeben.<br />"
    else:
        if n>=r:
            x1+=1
        else:
            Element("ergebnis").element.innerHTML += "Bitte für n eine natürliche Zahl kleiner gleich n eingeben.<br />" 
        
    
    if kumS:
        try:
            r1 = int(Element("r1").value)
        except:
            Element("ergebnis").element.innerHTML += "Bitte für r1 eine natürliche Zahl eingeben.<br />"
        else:
            x2+=1

        try:
            r2 = int(Element("r2").value)
        except:
            Element("ergebnis").element.innerHTML += "Bitte für r2 eine natürliche Zahl eingeben.<br />"
        else:
            x2+=1
        
        if r1>r2:
            Element("ergebnis").element.innerHTML += "Bitte für r2 eine natürliche Zahl größer r1 eingeben.<br />"
        else:
            x2+=1
        if (r1>n) or (r2>n):
            Element("ergebnis").element.innerHTML += "Bitte für r2 und r1 eine natürliche Zahl kleiner n eingeben.<br />"
        else:
            x2+=1
    
    if (x1 == 3) and (kum):
        if inv:
            Element("ergebnis").element.innerHTML += "1-P("+str(r)+" ≤ X)="+str(1-f(n,p,r))
        else:
            Element("ergebnis").element.innerHTML += "P("+str(r)+" ≤ X)="+str(f(n,p,r))
    
    if (x1 == 3) and not (kum):
        if inv:
            Element("ergebnis").element.innerHTML += "1-P("+str(r)+" ≤ X)="+str(1-b(n,p,r))
        else:
            Element("ergebnis").element.innerHTML += "P("+str(r)+" ≤ X)="+str(b(n,p,r))

    if x2 == 6:
        if inv:
            Element("ergebnis").element.innerHTML += "1-P("+str(r1)+" ≤ X ≤ "+str(r2)+")="+str(1-fdiff(n,p,r1,r2))
        else:
            Element("ergebnis").element.innerHTML += "P("+str(r1)+" ≤ X ≤ "+str(r2)+")="+str(fdiff(n,p,r1,r2))
