import random,pygame

pygame.init()

listadecomidas=[['Estrogonofe',10.5,True],['Rojões',8.5,True],['Massa com atum',8,True],['Francesinha',20,False],['Bife',13.5,False],['Costeletas',15.5,False],['Robalo',13.5,False]]
listaqnd=[5,5,5,0,0,0,0]
conquistas=[['Conquista desbloquear todas as comida',False],['conquista atender 10 clientes',False],['conquista atender 50 clientes',False],['conquista atender 100 clientes',False],['conquista ter 1000€',False],['conquista ter 5000€',False],['conquista ter 10000€',False],['conquista comprar 100 comidas',False],['conquista usar um codigo', False],['conquista de usar codigo do senna',False]]
conquistadesbloquear=0
conquistaclientes=0
conquistacomidas=0
conquistacodigo=0
codenum=0
codesenna=False
res1='s'
aclientes=0
aguito=0
acomidas=0
acodigo=False
asenna=False
res=1
guito=0


while guito>=0 and res1=='s':
    
    if res==1:
        print('Tu és o gerente este restaurante!!')
        print('Modos de jogo:')
        print('[1]Fácil (Começas com 1000€)\n[2]Médio (Começas com 500€)\n[3]Difícil (Começas com 300€)\n[4]Hardcore (Começas com 100€)')
        #Medida anti-ruben #1
        try:
            mododjogo=int(input('Qual queres escolher? '))
        except ValueError:
            print('Opção inválida')

        match mododjogo:
            case 1:
                guito=1000
            case 2:
                guito=500
            case 3:
                guito=300
            case 4:
                guito=100
        res=0

    if listaqnd[0]>=0 or listaqnd[1]>=0 or listaqnd[2]>=0 or listaqnd[3]>=0 or listaqnd[4]>=0 or listaqnd[5]>=0 or listaqnd[6]>=0:
        print('O que queres fazer?')
        print('[1]Desbloquear comidas\n[2]Ver stock\n[3]Ver dinheiro\n[4]Comprar comidas\n[5]Próximo cliente\n[6]Códigos\n[7]Ver conquistas\n[8]Estatísticas\n[9]Desistir')
        try:
            op=int(input('Qual vais escolher? '))
        except ValueError:
            print('Opção inválida')

        match op:

            case 1:

                print('Que comidas queres comprar?')
                for i in range(1,5):
                    print('[{}]{} (preço para desbloquear {})'.format(i,listadecomidas[i+2][0],listadecomidas[i+2][1]*20))
                #Medida anti-ruben #2
                try:
                    opdesbloquearcomida=int(input('Qual queres comprar? '))
                except ValueError:
                    print('Opção inválida')
                
                for i in range(1,5):
                    if opdesbloquearcomida==i:
                        if listadecomidas[i+2][2]==False:
                            if guito>listadecomidas[i+2][1]*20:
                                conquistadesbloquear+=1
                                guito-=listadecomidas[i+2][1]*20
                                listadecomidas[i+2][2]=True
                                numini=random.randint(1,3)
                                listaqnd[i+2]+=numini
                                print('Desbloqueaste {}\nTens agora como prenda {} {}'.format(listadecomidas[i+2][0],numini,listadecomidas[i+2][0]))
                            else:
                                print('Não tens dinheiro suficiente')
                        else:
                            print('Já tinhas desbloqueado {}'.format(listadecomidas[i+2][0]))

            case 2:

                print('Stock:')
                for i in range(0,7):
                    print('{}:{}'.format(listadecomidas[i][0],listaqnd[i]))

            case 3:

                print('Tens agora {}€'.format(guito))
            
            case 4:
                print('Comidas para comprar: ')
                for i in range(0,7):
                    print('[{}]{}'.format(i+1,listadecomidas[i][0]))
                #Medida anti-ruben #3
                try:
                    opcomprarcomidas=int(input('Qual queres comprar? '))
                except ValueError:
                    print('Opção inválida')
                for i in range(1,8):
                    if i==opcomprarcomidas:
                        if listadecomidas[i-1][2]==True:
                            #Medida anti-ruben #4
                            try:
                                qnd=int(input('Quantos {} queres comprar? '.format(listadecomidas[i-1][0])))
                            except ValueError:
                                print('Opção inválida')
                            if guito>=(qnd*listadecomidas[i-1][1]):
                                print('Isso vai custar {}€ ,tens {}€'.format(qnd*listadecomidas[i-1][1],guito))
                                #Medida anti-ruben #5
                                try:
                                    opsn=str(input('Queres comprar [S/N]')).lower()
                                except ValueError:
                                    print('Opção inválida')
                                if opsn=='s':
                                    guito-=qnd*listadecomidas[i-1][1]
                                    conquistacomidas+=1
                                    listaqnd[i-1]+=qnd
                                    print('Tens agora {} {}'.format(listaqnd[i-1],listadecomidas[i-1][0]))
                                elif opsn=='n':
                                    print('Compra cancelada')
                                else:
                                    print('Compra inválida')

            #agr vais fazer o ultimo caso que é os gajos pedirem a comida que quiserem a qnd que quiserem e tens de ver se ha dessa comida ou a da qnd suficiente dps podes aceitar o pedido ou recusar se recusares e podias dar a comida perdes guito se recusares e nao puderes dar a comida n ganhas nada  se aceitares e poderes dar a comida recebes a guita da comida se aceitares e n puderes dar ao cliente a comida perdes guito
            case 5:
                comidaqquerem=random.randint(0,6)
                qntcomida=random.randint(1,8)
                print('Eu queria {} doses de {}, por favor.'.format(qntcomida,listadecomidas[comidaqquerem][0],))
                #Medida anti-ruben #6
                try:
                    aceitrecus=str(input('Queres aceitar o pedido? [A (Aceitar)/R (Recusar)] ')).lower()
                except ValueError:
                    print('Opção inválida')
                if aceitrecus=='a':
                    conquistas[3][1]+=1
                    if listadecomidas[comidaqquerem][2]==True:
                        if listaqnd[comidaqquerem]>=qntcomida:
                            guito+=listadecomidas[comidaqquerem][1]*qntcomida
                            listaqnd[comidaqquerem]-=qntcomida
                            print('O cliente ficou satisfeito\nTens agora {}€'.format(guito))
                        else:
                            guito-=20
                            print('O cliente ficou insatisfeito porque não tinha a quantidade de comida que ele pediu\nPerdeste 20€ estás agora com {}€'.format(guito))
                    else:
                        guito-=20
                        print('O cliente ficou insatisfeito porque ainda não desbloqueaste esta comida\nPerdeste 20€ estás agora com {}€'.format(guito))
                elif aceitrecus=='r':
                    conquistas[3][1]+=1
                    if listadecomidas[comidaqquerem][2]==True:
                        if listaqnd[comidaqquerem]>=qntcomida:
                            guito-=20
                            print('O cliente não ficou satisfeito porque já tinhas desbloqueado a comida\nou tinhas comida suficiente\nTenta comprar mais comidas para poderes servir os clientes\nOu desbloquear novas comidas')
                        elif listaqnd[comidaqquerem]<qntcomida:
                            print('O cliente não ficou muito satisfeito mas foi-se embora\nTenta comprar mais comidas')
                    else:
                        print('O cliente não ficou muito satisfeito mas foi se embora\nTenta desbloquear mais comidas')
            case 6:
                opcodigo=input('Escreve o código secreto: ')
                if opcodigo=='\_gordo':
                    musicagordo=pygame.mixer.music.load('minefood.mp3')
                    pygame.mixer.music.play()
                    print('Desbloqueaste mais 99 comidas de cada comida que tinhas desbloqueado')
                    codenum+=1
                    for i in range(0,7):
                        if listadecomidas[i][2]==True:
                            conquistacomidas+=99
                            
                            listaqnd[i]+=99
                    while pygame.mixer.music.get_busy() is True:
                        conquistacodigo=True
                elif opcodigo=='\_ayrton_senna':
                    musicasenna=pygame.mixer.music.load('ayrton.mp3')
                    pygame.mixer.music.play()
                    #Sugerido por Lucas :) (mi amigo),(A musica tbm)
                    print('AAAAAYYYYYRRRRTOOONNN SSSSEEEEENNNNNAAAAA DO BBBBRRRRAAAAASSSSSSIIIIIIILLLLLLL!!!!!')
                    print('Desbloqueaste todas as comidas')
                    codenum+=1
                    codesenna=True
                    for i in range(3,7):
                        conquistadesbloquear+=1
                        listadecomidas[i][2]=True
                    pygame.time.delay(1000)
                    while pygame.mixer.music.get_busy() is True:
                        conquistacodigo=True
                elif opcodigo=='\_cold_desert':
                    #se vires isto stor isto é uma piada interna entre mim o ruben e o lucas (mi amigo)
                    musicamoney=pygame.mixer.music.load('mony.mp3')
                    pygame.mixer.music.play()
                    guito+=1000000000
                    print('Tens agora 1B€')
                    codenum+=1
                    while pygame.mixer.music.get_busy() is True:
                        conquistacodigo=True
                elif opcodigo=='\_fuck_the_story_I_want_the_achievments':
                    conquistacodigo=True
                    for i in range(0,9):
                        musicaconquista1=pygame.mixer.music.load('minerare.mp3')
                        pygame.mixer.music.play()
                        conquistas[i][1]=True
                        print('Desbloqueaste todas as conquistas')
                        codenum+=1
                    while pygame.mixer.music.get_busy() is True:
                        conquistacodigo=True
                else:
                    print('O código está errado')
                
            case 7 :
                print('Estas são as conquistas:')
                for i in range(0,11):
                            print('{}:{}'.format(conquistas[i][0],conquistas[i][1]))
            case 8:
                print('Comidas desbloqueadas: {}\nClientes atendidos: {}\nComidas compradas: {}\nCódigos usados: {}'.format(conquistadesbloquear,conquistaclientes,conquistacomidas,codenum))

            case 9:
                des=str(input('Queres desistir [S/N]')).lower()
                if des=='s':
                    res1='n'
                    res=0
                elif des=='n':
                    print('O jogo vai continuar')
                else:
                    print('Opção inválida')

        if conquistadesbloquear==4:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            conquistas[0][1]=True
            conquistadesbloquear=5
            print('Parabéns desbloqueaste todas as comidas')
        if conquistaclientes>=10 and aclientes==0:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            aclientes=1
            conquistas[1][1]=True
            print('Parabéns atendeste 10 clientes')
        elif conquistaclientes>=50 and aclientes==1:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            aclientes=2
            conquistas[2][1]=True
            print('Parabéns atendeste 50 clientes')
        elif conquistaclientes>=100 and aclientes==2:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            aclientes=3
            conquistas[3][1]=True
            print('Parabéns atendeste 100 clientes')
        if guito>=1000 and aguito==0:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            aguito=1
            conquistas[4][1]=True
            print('Parabéns tens 1000€')
        if guito>=5000 and aguito==1:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            aguito=2
            conquistas[5][1]=True
            print('Parabéns tens 5000€')
        if guito>=10000 and aguito==2:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            aguito=3
            conquistas[6][1]=True
            print('Parabéns tens 10000€')
        if conquistacomidas>=100 and acomidas==0:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            acomidas=1
            conquistas[7][1]=True
            print('Parabéns já compraste 100 comidas')
        if conquistacodigo>=1 and acodigo==False:
            acodigo=True
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            conquistas[8][1]=True
            print('Parabéns usaste o teu primeiro código')
        if codesenna==True and asenna==False:
            asenna=True
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            conquistas[9][1]=True
            print('Parabéns usaste o código do senna (contribuiçao do lucas (mi amigo))')
        if guito<0:
            print('Ficaste sem dinheiro \n Perdeste')
            res1='n'
        if res1=='n':
            try:
                res1=str(input('Queres recomeçar [S/N]')).lower()
            except ValueError:
                print('Opção inválida')
            if res1=='s':
                print('O jogo vai ser recomeçado')
                guito=0
                res=1
            elif res1=='n':
                print('O jogo acabou')
                break
            else:
                print('Opção inválida')
        
