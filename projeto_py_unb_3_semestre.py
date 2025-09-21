time = []
jogador = ['x', 'y', 'z']
posicoes = ['goleiro', 'defensor', 'meia' , 'atacante']
numeros = ['0','1','2','3','4','5','6','7','8','9']
contador_time= 0
Esquema_Tatico = 0




goleiro =[]
defensores =[] 
meias =[]
atacantes  =[]  

def CONTRATAR_JOGADORES(x):
    print()
    print("Entre com: nome posicao(atacante-meia-defensor-goleiro)  habilidade(0-10)")
    jogador = input().split()   
    if len(jogador) != 3:
        pass
    else:
        #Ex.: “Ronaldo” = “ronaldo” = “roNalDO”
        #colocar condição
        jogador[0] = jogador[0].lower()
        
        for i in range(len(time)):
            if time[i][0] == jogador[0]:
                print("Jogador já está no time")
                return 
            
        if jogador[0] in time:
            print("Jogador já está no time")
            return 
        
        else:
            #Caso o nome do jogador seja menor que 8 caracteres, seu nome deve ser cortado para que contenha apenas 8 caracteres.
            if len(jogador[0]) < 8:
                for i in jogador[0]:
                    if i in numeros:
                        return 
                
                if jogador[1] in posicoes:
                    
                    if 10 >= int(jogador[2]) >= 0 :
                        time.append(jogador)
                        return num

                    
                    else:
                        print('A habilidade do jogador deve estar entre 0 e 10')
                        return 
                
                else:
                    print('A posição informada não existe')
                    return 
            
            else:
                if jogador[0] not in time:
                    nome= ''
                    for i in jogador[0]:
                        if i in numeros:
                            return 

                        elif len(nome) < 8:
                            nome += i
                        else:
                            pass
                     
                    jogador[0] = nome
                
                if jogador[1] in posicoes:
                    
                    if 10 >= int(jogador[2]) >= 0 :
                        time.append(jogador)
                        return num

                    
                    else:
                        print('A habilidade do jogador deve estar entre 0 e 10')
                        return 
                
                else:
                    print('A posição informada não existe')
                    return 
    
    
def TROCA_JOGADORES(num):
    print()
    print('Entre com jogador a ser trocado e jogador q ira entrar. (troca x entra) ')
    jogador1, jogador2 = input().split(' x ')
    
    jogador1 = jogador1.split()
    
    jogador2 = jogador2.split()
    contador = 0
    for i in range(len(time)):
        if jogador1[1] not in posicoes or jogador2[1] not in posicoes:
            print('A posição informada não existe')
            return
            
        else:
            
            if 10 >= int(jogador1[2]) >= 0 and 10 >= int(jogador2[2]) >= 0 :
                print(end='')
                if len(jogador1[0]) > 8:
                    jogador1[0] = jogador1[0].lower()

                    nome= ''
                    for i in jogador1[0]:
                        if i in numeros:
                            return 

                        elif len(nome) < 8:
                            nome += i
                        else:
                            pass
                    jogador1[0] = nome
                else:
                    for i in jogador1[0]:
                        if i in numeros:
                            return 
                     
                    
                if len(jogador2[0]) > 8:
                    jogador2[0] = jogador2[0].lower()

                    nome= ''
                    for i in jogador2[0]:
                        if i in numeros:
                            return 

                        elif len(nome) < 8:
                            nome += i
                        else:
                            pass
                 
                    jogador2[0] = nome
                else:
                    for i in jogador2[0]:
                        if i in numeros:
                            
                            return
                
            else:
                print('A habilidade do jogador deve estar entre 0 e 10')
                return
        
        

    

    
    
     # Trocar os jogadores
    for i in range(len(time)):
        dic = {}
        contador = 0
        for teste in time:
            dic.append(teste)
        

        if time[i][0] != jogador1[0] and time[i][0] != jogador2[0]:
            pass
        elif time[i][0] == jogador1[0] and time[i][0] != jogador2[0]:
            if  time[i][0] == jogador2[0]:
                    print("Jogador já está no time")
                    return
            elif time[i][0]!= jogador2[0]:
                    time[i] = jogador2
                    return
            else:
                if time[i][0] == jogador1[0] and time[i][0] == jogador2[0]:
                    print("Jogador já está no time")
                    return
        else:
            if time[i][0] != jogador1[0] and time[i][0] == jogador2[0]:
                print("Jogador não está no time")
                return
                
        
    print('Jogador não está no time')
    
    return
Esquema_Tatico = []
def Definir_Esquema_Tatico(num):
    print()
    print('Entre com o esquema tatico. (4 4 2 ou 4 3 3 ou 4 2 4 ou 3 4 3 ou 2 2 4 ou 2 3 5 ... : ')
    qtd_defensores, qtd_meias, qtd_atacantes = input().split()
    
    qtd_defensores = int(qtd_defensores)
    qtd_meias = int(qtd_meias)            
    qtd_atacantes = int(qtd_atacantes)
    
    if (2<= qtd_defensores <=4) and (2<= qtd_meias <=4) and (2<= qtd_atacantes <=4) :
        if (qtd_defensores + qtd_meias + qtd_atacantes) == 10:
            Esquema_Tatico.append(qtd_defensores)
            Esquema_Tatico.append(qtd_meias)
            Esquema_Tatico.append(qtd_atacantes)

         

            #print('usando', Esquema_Tatico)
        else:
            print('A soma das posições deve totalizar 10 jogadores')
            
                               
            return 
    else:
        print('Cada posição deve conter entre 2 e 4 jogadores')
        return
    


def Montar_o_Time(num):
    print()
    print('Montando Time! ')
    print(' ... ... ... ')
    if 3 == len(Esquema_Tatico) :
        
      
        
        qtd_defensores = Esquema_Tatico[0]
        qtd_meias = Esquema_Tatico[1]
        qtd_atacantes = Esquema_Tatico[2]
        
        for jogador in time:
                if jogador[1] == 'goleiro':
                    
                    if len(goleiro) == 0:
                            goleiro.append(jogador)
                    else:
                        if len(goleiro) == 1:
                            contador = 0
                            for jog in goleiro:
                            
                                if jogador[2] > jog[2]:
                                    goleiro[contador].append(jogador)
                                else:
                                    contador +=1
                        
                            
                elif jogador[1] == 'defensor':
                    if len(defensores) < qtd_defensores:
                            defensores.append(jogador)
                    else:
                        if len(defensores) == qtd_defensores:
                            contador = 0
                            menor = 0
                            anterior = 0
                            for jog in defensores:
                                if anterior == 0:
                                    anterior = jog[2]
                                if jogador[2] > jog[2] :
                                    if jog[2] < anterior:
                                        anterior = jog[2]
                                        menor = contador
                                    else:
                                        if jog[2] >= anterior:
                                            contador +=1
                                     
                                else:
                                    contador +=1
                            if jogador[2] > anterior:
                                defensores[menor].append(jogador)
                            else:
                                pass

                                    
                                    
                elif jogador[1] == 'meia':
                    if len(meias) < qtd_meias:
                            meias.append(jogador)
                    else:
                        if len(meias) == qtd_meias:
                            contador = 0
                            menor = 0
                            anterior = 0
                            for jog in meias:
                                if anterior == 0:
                                    anterior = jog[2]
                                if jogador[2] > jog[2]:
                                    if jog[2] < anterior:
                                        anterior = jog[2]
                                        menor = contador
                                    else:
                                        if jog[2] >= anterior:
                                            contador +=1
                                     
                                else:
                                    contador +=1
                            if jogador[2] > anterior:
                                meias[menor].append(jogador)
                            else:
                                pass
                            
                            
                            
                elif jogador[1] == 'atacante':
                    if len(atacantes) < qtd_atacantes:
                        atacantes.append(jogador)
                        
                    else:
                        if len(atacantes) == qtd_atacantes:
                            contador = 0
                            menor = 0
                            anterior = 0
                            for jog in meias:
                                if anterior == 0:
                                    anterior = jog[2]
                                if jogador[2] > jog[2]:
                                    if jog[2] < anterior:
                                        anterior = jog[2]
                                        menor = contador
                                    else:
                                        if jog[2] >= anterior:
                                            contador +=1
                                     
                                else:
                                    contador +=1
                            if int(jogador[2]) > anterior:
                                atacantes[menor].append(jogador)
                            else:
                                pass
                            
                    
                        
        
        errado = 0
        if len(goleiro) == 1:
            pass
        else:
            errado = 1
            print('Estão faltando jogadores no time:')
            print(f'{ 1 - len(goleiro)} goleiro')

            
            
        if len(defensores) == qtd_defensores:
            
            pass
        else:
            if errado == 1:
                print(f'{qtd_defensores - len(defensores)} defensores')
            else:
                errado = 1
                print('Estão faltando jogadores no time:')
                print(f'{qtd_defensores - len(defensores)} defensores')


            
            
        if len(meias) == qtd_meias :
            pass
        else:
            if errado == 1:
                print(f'{qtd_meias - len(meias)} meias')
            else:
                errado = 1
                print('Estão faltando jogadores no time:')
                print(f'{qtd_meias - len(meias)} meias')
            
            
            
        if len(atacantes) == qtd_atacantes :
            pass
                        
        else:
            if errado == 1:
                print(f'{qtd_atacantes - len(atacantes)} atacantes')
            else:
                errado = 1
                print('Estão faltando jogadores no time:')
                print(f'{qtd_atacantes - len(atacantes)} atacantes')
        if errado == 0 :
           
            posicao_goleiro = (40 // (len(goleiro)+1)) * ' '

            posicao_defensores =  ((40 - len(defensores))  // ((len(defensores))+1)) * ' '

            posicao_meias = ((40 - len(meias))  // ((len(meias))+1)) * ' '

            posicao_atacante = ((40 - len(atacantes))  // ((len(atacantes))+1)) * ' '    
            
            
            posicao_atacante = ((40 - len(atacantes))  // ((len(atacantes))+1)) * ' '
            
            print('+'+(40*'-')+'+')
            print('|'+(14*' ')+'|'+(10*' ')+'|'+(14*' ')+'|')
            print('|'+(15*' ')+(10*'-')+(15*' ')+'|')
            print('|'+(40*' ')+'|')
            
            posi_atacantes(atacantes)
            
            #print('|'+(5*' ')+ atacantes[0][0]+ (5*' ')+ atacantes[1][0] +(4*' ')+ atacantes[2][0]+ (8*' ') +'|')
            #print('|'+((posicao_atacante +'o') * len(atacantes))+(posicao_atacante)+' '+'|')
            print('|'+(40*' ')+'|')
            
            posi_meias(meias)
            
            #print('|'+(7*' ')+ meias[0][0]+ (6*' ')+ meias[1][0] +(5*' ')+ meias[2][0]+ (5*' ')+'|')
            #print('|'+((posicao_meias +'o')*len(meias))+(posicao_meias)+' '+'|')
            print('|'+(40*' ')+'|')
            print('|'+(40*' ')+'|')
            print('|'+(40*' ')+'|')
            
            posi_defensores(defensores)
            
            #print('|'+(5*' ')+ defensores[0][0]+ (2*' ')+ defensores[1][0] +(2*' ')+ defensores[2][0]+ (2*' ')+ defensores[3][0]+ (2*' ') +'|')
            #print('|'+' '+((posicao_defensores +'o')*len(defensores))+(posicao_defensores)+'|')
            print('|'+(40*' ')+'|')
            print('|'+(15*' ')+(4*'-')+('o')+(5*'-')+(15*' ')+'|')
            print('|'+(14*' ')+'|'+ (((10 - len(goleiro[0][0])) // 2) * ' ')+ goleiro[0][0] +(((10 - len(goleiro[0][0])) // 2) * ' ') +'|'+(14*' ')+'|')
            print('+'+(40*'-')+'+')

        
        else:
            pass

        
        
    else:
        
        print('O Esquema tático deve ser estabelecido antes de montar o time')
        
        return
    
def posi_atacantes(atacantes):
    if len(atacantes)  == 2:
        espaco = (40 - (len(atacantes[0][0])+ len(atacantes[1][0]))) // 2
        print('|'+((espaco//2)*' ')+atacantes[0][0]+(espaco*' ')+atacantes[1][0]+((espaco//2)*' ')+' '+'|')
        print('|'+(9*' ')+'o'+(19*' ')+'o'+(10*' ')+'|')

    elif len(atacantes)   == 3:
        print('|'+(5*' ')+atacantes[0][0]+(12*' ')+atacantes[1][0]+(12*' ')+atacantes[2][0]+(8*' ')+'|')
        print('|'+(5*' ')+'o'+(12*' ')+'o'+(12*' ')+'o'+(8*' ')+'|')


    elif len(atacantes)   == 4:
        print('|'+(4*' ')+atacantes[0][0]+(9*' ')+atacantes[1][0]+(9*' ')+atacantes[2][0]+(9*' ')+atacantes[3][0]+(5*' ')+'|')
        print('|'+(4*' ')+'o'+(9*' ')+'o'+(9*' ')+'o'+(9*' ')+'o'+(5*' ')+'|')


def posi_defensores(defensores):
    
    if len(defensores) == 2:
        espaco = (40 - (len(defensores[0][0])+ len(defensores[1][0]))) // 2
        print('|'+((espaco/2)*' ')+defensores[0][0]+(espaco*' ')+defensores[1][0]+((espaco/2)*' ')+'|')
        print('|'+(9*' ')+'o'+(19*' ')+'o'+(10*' ')+'|')
        
    elif len(defensores) == 3:
        espaco = (40 - (len(defensores[0][0])+ len(defensores[1][0])+len(defensores[2][0])) // 3)
        print('|'+((espaco/2)*' ')+defensores[0][0]+(espaco*' ')+defensores[1][0]+(espaco*' ')+defensores[2][0]+((espaco/2)*' ')+'|')
        print('|'+(5*' ')+'o'+(12*' ')+'o'+(12*' ')+'o'+(8*' ')+'|')

    
    elif len(defensores) == 4:
        espaco = int((40 - (len(defensores[0][0])+ len(defensores[1][0]) + len(defensores[2][0]) + len(defensores[3][0]))) // 5)

        print('|'+((espaco//2)*' ')+defensores[0][0]+(espaco*' ')+defensores[1][0]+(espaco*' ')+defensores[2][0]+(espaco*' ')+defensores[3][0]+((espaco//2)*' ')+'|')
        print('|'+(4*' ')+'o'+(9*' ')+'o'+(9*' ')+'o'+(9*' ')+'o'+(5*' ')+'|')

def posi_meias(meias):
    if len(meias) == 2:
        espaco = (40 - (len(meias[0][0])+ len(meias[1][0]))) // 2
        print('|'+((espaco/2)*' ')+meias[0][0]+(espaco*' ')+meias[1][0]+((espaco/2)*' ')+'|')
        print('|'+(9*' ')+'o'+(19*' ')+'o'+(10*' ')+'|')
        
    elif len(meias) == 3:
        espaco = (40 - (len(meias[0][0])+ len(meias[1][0])+len(meias[2][0])) // 3)
        print('|'+((espaco//2)*' ')+meias[0][0]+(espaco*' ')+meias[1][0]+(espaco*' ')+meias[2][0]+((espaco//2)*' ')+'|')
        print('|'+(5*' ')+'o'+(12*' ')+'o'+(12*' ')+'o'+(8*' ')+'|')

    
    elif len(meias) == 4:
        espaco = int((40 - (len(meias[0][0])+ len(meias[1][0]) + len(meias[2][0]) + len(meias[3][0]))) // 5)

        print('|'+(espaco*' ')+meias[0][0]+(espaco*' ')+meias[1][0]+(espaco*' ')+meias[2][0]+(espaco*' ')+meias[3][0]+(espaco*' ')+'|')
        print('|'+(4*' ')+'o'+(9*' ')+'o'+(9*' ')+'o'+(9*' ')+'o'+(5*' ')+'|')

    
    
    
def entrada(num):
    if num == 1:
        CONTRATAR_JOGADORES(num)
        print()
        return entrada(int(input('Entre com 1 (CONTRATAR_JOGADORES) - 2 (TROCA_JOGADORES) - 3(Definir_Esquema_Tatico) - 4 (Montar_o_Time) - 5 (SAIR) \n')))

    elif num == 2:
        TROCA_JOGADORES(num)
        print()
        return entrada(int(input('Entre com 1 (CONTRATAR_JOGADORES) - 2 (TROCA_JOGADORES) - 3(Definir_Esquema_Tatico) - 4 (Montar_o_Time) - 5 (SAIR) \n')))

    elif num == 3:
        Definir_Esquema_Tatico(num)
        print()
        return entrada(int(input('Entre com 1 (CONTRATAR_JOGADORES) - 2 (TROCA_JOGADORES) - 3(Definir_Esquema_Tatico) - 4 (Montar_o_Time) - 5 (SAIR) \n')))

    elif num == 4:
        Montar_o_Time(num)
        print()
        return entrada(int(input('Entre com 1 (CONTRATAR_JOGADORES) - 2 (TROCA_JOGADORES) - 3(Definir_Esquema_Tatico) - 4 (Montar_o_Time) - 5 (SAIR) \n')))

    elif num == 5:
        print('')

num = int(input('Entre com 1 (CONTRATAR_JOGADORES) - 2 (TROCA_JOGADORES) - 3(Definir_Esquema_Tatico) - 4 (Montar_o_Time) - 5 (SAIR) \n'))
entrada(num)

#\n
'''
1
cabaro goleiro 9
1
calebe atacante 9
1
joao atacante 8
1
vinivius meia 7
1
caue meia 6
1
guto meia 5
1
folha meia 4
1
sido defensor 3
1
trom defensor 2
1
jober defensor 1
1
ticaba defensor 9
3
4 4 2
4

'''








