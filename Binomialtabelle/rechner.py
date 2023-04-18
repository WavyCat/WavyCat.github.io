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
    n = int(Element("n").value)
    p = float(Element("p").value)
    r = int(Element("r").value)
    k = js.document.querySelector("#k").checked

    if k:
        Element("ergebnis").write($$\begin{multline*}
{\hspace{1cm}} P(X \leqslant r) = \sum_{i=0}^r \binom{n}{i} p^i (1-p)^{n-i} \\
Fig.1
\end{multline*}
$$)
