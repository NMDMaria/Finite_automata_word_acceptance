"""
Fisierul de intrare de forma:
        N
        s1 s2 s3 ... sN
        M
        t1
        t2
        ...
        tM  --- cu t de forma : stare stareUndeAjung litera
        S
        nrF
        f1 f2 f3 ... fnrF
        nrCuv
        c1
        c2
        ...
        cnrCuv

Fisierul de iesire de forma:
        DA/NU
        DA/NU
        ...
        DA/NU
        --- de nrCuv ori
Fisierul suplimentar "succesiune.out" de forma:
        cuv1
        succesiune1_1 succesiune1_2 ... succesiune1_n
        ...
        succesiuneM_1 succesiuneM_2 ... succesiuneM_n
        cuv2
        ...
        ...
"""


def verificare(cuv): # teoretic merge cu 'lamda' -> trebuie testata
    def parcurgere(stare, i):
        global solutie, last_tranzitie
        for tranzitie in stari[stare]:
            if tranzitie[1] == cuv[i]:
                if i == len(cuv) - 1:
                    if tranzitie[0] in F:
                        solutie = solutie + 1
                else:
                    parcurgere(tranzitie[0], i + 1)
            elif tranzitie[1] == 'lamda' and last_tranzitie != (stare, tranzitie[0], tranzitie[1]):
                last_tranzitie = (stare, tranzitie[0], tranzitie[1])
                if i == len(cuv) - 1:
                    if tranzitie[0] in F:
                        solutie = solutie + 1
                    else:
                        parcurgere(tranzitie[0], i)


    global S, F, stari, solutie, last_tranzitie
    solutie = 0
    last_tranzitie = (-1, -1, -1) # 0 = de unde 1 = unde 2 = litera
    if cuv == "":
        if S in F:
            solutie = solutie + 1
    else:
        parcurgere(S, 0)
    return solutie


f = open("date.in", 'r')
g = open("date.out", 'w')
"""
"succesiune.out" = fisier suplimentar unde afisez ordinea succesiunilor de noduri/stari a solutiilor

stari = dictionar cu key: nod/stare, items: lista cu tranzitiile - tuple -  care pleaca din key
aux = ajutor pentru citirea din fisier
N, M, S, nrF, F, nrCuv cu semnificatiile date

Citesc N. Citesc pe rand valorile nodurilor/starilor si le memorez ca si key in "stari" -> nu este nevoie ca starile sa fie consecutive, nu ocup memorie inutil
Citesc M. Citesc pe rand fiecare tranzitie si o adaug la key-ul care trebuie. 
    - tranzitiile se memoreaza in tuple cu 0: nodul unde duce tranzitia, 1: litera tranzitiei
Citesc S.
Citesc nrF. Citesc pe rand starile finale.
Citesc nrCuv. Citesc pe rand fiecare cuvant.
    Pentru fiecare cuvant:
        - apelez functia de verificare ce returneaza numarul de solutii
        - daca am cel putin o solutie afisez in "date.out" - "DA", altfel afisez - "NU"
        Suplimentar:
            - daca am cel putin o solutie afisez in "succesiune.out" cuvantul, urmat de fiecare succesiune de noduri ce duce la procesarea cuvantului 

"""
stari = {}
N = int(f.readline().strip())
aux = f.readline().strip().split()
for i in range(N):
    stari.update({int(aux[i]): []})
M = int(f.readline().strip())
for i in range(M):
    aux = f.readline().strip().split()
    t = (int(aux[1]), aux[2])
    stari[int(aux[0])].append(t)
S = int(f.readline().strip())
nrF = int(f.readline().strip())
F = []
aux = f.readline().strip().split()
for i in range(nrF):
    F.append(int(aux[i]))
nrCuv = int(f.readline().strip())
for i in range(nrCuv):
    cuv = f.readline().strip()
    sol = verificare(cuv)
    global solutie_stari
    if sol > 0:
        g.write("DA\n")
    else:
        g.write("NU\n")
