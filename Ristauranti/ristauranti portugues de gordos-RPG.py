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
    if res1=='s':
        musicass=pygame.mixer.music.load('intense.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
    if res==1:
        print('\033[31mTu és o gerente este restaurante!!\033[m')
        print('Modos de jogo:')
        print('\033[32m[1]Fácil (Começas com 1000€)\033[m\n\033[33m[2]Médio (Começas com 500€)\033[m\n\033[38;2;255;165;0m[3]Difícil (Começas com 300€)\033[m\n\033[31m[4]Hardcore (Começas com 100€)\033[m')
        #Medida anti-ruben #1
        try:
            mododjogo=int(input('Qual queres escolher? '))
        except ValueError:
            print('\033[31mOpção inválida\033[m')

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
        print('[1]Desbloquear comidas\n[2]Ver stock\n[3]Ver dinheiro\n[4]Comprar comidas\n[5]Próximo cliente\n[6]Códigos\n[7]Ver conquistas\n[8]Estatísticas\n[9]Desistir\n[10]Créditos')
        try:
            op=int(input('Qual vais escolher? '))
        except ValueError:
            print('Opção inválida')

        match op:

            case 1:

                print('Que comidas queres comprar?')
                for i in range(1,5):
                    print('\033[36m[{}]{} (preço para desbloquear {})\033[m'.format(i,listadecomidas[i+2][0],listadecomidas[i+2][1]*20))
                print('\033[36m[5]Voltar atrás\033[m')
                #Medida anti-ruben #2
                try:
                    opdesbloquearcomida=int(input('Qual queres comprar? '))
                except ValueError:
                    print('\033[31mOpção inválida\033[m')
                
                for i in range(1,5):
                    if opdesbloquearcomida==i:
                        if listadecomidas[i+2][2]==False:
                            if guito>listadecomidas[i+2][1]*20:
                                conquistadesbloquear+=1
                                guito-=listadecomidas[i+2][1]*20
                                listadecomidas[i+2][2]=True
                                numini=random.randint(1,3)
                                listaqnd[i+2]+=numini
                                print('\033[32mDesbloqueaste {}\nTens agora como prenda {} {}\033[m'.format(listadecomidas[i+2][0],numini,listadecomidas[i+2][0]))
                            else:
                                print('\033[31mNão tens dinheiro suficiente\033[m')
                        else:
                            print('\033[31mJá tinhas desbloqueado {}\033[m'.format(listadecomidas[i+2][0]))
                    if opdesbloquearcomida==5:
                        print('\033[31mCompra cancelada\033[m')
            case 2:

                print('Stock:')
                for i in range(0,7):
                    print('\033[33m{}:{}\033[m'.format(listadecomidas[i][0],listaqnd[i]))

            case 3:

                print('\033[32mTens agora {}€\033[m'.format(guito))
            
            case 4:
                print('\033[34mComidas para comprar: \033[m')
                for i in range(0,7):
                    print('\033[34m[{}]{}\033[m'.format(i+1,listadecomidas[i][0]))
                #Medida anti-ruben #3
                try:
                    opcomprarcomidas=int(input('Qual queres comprar? '))
                except ValueError:
                    print('\033[31mOpção inválida\033[m')
                for i in range(1,8):
                    if i==opcomprarcomidas:
                        if listadecomidas[i-1][2]==True:
                            #Medida anti-ruben #4
                            try:
                                qnd=int(input('Quantos {} queres comprar? '.format(listadecomidas[i-1][0])))
                            except ValueError:
                                print('\033[31mOpção inválida\033[m')
                            if guito>=(qnd*listadecomidas[i-1][1]):
                                print('\033[32mIsso vai custar {}€ ,tens {}€\033[m'.format(qnd*listadecomidas[i-1][1],guito))
                                #Medida anti-ruben #5
                                try:
                                    opsn=str(input('Queres comprar [\033[32mS\033[m/\033[31mN\033[m]')).lower()
                                except ValueError:
                                    print('\033[31mOpção inválida\033[m')
                                if opsn=='s':
                                    guito-=qnd*listadecomidas[i-1][1]
                                    conquistacomidas+=1
                                    listaqnd[i-1]+=qnd
                                    print('\033[33mTens agora {} {}\033[m'.format(listaqnd[i-1],listadecomidas[i-1][0]))
                                elif opsn=='n':
                                    print('\033[31mCompra cancelada\033[m')
                                else:
                                    print('\033[31mCompra inválida\033[m')

            #agr vais fazer o ultimo caso que é os gajos pedirem a comida que quiserem a qnd que quiserem e tens de ver se ha dessa comida ou a da qnd suficiente dps podes aceitar o pedido ou recusar se recusares e podias dar a comida perdes guito se recusares e nao puderes dar a comida n ganhas nada  se aceitares e poderes dar a comida recebes a guita da comida se aceitares e n puderes dar ao cliente a comida perdes guito
            case 5:
                comidaqquerem=random.randint(0,6)
                qntcomida=random.randint(1,8)
                print('\033[36mEu queria {} doses de {}, por favor\033[m.'.format(qntcomida,listadecomidas[comidaqquerem][0],))
                #Medida anti-ruben #6
                try:
                    aceitrecus=str(input('Queres aceitar o pedido? [\033[32mA (Aceitar)\033[m/\033[31mR (Recusar)\033[m] ')).lower()
                except ValueError:
                    print('\033[31mOpção inválida\033[m')
                if aceitrecus=='a':
                    conquistas[3][1]+=1
                    conquistaclientes+=1
                    if listadecomidas[comidaqquerem][2]==True:
                        if listaqnd[comidaqquerem]>=qntcomida:
                            guito+=listadecomidas[comidaqquerem][1]*qntcomida
                            listaqnd[comidaqquerem]-=qntcomida
                            print('\033[32mO cliente ficou satisfeito\nTens agora {}€\033[m'.format(guito))
                        else:
                            guito-=20
                            print('\033[31mO cliente ficou insatisfeito porque não tinha a quantidade de comida que ele pediu\nPerdeste 20€ estás agora com {}€\033[m'.format(guito))
                    else:
                        guito-=20
                        print('\033[31mO cliente ficou insatisfeito porque ainda não desbloqueaste esta comida\nPerdeste 20€ estás agora com {}€\033[m'.format(guito))
                elif aceitrecus=='r':
                    conquistas[3][1]+=1
                    conquistaclientes+=1
                    if listadecomidas[comidaqquerem][2]==True:
                        if listaqnd[comidaqquerem]>=qntcomida:
                            guito-=20
                            print('\033[31mO cliente não ficou satisfeito porque já tinhas desbloqueado a comida\nou tinhas comida suficiente\nTenta comprar mais comidas para poderes servir os clientes\nOu desbloquear novas comidas\nPerdeste 20€\033[m')
                        elif listaqnd[comidaqquerem]<qntcomida:
                            print('\033[36mO cliente não ficou muito satisfeito mas foi-se embora\nTenta comprar mais comidas\033[m')
                    else:
                        print('\033[36mO cliente não ficou muito satisfeito mas foi se embora\nTenta desbloquear mais comidas\033[m')
            case 6:
                opcodigo=input('\033[1;32;40mEscreve o código secreto: \033[1;32;40m')
                if opcodigo=='\_gordo':
                    musicagordo=pygame.mixer.music.load('minefood.mp3')
                    pygame.mixer.music.play()
                    print('\033[1;32;40mDesbloqueaste mais 99 comidas de cada comida que tinhas desbloqueado\033[m')
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
                    print('\033[33mAAAAAYYYYYRRRRTOOONNN SSSSEEEEENNNNNAAAAA DO BBBBRRRRAAAAASSSSSSIIIIIIILLLLLLL!!!!!\033[m')
                    print('\033[1;32;40mDesbloqueaste todas as comidas\033[m')
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
                    print('\033[1;32;40mTens agora 1B€\033[m')
                    codenum+=1
                    while pygame.mixer.music.get_busy() is True:
                        conquistacodigo=True
                elif opcodigo=='\_fuck_the_story_I_want_the_achievments':
                    conquistacodigo=True
                    musicaconquista1=pygame.mixer.music.load('minerare.mp3')
                    pygame.mixer.music.play()
                    print('\033[1;32;40mDesbloqueaste todas as conquistas\033[m')
                    codenum+=1
                    for i in range(0,9):
                        conquistas[i][1]=True
                    while pygame.mixer.music.get_busy() is True:
                        conquistacodigo=True
                else:
                    print('\033[31mO código está errado\033[m')
                
            case 7 :
                print('Estas são as conquistas:')
                for i in range(0,10):
                            print('\033[35m{}:{}\033[m'.format(conquistas[i][0],conquistas[i][1]))
            case 8:
                print('\033[34mComidas desbloqueadas: {}\033[m\n\033[36mClientes atendidos: {}\033[m\n\033[33mComidas compradas: {}\033[m\n\033[32mCódigos usados: {}\033[m'.format(conquistadesbloquear,conquistaclientes,conquistacomidas,codenum))

            case 9:
                des=str(input('Queres desistir [\033[32mS\033[m/\033[31mN\033[m]')).lower()
                if des=='s':
                    res1='n'
                    res=0
                elif des=='n':
                    print('\033[32mO jogo vai continuar\033[m')
                else:
                    print('\033[31mOpção inválida\033[m')
            case 10:
                print('\033[37mCódigo:João Duarte\nIdeias:João Duarte, lucas, ruben\033[m')
        if conquistadesbloquear==4:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            conquistas[0][1]=True
            conquistadesbloquear=5
            guito += 200
            print('\033[35mParabéns desbloqueaste todas as comidas\033[m')
            print('\033[32mGanhaste 200€\nTens agora {}€\033[m'.format(guito))
        if conquistaclientes>=10 and aclientes==0:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            guito += 100
            aclientes=1
            conquistas[1][1]=True
            print('\033[35mParabéns atendeste 10 clientes\033[m')
            print('\033[32mGanhaste 100€\nTens agora {}€\033[m'.format(guito))
        elif conquistaclientes>=50 and aclientes==1:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            aclientes=2
            guito += 500
            conquistas[2][1]=True
            print('\033[35mParabéns atendeste 50 clientes\033[m')
            print('\033[32mGanhaste 500€\nTens agora {}€\033[m'.format(guito))
        elif conquistaclientes>=100 and aclientes==2:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            aclientes=3
            guito += 1000
            conquistas[3][1]=True
            print('\033[35mParabéns atendeste 100 clientes\033[m')
            print('\033[32mGanhaste 1000€\nTens agora {}€\033[m'.format(guito))
        if guito>=1000 and aguito==0:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            aguito=1
            guito += 100
            conquistas[4][1]=True
            print('\033[35mParabéns tens 1000€\033[m')
            print('\033[32mGanhaste 100€\nTens agora {}€\033[m'.format(guito))
        if guito>=5000 and aguito==1:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            aguito=2
            guito += 500
            conquistas[5][1]=True
            print('\033[35mParabéns tens 5000€\033[m')
            print('\033[32mGanhaste 500€\nTens agora {}€\033[m'.format(guito))
        if guito>=10000 and aguito==2:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            aguito=3
            conquistas[6][1]=True
            guito += 1000
            print('\033[35mParabéns tens 10000€\033[m')
            print('\033[32mGanhaste 1000€\nTens agora {}€\033[m'.format(guito))
        if conquistacomidas>=100 and acomidas==0:
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            acomidas=1
            conquistas[7][1]=True
            guito += 500
            print('\033[35mParabéns já compraste 100 comidas\033[m')
            print('\033[32mGanhaste 500€\nTens agora {}€\033[m'.format(guito))
        if conquistacodigo>=1 and acodigo==False:
            acodigo=True
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            conquistas[8][1]=True
            print('\033[35mParabéns usaste o teu primeiro código\033[m')
        if codesenna==True and asenna==False:
            asenna=True
            musicaconquista1=pygame.mixer.music.load('minerare.mp3')
            pygame.mixer.music.play()
            conquistas[9][1]=True
            print('\033[35mParabéns usaste o código do senna (contribuiçao do lucas (mi amigo))\033[m')
        if guito<0:
            print('\033[31mFicaste sem dinheiro \n Perdeste\033[m')
            res1='n'
        if res1=='n':
            #Medida anti-ruben #7
            try:
                res1=str(input('Queres recomeçar [\033[33mS\033[m/\033[31mN\033[m]')).lower()
            except ValueError:
                print('\033[31mOpção inválida\033[m')
            if res1=='s':
                print('\033[33mO jogo vai ser recomeçado\033[m')
                guito=0
                res=1
            elif res1=='n':
                print('\033[31mO jogo acabou\033[m')
                break
            else:
                print('\033[31mOpção inválida\033[m')

