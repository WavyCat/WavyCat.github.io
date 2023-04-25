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

def hidclick1():
    if js.document.querySelector("#k").checked:
        Element("containsr").remove_class("hidden")
        Element("containsr2").add_class("hidden")
        Element("containsbox2").remove_class("hidden")
        Element("containsbox3").add_class("hidden")
        Element("containsbox4").add_class("hidden")
    else:
        Element("containsbox2").remove_class("hidden")
        Element("containsbox3").remove_class("hidden")
        Element("containsbox4").remove_class("hidden")

def hidclick2():
    if js.document.querySelector("#kS").checked:
        Element("containsr").remove_class("hidden")
        Element("containsr2").remove_class("hidden")
    else:
        Element("containsbox1").remove_class("hidden")
        Element("containsbox2").remove_class("hidden")
        Element("containsbox4").remove_class("hidden")

def hidclick3():
    if js.document.querySelector("#sigI").checked:
        Element("containsr").add_class("hidden")
        Element("containsr2").add_class("hidden")
        Element("containsbox1").add_class("hidden")
        Element("containsbox2").add_class("hidden")
        Element("containsbox3").add_class("hidden")
    else:
        Element("containsr").remove_class("hidden")
        Element("containsbox1").remove_class("hidden")
        Element("containsbox2").remove_class("hidden")
        Element("containsbox3").remove_class("hidden")

    


def hidclick2():
    Element("containsr2").remove_class("hidden")

def rechnen():
    #Alle drei Checkboxen(kumuliert, invertiert, und kumuliert Differenz, SigmaInterval) werden in Variablen gespeichert
    inv = js.document.querySelector("#v").checked
    kum = js.document.querySelector("#k").checked
    kumS = js.document.querySelector("#kS").checked 
    sigI = js.document.querySelector("#sigI").checked
    
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
        r1 = int(Element("r1").value)
    except:
        Element("ergebnis").element.innerHTML += "Bitte für r1 eine natürliche Zahl eingeben.<br />"
    else:
        if x1 == 2:
            if n>=r1:
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
            if (x1!=0) and ((r1>n) or (r2>n)):
                Element("ergebnis").element.innerHTML += "Bitte für r2 und r1 eine natürliche Zahl kleiner n eingeben.<br />"
            else:
                x2+=1
    
    if (x1 == 3) and (kum):
        if inv:
            Element("ergebnis").element.innerHTML += "1-P("+str(r1)+" ≤ X)="+str(round((1-f(n,p,r1))*100,4))+"%<br />"
        else:
            Element("ergebnis").element.innerHTML += "P("+str(r1)+" ≤ X)="+str(round(f(n,p,r1)*100,4))+"%<br />"
    
    if (x1 == 3) and not (kum):
        if inv:
            Element("ergebnis").element.innerHTML += "1-P("+str(r1)+" ≤ X)="+str(round((1-b(n,p,r1))*100,4))+"%<br />"
        else:
            Element("ergebnis").element.innerHTML += "P("+str(r1)+" ≤ X)="+str(round(b(n,p,r1)*100,4))+"%<br />"

    if x2 == 6:
        if inv:
            Element("ergebnis").element.innerHTML += "1-P("+str(r1)+" ≤ X ≤ "+str(r2)+")="+str(round((1-fdiff(n,p,r1,r2))*100,4))+"%<br />"
        else:
            Element("ergebnis").element.innerHTML += "P("+str(r1)+" ≤ X ≤ "+str(r2)+")="+str(round(fdiff(n,p,r1,r2)*100,4))+"%<br />"

    if x1 >= 2:
        if sigI:
            Element("ergebnis").element.innerHTML += "P<sub>σ</sub>="+str(round(sigmaP(1,n,p)*100,4))+"%<br />"
            Element("ergebnis").element.innerHTML += "P<sub>2σ</sub>="+str(round(sigmaP(2,n,p)*100,4))+"%<br />"
            Element("ergebnis").element.innerHTML += "P<sub>3σ</sub>="+str(round(sigmaP(3,n,p)*100,4))+"%<br />"
            Element("ergebnis").element.innerHTML += "P<sub>1.64σ</sub>="+str(round(sigmaP(1.64,n,p)*100,4))+"%<br />"
            Element("ergebnis").element.innerHTML += "P<sub>1.96σ</sub>="+str(round(sigmaP(1.96,n,p)*100,4))+"%<br />"
            Element("ergebnis").element.innerHTML += "P<sub>2.58σ</sub>="+str(round(sigmaP(2.58,n,p)*100,4))+"%<br />"
