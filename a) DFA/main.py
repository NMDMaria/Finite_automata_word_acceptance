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

# from collections import namedtuple
# tranzitie = namedtuple("tranzitie", "unde caracter")
#
# """
# Folosind namedtuple creez un tuplu unde:
#     tranzitie[0] -> unde
#     tranzitie[1] -> caracter
# Ceea ce ar echivala oarecum "class tranzitie" din c++.
# Diferenta dintre namedtuple si tuple normal tine de afisare:
#     - tuple normal: (var1, var2, ...)
#     - namedtuple: name("nume_var1"=var1, "nume_var2"=var2, ...)
# Folosirea namedtuple nu este necesară pentru functionarea programului. Fiecare "tranzitie" poate fi inlocuita cu "tuple" si programul ar functiona la fel.
# Pentru fiecare namedtuple este o versiune comentată cu declararea tuple normal, daca se decomenteaza versiunea normala si se comenteaza cea named programul functioneaza la fel, fara a folosi librarii suplimentare.
# """


def verificare(cuv):
    def parcurgere(stare, i, succesiune, solutie_stari):
        """
        :param stare: nodul/starea curenta din proccesare
        :param i: indexul la care ne aflam in cuvantul de verificat
        :param succesiune: lista cu nodurile/starile procesate (corect pt. cuvant) pana acum
        :param solutie_stari: lista cu succesiunile de noduri care dau solutie
        Functie recursiva.

        - verific daca am ajuns la o stare a automatului (nu trebuie neaparat pentru ca nu ies niciodata din starile automatului)
        - trec prin fiecare tranzitie care pleaca din "stare" :
                - daca litera tranzitiei este la indexul cautat (i) in cuvant:
                            - adaug "stare" in "succesiune"
                            - daca i este chiar ultima litera din cuvantul verificat: -> nu mai fac alt apel, deci nu pot depasi niciodata numarul de litere din cuvant
                                    - verific daca starea/nodul in care ajung prin tranzitie este in F
                                            => daca este o adaug la "succesiune", cresc numarul de solutii si adaug la "solutie_stari" succesiunea curenta
                                            - sterg starea/nodul adaugat din succesiune (pt. a ma asigura ca la un alt apel al functiei nu am acest nod ca si parcurs)
                            - altfel -> nu am depasit numarul de litere din cuvant
                                    - apelez parcurgere(starea unde m-a dus tranzitia procesata, i + 1 -> caut alta litera, "succesiune", "solutie_stari")
                            - scot "stare" din "succesiune" (pt. a ma asigura ca la un alt apel al functiei nu am acest nod ca si parcurs - ceea ce ar fi ernoat)
        """
        global solutie

        if stare in stari:
            for t in stari[stare]:
                if t[1] == cuv[i]:
                    succesiune.append(stare)
                    if i == len(cuv) - 1:
                        if t[0] in F:
                            succesiune.append(t[0])
                            solutie = solutie + 1
                            solutie_stari.append([i for i in succesiune])
                            succesiune.pop(len(succesiune) - 1)
                    else:
                        parcurgere(t[0], i + 1, succesiune, solutie_stari)
                    succesiune.pop(len(succesiune) - 1)

    global S, F, stari, solutie, solutie_stari
    """
        Functia ce initiaza parcurgerea automatului/grafului.
        solutie = nr. de procesari ce produc cuvantul dat
        solutie_stari = lista unde avem cate o lista cu noduri/stari pentru fiecare procesare ce a dat solutie
        
        Apelam functia de parcurgere cu nodul/stare initiala, o lista goala pentru a memora succesiunea de noduri din parcurgere si solutie_stari.
        Returnam numarul de solutii. 
    """
    solutie = 0
    solutie_stari = []
    if cuv == "":
        if S in F:
            solutie_stari.append([S])
            solutie = solutie + 1
    else:
        parcurgere(S, 0, [], solutie_stari)
    return solutie


f = open("date.in", 'r')
g = open("date.out", 'w')
op = open("succesiune.out", 'w')
"""
op = fisier suplimentar unde afisez ordinea succesiunilor de noduri/stari a solutiilor
"""

"""
stari = dictionar cu key: nod/stare, items: lista cu tranzitiile care pleaca din key
aux = ajutor pentru citirea din fisier
N, M, S, nrF, F, nrCuv cu semnificatiile date

Presupun ca automatul citit chiar este un DFA / datele de intrare sunt corecte. 

Citesc N. Citesc pe rand valorile nodurilor/starilor si le memorez ca si key in "stari" -> nu este nevoie ca starile sa fie consecutive, nu ocup memorie inutil
Citesc M. Citesc pe rand fiecare tranzitie si o adaug la key-ul care trebuie.
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
        op.write(cuv)
        op.write("\n")
        for k in range(len(solutie_stari)):
            for i in solutie_stari[k]:
                op.write(str(i))
                op.write(' ')
            op.write("\n")
    else:
        g.write("NU\n")