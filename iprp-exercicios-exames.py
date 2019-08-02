import turtle
import math
import random


def troca(pal):
    pares = pal[::2]
    impares = pal[1::2]
    nova = ''
    for i in range(len(pal)//2):
        nova += impares[i] + pares[i]
    if len(pal) % 2 != 0:
        nova += pares[-1]
    print nova


# zen
def zen1(raio):
    #circulo grande
    turtle.setheading(90)
    turtle.circle(raio)

    # divisao
    turtle.circle(raio/2,-180)
    # meio
    turtle.setheading(90)
    turtle.circle(raio/2,180)

    turtle.exitonclick()

# teste final 2015/16
def processa(cad):
    lista = []
    for i in range(len(cad)):
        lista.append((cad[i],i,0))
        if i != 0 and lista[-2][0] == lista[-1][0]:
            lista[-2] = (lista[-2][0], lista[-2][1], lista[-2][2] + 1)
            lista.pop(-1)

    print(lista)

#processa('x22ddd cbba')

# exercio 3
dicio_twitter = {"maria":["joao","beatriz","constanca"], "renato":["carolina"], "beatriz":["renato","maria"], "carolina":["renato", "maria"]}

def mais_seguidores(dicio):
    max = 0
    user = ""
    for k,v in dicio.items():
        if len(v) > max:
            max = len(v)
            user = k

    print (k)
#mais_seguidores(dicio_twitter)

# ex 4
def casais(ficheiro,dif):
    f_in = open(ficheiro,"r")
    f_out = open("casais.txt","w")

    # separar homens de mulheres
    m = []
    f = []
    for pessoa in f_in.readlines():
        #print(pessoa.split())
        if (pessoa.split()[1] == 'F'):
            f.append((pessoa.split()[0], pessoa.split()[2]))
        else:
            m.append((pessoa.split()[0], pessoa.split()[2]))

    #juntar casais
    l = []
    for homem in m:
        for mulher in f:
            #print(homem[1])
            if ( abs(int(homem[1])) - (int(mulher[1])) <= dif):
                l.append( (homem[0] + " + " + mulher[0] + " -- " + str( abs(int(homem[1]) - (int(mulher[1]))) )))
                f.remove(mulher)
                break

    print(l)
    #escreve ficheiro
    for i in l:
        f_out.write(i + "\n")

    f_in.close()
    f_out.close()

#casais("pessoas.txt",3)

def xpto(lista):
    for i in range(len(lista)):
        m = max(lista[i:])
        ind = lista.index(m)
        lista[i], lista[ind] = lista[ind], lista[i]
    return lista

#print(xpto([4,30,2,10,21]))

# recurso

def vai_para(posx,posy):
    turtle.pu()
    turtle.goto(posx,posy)
    turtle.pd()

def triangulo(lado):

    for i in range(3):
        turtle.fd(lado)
        turtle.lt(120)

    #turtle.exitonclick()

#triangulo(50)

def n_triangulos(lado,n):

    for i in range(n):
        turtle.fd(lado)
        turtle.rt(360/n)

        triangulo(lado)

    turtle.exitonclick()

#n_triangulos(100,4)

def gera_cadeira():
    lista = [("2", 1, 1), ("a", 10, 0), ("x", 0, 0), ("d", 3, 2), (" ", 6, 0), ("c", 7, 0), ("b", 8, 1)]

    cadeia = ""
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if (lista[j][1] > lista[j+1][1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]


    print(lista)

    for i in range(len(lista)):
        cadeia += (str(lista[i][0]) * (lista[i][2]+1) )

    print(cadeia)
#gera_cadeira()

def desenha_triangulo(base,comp):
    turtle.fd(base)
    turtle.lt(105)

    turtle.fd(comp)
    turtle.lt(150)

    turtle.fd(comp)
    turtle.lt(105)

def caminho_ferro(base, comp, nr_trav):
    vai_para(0,0)
    #desenha_triangulo(base,comp)

    h = math.sqrt(comp**2 - (base/2)**2)

    for i in range(nr_trav):
        turtle.setheading(turtle.towards(-base/2,-h))
        turtle.fd( (comp/nr_trav) * i)
        turtle.goto(-turtle.position()[0], turtle.position()[1])
        turtle.goto(0,0)

    turtle.hideturtle()
    turtle.exitonclick()

#caminho_ferro(100,200,10)

def conta_subCadeia(subcad, cad):
    soma = 0

    tam = len(cad) - len(subcad)
    for i in range(tam):
        #print(cad[:i])
        if(cad[i: i + len(subcad) ] == subcad):
            soma += 1

    return soma

#print(conta_subCadeia("lal","olalal mundo"))

def soma_esparsos():
    d1 = {3:5, 6:2, 'len':7}
    d2 = {1:2, 3:4, 5:3, 'len':7}

    dicio = {}

    l1 = []
    l2 = []
    soma = []

    for c,v in d1.items():
        #l1.append(0)
        #l1 *= v
        if(c == "len"):
            l1 = [0] * v
            continue

    #print(l1)

    for c,v in d1.items():
        for i in range(len(l1)):
            #print(c)
            #print(i)
            #l1[c] = v
            if c != "len":
                l1[c] = v

    for c,v in d2.items():
        #l1.append(0)
        #l1 *= v
        if(c == "len"):
            l2 = [0] * v
            continue

    #print(l1)

    for c,v in d2.items():
        for i in range(len(l2)):
            #print(c)
            #print(i)
            #l1[c] = v
            if c != "len":
                l2[c] = v

    # soma
    for i in range(len(l1)): # teem a mesma dimensao
        soma.append(l1[i] + l2[i])


    # transformar em dicionario
    """
    for c,v in dicio.items():
        for i in range(len(soma)):
            if soma[i] != 0:
                dicio.setdefault(c,i)
                
        dicio["len"] = len(soma)
    """

    for i in range(len(soma)):
        if soma[i] != 0:
            dicio[i] = soma[i]
        dicio["len"] = len(soma)

    print(l1)
    print(l2)
    print(soma)

    print(dicio)

#soma_esparsos()


def soma_vetores(fich):
    f = open(fich,"r")
    soma = []
    lists = []
    n_vetores = 0

    linhas = f.readlines()

    for i in linhas:
        n_vetores += 1

    #for i in range(n_vetores):
    #    lists.append([])


    for v in linhas:
        #print(linha)
        vetor = v.strip().split(",")
        print(vetor)
        lists.append(vetor)

    print(lists)


    #print(soma)
    for i in range(len(lists[0])):
        temp = 0
        for j in range(len(lists)):
            #print(lists[i][j])
            temp = temp + int(lists[j][i])
        soma.append(temp)

    print(soma)

    dicio ={}
    for i in range(len(soma)):
        if(soma[i] != 0):
            dicio[i] = soma[i]
        dicio["len"] = len(soma)

    print(dicio)

#soma_vetores("vetores.txt")

def alvo(raio):
    turtle.speed(0)
    for i in range(5,0,-1):
        vai_para(0,-(raio/4)*i)

        if (i%2 == 0):
            turtle.color("black")
            turtle.begin_fill()
            turtle.circle((raio/4) *i)
            turtle.end_fill()
        else:
            turtle.color("white")
            turtle.begin_fill()
            turtle.circle((raio / 4) * i)
            turtle.end_fill()

    posx = random.randint(-raio, raio)
    posy = random.randint(-raio, raio)

    vai_para(posx, posy)
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

    turtle.ht()
    turtle.exitonclick()

#alvo(100)

def melhor_filme(atualiza):
    films = {"X": [3, 2, 5],"Y": [1, 3],"Z":[2, 2, 4, 1]}

    #adiciona
    for c, v in films.items():
        if(c == atualiza[0]):
            films[c] = v + atualiza[1:]
        films[atualiza[0]] = atualiza[1:]
        #if(c != atualiza[0]):
        #    films[atualiza[0]] = atualiza[1:]

        #media
        #films[c] = sum(v[0:])/len(v)

    # media
    for c,v in films.items():
        media = float(float(sum(v))/len(v))
        #print(media)
        films[c] = media

    # melhor filme
    max = 0
    tmp = ""
    for c,v in films.items():
        if v > max:
            max = v
            tmp = c

    print(tmp)
    print(films)

    #print(films)

#melhor_filme(["W",5,5,4])
from operator import itemgetter
def soma_numeros(ficheiro, ficheiro_saida):
    f_in = open(ficheiro,"r")
    f_out = open(ficheiro_saida,"w")

    l = []
    soma = 0
    for linha in f_in.readlines():
        #print(linha)
        pessoa = linha.strip().split()

        l.append(pessoa)

    for i in range(0,len(l)):
        l[i][1:] = map(int,l[i][1:])
        soma = sum(l[i][1:])
        #print(soma)
        l[i].append(soma)

    # ordenar
    for i in range(len(l)):
        for j in range(len(l) -1 ):
            if(l[j][-1] > l[j+1][-1]):
                l[j],l[j+1] = l[j+1],l[j]

    print(l)

    # escrever ficheiro

    for i in l:
        f_out.write(str(i) + "\n")

    f_in.close()
    f_out.close()

#soma_numeros("ordena_nrs.txt", "ordenado.txt")

def palavras (w1 , w2):
    dif = len (w1) - len (w2)
    if dif > 0:
        w2 = w2 + dif * " "
    else :
        w1 = w1 + (- dif ) * " "
    for i in range (len(w1)):
        print (w1[i], w2[i])
#palavras("Epoca","Normal")

def jaccard(l1,l2):
    interseta = 0.0
    total = 0.0
    for i in range(len(l1)):
        for j in range(len(l2)):
            #print(l1[i],l2[j])
            if l1[i] == l2[j]:
                interseta +=1.0

    dif = len(l1) - len(l2)

    for i in l1:
        if (i not in l2):
            total+=1
        else:
            total+=1

    for j in l2:
        if j not in l1:
            total+=1

    print(total)
    return float(interseta/total)

#print(jaccard([1,2,3,4],[2,3,5]))

# ex 3 - 2013

receitas ={"sonhos":["agua","farinha","manteiga","ovos","acucar"],
"rabanadas":[ "pao","leite","ovos","manteiga","acucar"],"leite creme":["acucar","farinha","ovos","leite"]}

def ingredientes_mais_usados(receitas):

    # ingredientes
    lista = []

    for i in receitas:
        for j in receitas[i]:
            if j not in lista:
                lista.append(j)
    print(lista)

    mais_usados = []
    for ingrediente in lista:
        conta = 0
        for c,v in receitas.items():
            if ingrediente in v:
                conta+=1
        #print(conta)
        if conta == len(receitas):
            mais_usados.append(ingrediente)
        #print(conta)
    print(mais_usados)

    dicio = {}
    for ingrediente in mais_usados:
        for c,v in receitas.items():
            if ingrediente in v:
                if dicio.get(ingrediente) is not None:
                    dicio[ingrediente].append(c)
                else:
                    dicio[ingrediente] = [c]

    print(dicio)
#print(ingredientes_mais_usados(receitas))

def horario_salas(ficheiro):
    f_in = open(ficheiro,"r")

    #aulas = []
    dicio = {}
    for linha in f_in.readlines():
        aula = linha.strip().split()
        #aulas.append(aula)
        sala = aula[-1]

        if (dicio.get(sala)) is None:
            dicio[sala] = aula
        else:
            dicio[sala].append(aula)

        #print(dicio[sala][-1])
        #dicio[sala][-1].pop(-1)

    print(dicio)
    """
    print(aulas)
    
    dicio = {}
    for i in range(len(aulas)):
        sala = aulas[i][-1]
        print(sala)
        print(aulas[i])
        if ( sala in aulas[i] ):

            dicio[sala] = aulas[i]
        aulas[i].pop(-1)

    print(dicio)
    """

    f_out = open("horarios.txt","w")
    for c,v in dicio.items():
        f_out.write("Horario da sala: " + str(c) + "\n" )
        for v in dicio.values():
            f_out.write(str(v[0]) + " " + str(v[1]) + " " + str(v[2]) + " " + str(v[3]) + " " + str(v[4]) + "\n")

    f_in.close()
    f_out.close()
#horario_salas("aulas.txt")

def triangulo_equilatero(lado):

    for i in range(3):
        turtle.fd(lado)
        turtle.lt(180-60)
    #turtle.exitonclick()

#triangulo_equilatero(50)

def triangulo_voltas(n,lado):

    for i in range(n):
        turtle.fd(lado)
        turtle.rt(360/n)
        triangulo_equilatero(lado)

    turtle.ht()
    turtle.exitonclick()
#triangulo_voltas(10,100)

def gerar_cadeia(lista):

    cad = ""
    #ordena lista
    for i in range(len(lista)):
        #print(lista[i][0])
        for j in range(len(lista)):
            if (lista[i][1] < lista[j][1]):
                lista[i], lista[j] = lista[j], lista[i]

    print(lista)
    for i in range(len(lista)):
        cad += lista[i][0] * (lista[i][2] + 1)

    print(cad)

#gerar_cadeia([("2", 1, 1), ("a", 10, 0), ("x", 0, 0), ("d", 3, 2), (" ", 6, 0), ("c", 7, 0), ("b", 8, 1)])

rede = {"tiago": ["rita", "francisco", "joao", "filipa"], "joao":
    ["tiago", "ricardo"], "ricardo":["rita", "francisco"], "rita": ["tiago"
, "filipa", "ricardo"], "filipa":[], "francisco": ["tiago"]}

def sugestoes(user,rede,n):

    following = []
    notfollowing = []

    conta = 0
    sugestao = []
    seguidores = []
    for c,v in rede.items():
        if user == c:
            #print(seguindo)
            #print(len(v))
            for i in range(len(v)):
                #print(v[i])
                following.append(v[i])
        else:
            for i in range(len(v)):
                if v[i] not in following:
                    notfollowing.append(v[i])

        for i in range(n):
            if(following[i] == c):
                sugestao.append(v[i])

    #print(following)
    #print(notfollowing)
    return sugestao

#print(sugestoes("joao",rede,2))

# ex 5

from operator import itemgetter

def top5(ficheiro):
    f = open(ficheiro,"r")

    prova = []

    for linha in f.readlines():
        atleta = linha.strip().split(" ")
        prova.append(atleta)

        #print(prova)

    for i in range(len(prova)):
        tempo = prova[i][2].split(":")
        #print(tempo)
        prova[i].pop(-1) # apagar tempo
        for j in range(len(tempo)):
            #tempo[j] = map(int,tempo[j])
            #print(tempo[j])
            prova[i].append(int(tempo[j]))

    #print(prova)

    #ordenar por segundo
    prova.sort( key = lambda prova: prova[4])

    #ordenar por minuto
    prova.sort( key = lambda prova: prova[3])

    #ordenar por hora
    prova.sort( key = lambda prova: prova[2])

    print(prova)

    best = []
    for i in range(len(prova)):
        best.append(prova[i][2:])
        dif = prova[i][4] - prova[0][4]
        prova[i].append(dif)
    print(best)
    print(prova)


    f_out = open("resultados.txt","w")
    for i in range(5): # top 5
        #print(prova[i][5])
        f_out.write(str(i+1) + " " + str(prova[i][0]) + " " + "-" + str(prova[i][5]) + "\n")

    f.close()

#top5("tempos_prova.txt")

twitter = {"maria":["joao","beatriz","constanca","renato"], "renato":["carolina","beatriz","mariana"], "beatriz":["renato","maria"], "carolina":["renato", "maria"]}

def more_followers(twitter):

    dicio = {}
    for c,v in twitter.items():
        conta = 0
        for v in twitter.values():
            if(c in v):
                conta+=1
                dicio[c] = conta
    print(dicio)

    max = 0
    user = ""
    pessoas=[]
    for c,v in dicio.items():
        if(v > max):
            max = v
            user = c
            #pessoas.append(c)
    #print(pessoas)
    #for i in range(len(pessoas)):
    #    user += pessoas[i]
    print(user)

    """
    ou
    ###
    max = 0
    user = ""
    for k,v in dicio.items():
        if len(v) > max:
            max = len(v)
            user = k

    print (k)
    """

#more_followers(twitter)

def comprar_vender(lista):
    l = []

    for i in range(len(lista)):
        if (len(lista[:i]) > 0):
            media = sum(lista[:i])/len(lista[:i])
            if( lista[i] < media):
                l.append("c")
            else:
                l.append("v")
        else:
            l.append("v")
    print(l)

#comprar_vender ([3, 4, 5, 7, 3, 5, 10, 13, 5, 7])

def gerar_casais(fich, fich_out, dif):
    ficheiro = open(fich,"r")

    f = []
    m = []
    for linha in ficheiro.readlines():
        pessoa = linha.strip().split()
        if(pessoa[1] == "F"):
            f.append(pessoa)
        else:
            m.append(pessoa)

    print(f)
    print(m)

    fich_out = open(fich_out,"w")
    #casais = []
    for i in range(len(f)):
        dif_idade = abs( int(m[i][2]) - int(f[i][2]))
        if(dif_idade <= dif):
            fich_out.write(str(m[i][0]) + " " + str(f[i][0]) + " " + "-" + str(dif_idade) + "\n")

    ficheiro.close()
    fich_out.close()

#gerar_casais("pessoas.txt","casados.txt",2)
#casais("pessoas.txt",10)


texto = "O Tempo perguntou ao tempo quanto tempo o tempo tem o Tempo respondeu ao tempo que o tempo tem tanto tempo quanto tempo tempo tem"

def conta_palavras(fich,texto):

    dicio = {}
    conta = 0
    pal = texto.lower().split()

    for word in pal:
        if word not in dicio:
            dicio[word] = 1
        else:
            dicio[word] +=1
    #print(pal)
    print(dicio)
    f = open(fich,"w")

    for c,v in dicio.items():
        f.write(str(c) + "," + str(v) + "\n")

    f.close()
#conta_palavras("palavras.txt",texto)


# exame especial 2019

def vai_para(px,py):
    turtle.pu()
    turtle.goto(px,py)
    turtle.pd()

def circulo(cor,raio):
    turtle.color(cor)
    turtle.begin_fill()
    turtle.circle(raio)
    turtle.end_fill()

def alvo(cor1,cor2,raio,n,posx,posy):
    vai_para(posx,posy)

    for i in range(n,0,-1):
        vai_para(posx, -(raio/n)*i)
        if(i%2 == 0):
            circulo(cor1, (raio/n)*i)
        else:
            circulo(cor2, (raio/n)*i)

    turtle.exitonclick()

#alvo("red","black",100,4,0,0)


def pal_rep():
    frase = "ola tudo tudo bem contigo e tu tu ne"

    pal = frase.split()

    lista = []

    for i in range(len(pal)):
        if(pal[i] not in lista):
            lista.append(pal[i])

    nova = ""
    for i in range(len(lista)):
        nova += str(lista[i]) + " "

    return nova
#print(pal_rep())

def biblioteca(fich_out):
    f = open("livros.txt","r")
    dicio = {}
    for linha in f.readlines():
        livro = linha.strip().split()
        ano = 0
        nome = ""
        autor = ""
        autor = livro[1:3]

        if(len(livro) == 7):
            nome = livro[3:6]
            ano = int(livro[6])
        if (len(livro) == 6):
            nome = livro[3:5]
            ano = int(livro[5])
        if (len(livro) == 5):
            nome = livro[3]
            ano = int(livro[4])

        dicio[livro[0]] = autor
        dicio[livro[0]].append(nome)
        dicio[livro[0]].append(ano)

    print(dicio)
    autores = []
    novo_dicio = {}

    #conta = 0
    for c,v in dicio.items():
        conta = 0
        if(v[0] not in autores):
            autores.append(v[0])
            conta+=1
            novo_dicio[v[0]] = conta
            #novo_dicio[v[0]] += int(1)
        else:
            conta+=1
            #novo_dicio[v[0]] += 1
            novo_dicio[v[0]] += conta

    f_out = open(fich_out,"w")
    for c,v in novo_dicio.items():
        f_out.write(str(c) + " " + str(v) + "\n")

    #print(novo_dicio)

    f.close()
    f_out.close()
biblioteca("autores.txt")