---This is a rough draft to undergo documentation in the near future---

Xmat = (m,n) ->(
    rowIndex = for i from 1 to m list i;
    colIndex = for j from 1 to n list j;
    M = for i in rowIndex list apply(colIndex, j-> x_(i,j));
    return M
)

X = (m,n) ->(
    return flatten(Xmat(m,n)) -- need these to be order just like this
)

Y = (n) ->(
    return for j from 1 to n list y_j
)

R = (m,n) ->(
    Xvar = X(m,n);
    Yvar = Y(n);
    return QQ[Yvar,Xvar, MonomialOrder => Lex] --- In this order for the desired ordering of monomials
)

residualIdeal = (m,n) ->(
    S = R(m,n);
    MX = matrix(Xmat(m,n));
    I = minors(n,MX);
    rowIndex = for i from 1 to m list i;
    colIndex = for j from 1 to n list j;
    Jset = for i in rowIndex list sum(apply(colIndex, j-> y_j*x_(i,j)));
    J = ideal(Jset);
    return I + J
)

residualPres = (m,n) -> (
    J = residualIdeal(m,n);
    Jgens = flatten entries gens J;
    preHash = for i from 1 to #Jgens list (w_i => Jgens # (i-1));
    WHash = new HashTable from preHash;
    Wvars = keys WHash;
    Wdegrees = for w in Wvars list degree(WHash#w);
    U = QQ[Wvars, Degrees => Wdegrees];
    Wmap = for w in Wvars list WHash#w;
    psi = map(S,U, matrix{Wmap});
    return U/ker(psi)
)



initSet = (m,n) -> (
    K = residualIdeal(m,n);
    Kgen = flatten entries gens K;
    return for x in Kgen list leadTerm(x)
)

initPres = (m,n) -> (
    Kinit = initSet(m,n);
    preHash = for i from 1 to #Kinit list (z_i => Kinit # (i-1));
    ZHash = new HashTable from preHash;
    Zvars = keys ZHash;
    Zdegrees = for z in Zvars list degree(ZHash#z);
    T = QQ[Zvars, Degrees => Zdegrees];
    Zmap = for z in Zvars list ZHash#z;
    phi = map(S,T, matrix{Zmap});
    return T/ker(phi)
)



