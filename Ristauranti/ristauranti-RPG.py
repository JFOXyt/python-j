import random,pygame

pygame.init()

listadecomidas=[['Estrogonofe',10.5,True],['Rojões',8.5,True],['Massa com atum',8,True],['Francesinha',20,False],['Bife',13.5,False],['Costeletas',15.5,False],['Robalo',13.5,False]]
listaqnd=[5,5,5,0,0,0,0]
conquistas=[['Conquista desbloquear todas as comida',False],['conquista atender 10 clientes',False],['conquista atender 50 clientes',False],['conquista atender 100 clientes',False],['conquista ter 1000€',False],['conquista ter 5000€',False],['conquista ter 10000€',False],['conquista comprar 100 comidas',False],['conquista usar um codigo', False]]
conquistadesbloquear=0
conquistaclientes=0
conquistacomidas=0
conquistacodigo=0

aclientes=0

aguito=0

acomidas=0

acodigo=False

print('Tu és o gerente este restaurante!!')
print('Modos de jogo:')
print('[1]Fácil (Começas com 1000€)\n[2]Médio (Começas com 500€)\n[3]Difícil (Começas com 300€)\n[4]Hardcore (Começas com 100€)')
mododjogo=int(input('Qual queres escolher? '))
guito=0

match mododjogo:
    case 1:
        guito+=1000
    case 2:
        guito+=500
    case 3:
        guito+=300
    case 4:
        guito+=100

while guito>0:
    if listaqnd[0]>=0 or listaqnd[1]>=0 or listaqnd[2]>=0 or listaqnd[3]>=0 or listaqnd[4]>=0 or listaqnd[5]>=0 or listaqnd[6]>=0:
        print('O que queres fazer?')
        print('[1]Desbloquear comidas\n[2]Ver stock\n[3]Ver dinheiro\n[4]Comprar comidas\n[5]Próximo cliente\n[6]Códigos\n[7]Ver conquistas\n[8]Estatísticas')
        op=int(input('Qual vais escolher? '))

        match op:

            case 1:

                print('Que comidas queres comprar?')
                print('[1]Francesinha (preço para desbloquear 250)\n[2]Bife (preço para desbloquear 200)\n[3]Costeletas de frango (preço para desbloquar 220\n[4]Robalo (preço para desbloquar 210) ')
                opdesbloquearcomida=int(input('Qual queres comprar? '))
                match opdesbloquearcomida:
                    case 1:
                        if listadecomidas[3][2]==False:
                            if guito>=250:
                                conquistadesbloquear+=1
                                guito-=250
                                listadecomidas[3][2]=True
                                frannumini=random.randint(1,3)
                                listaaddfran=listaqnd[3]+frannumini
                                listaqnd[3] = listaaddfran
                                print('Desbloquaste a francesinha\n Tens agora como prenda {} francesinha '.format(frannumini))
                            else:
                                print('Não tens dineiro suficiente')
                        else:
                            print('Já desbloquaste a francesinha')

                    case 2:
                        if listadecomidas[4][2]==False:
                            if guito>=200:
                                conquistadesbloquear+=1
                                guito-=200
                                listadecomidas[4][2]=True
                                bifenumini=random.randint(1,3)
                                listaaddbife=listaqnd[4]+bifenumini
                                listaqnd[4]=listaaddbife
                                print('Desbloquaste o bife\n Tens agora como prenda {} bife '.format(bifenumini))
                            else:
                                print('Não tens dinheiro suficiente')
                        else:
                            print('Já desbloquaste o bife')

                    case 3:
                        if listadecomidas[5][2]==False:
                            if guito>=220:
                                conquistadesbloquear+=1
                                guito-=200
                                listadecomidas[5][2]=True
                                costeletanumini=random.randint(1,3)
                                listaaddcosteleta=listaqnd[5]+costeletanumini
                                listaqnd[5]=listaaddcosteleta
                                print('Desbloquaste as costeletas\n Tens agora como prenda {} costeletas '.format(costeletanumini))
                            else:
                                print('Não tens dinheiro suficiente')
                        else:
                            print('Já desbloquaste a costeleta')

                    case 4:
                        if listadecomidas[6][2]==False:
                            if guito>=210:
                                conquistadesbloquear+=1
                                guito-=210
                                listadecomidas[6][2]=True
                                robalonumini=random.randint(1,3)
                                listaaddrobalo=listaqnd[6]+robalonumini
                                listaqnd[6]=listaaddrobalo
                                print('Desbloquaste o robalo\n Tens agora como prenda {} robalo '.format(robalonumini))
                        else:
                            print('Já desbloquaste o robalo')
            case 2:

                print('Stock:')
                print('Estrogonofe: {}'.format(listaqnd[0]))
                print('Rojões: {}'.format(listaqnd[1]))
                print('Massa com atum: {}'.format(listaqnd[2]))
                print('Francesinha: {}'.format(listaqnd[3]))
                print('Bife: {}'.format(listaqnd[4]))
                print('Costeletas: {}'.format(listaqnd[5]))
                print('Robalo: {}'.format(listaqnd[6]))

            case 3:

                print('Tens agora {}€'.format(guito))
            
            case 4:
                print('Comidas para comprar: ')
                print('[1]Estrogonofe\n[2]Rojões\n[3]Massa com atum\n[4]Francesinha\n[5]Bife\n[6]Costeletas\n[7]Robalo')
                opcomprarcomidas=int(input('Qual queres comprar? '))
                match opcomprarcomidas:
                    case 1:
                        if listadecomidas[0][2]==True:
                            qndestrogonofe=int(input('Quantos estrogonofes queres comprar? '))
                            if guito>=(qndestrogonofe*10.5):
                                print('Isso vai custar {}€, tens agora {}'.format(qndestrogonofe*10.5,guito))
                                opsnestrogonofe=str(input('Queres comprar [S/N]')).lower()
                                if opsnestrogonofe=='s':
                                    guito= guito - (qndestrogonofe*10.5)
                                    conquistacomidas+=1
                                    listaqnd[0]+=qndestrogonofe
                                    print('Tens agora {} estrogonofes'.format(listaqnd[0]))
                                elif opsnestrogonofe=='n':
                                    print('Compra cancelada')
                                else:
                                    print('Opção inválida')
                            else:
                                print('Não tens dinheiro suficiente ')
                        else:
                            print('Ainda não desbloqueaste esta comida')
                    case 2:
                        if listadecomidas[1][2]==True:
                            qndrojoes=int(input('Quantos rojões queres comprar? '))
                            if guito>=(qndrojoes*8.5):
                                print('Isso vai custar {}€, tens {}€'.format(qndrojoes*8.5,guito))
                                opsnrojoes=str(input('Queres comprar [S/N]')).lower()
                                if opsnrojoes=='s':
                                    guito=guito-(qndrojoes*8.5)
                                    conquistacomidas+=1
                                    listaqnd[1]+=qndrojoes
                                    print('Tens agora {} rojões'.format(listaqnd[1]))
                                elif opsnrojoes=='n':
                                    print('Compra cancelada')
                                else:
                                    print('Opção inválida')
                            else:
                                print('Não tens dinheiro suficiente')
                        else:
                            print('Ainda não desbloqueaste os rojões')
                    case 3:
                        if listadecomidas[2][2]==True:
                            qndmassacatum=int(input('Quantas massas com atum queres comprar? '))
                            if guito>=(qndmassacatum*8):
                                print('Isso vai custar {}€, tens agora{}€'.format(qndmassacatum*8,guito))
                                opsnmassacatum=str(input('Queres comprar [S/N]')).lower()
                                if opsnmassacatum=='s':
                                    guito=guito-(qndmassacatum*8)
                                    conquistacomidas+=1
                                    listaqnd[2]+=qndmassacatum
                                    print('Tens agora {} massas com atum'.format(listaqnd[2]))
                                elif opsnmassacatum=='n':
                                    print('Compra cancelada')
                                else:
                                    print('Opção inválida')
                            else:
                                print('Não tens dinheiro suficiente')
                        else:
                            print('Ainda não desbloqueaste esta comida')
                    case 4:
                        if listadecomidas[3][2]==True:
                            qndfrancesinha=int(input('Quantas francesinhas queres comprar? '))
                            if guito>=(qndfrancesinha*20):
                                print('Isso vai custar {}€, tens {}€'.format(qndfrancesinha*20,guito))
                                opsnfrancesinha=str(input('Queres comprar [S/N]')).lower()
                                if opsnfrancesinha=='s':
                                    guito=guito-(qndfrancesinha*20)
                                    conquistacomidas+=1
                                    listaqnd[2]+=qndfrancesinha
                                    print('Tens agora {} francesinhas'.format(listaqnd[3]))
                                elif opsnfrancesinha=='n':
                                    print('Compra cancelada')
                                else:
                                    print('Opção inválida')
                            else:
                                print('Não tens dinheiro suficiente')
                        else:
                            print('Ainda não desbloqueaste esta comida')
                    case 5:
                        if listadecomidas[4][2]==True:
                            qndbife=int(input('Quantos bifes queres comprar? '))
                            if guito>=(qndbife*13.5):
                                print('Isso vai custar {}€,tens {}€'.format(qndbife*13.5,guito))
                                opsnbife=str(input('Queres comprar [S/N]')).lower()
                                if opsnbife=='s':
                                    guito=guito-(qndbife*13.5)
                                    conquistacomidas+=1
                                    listaqnd[4]+=qndbife
                                    print('Tens agora {} bifes'.format(listaqnd[4]))
                                elif opsnbife=='n':
                                    print('Compra cancelada')
                                else:
                                    print('Opção inválida')
                            else:
                                print('Não tens dinheiro suficiente')
                        else:
                            print('Ainda não desbloqueste esta comida')
                    case 6:
                        if listadecomidas[5][2]==True:
                            qndcosteletas=int(input('Quantas costeletas queres comprar? '))
                            if guito>=(qndcosteletas*15.5):
                                print('Isso vai custar {}€ ,tens {}€'.format(qndcosteletas*15.5,guito))
                                opsncosteletas=str(input('Queres comprar [S/N]')).lower()
                                if opsncosteletas=='s':
                                    guito=guito-(qndcosteletas*15.5)
                                    conquistacomidas+=1
                                    listaqnd[5]+=qndcosteletas
                                    print('Tens agora {} costeletas'.format(listaqnd[5]))
                                elif opsncosteletas=='n':
                                    print('Compra cancelada')
                                else:
                                    print('Opção inválida')
                            else:
                                print('Não tens dinheiro suficiente')
                        else:
                            print('Ainda não desbloqueaste esta comida')
                    case 7:
                        if listadecomidas[6][2]==True:
                            qndrobalo=int(input('Quantos robalos queres comprar? '))
                            if guito>=(qndrobalo*13.5):
                                print('Isso vai custar {}€ ,tens {}€'.format(qndrobalo*13.5,guito))
                                opsnrobalo=str(input('Queres comprar [S/N]')).lower()
                                if opsnrobalo=='s':
                                    guito=guito-(qndrobalo*13.5)
                                    conquistacomidas+=1
                                    listaqnd[6]+=qndrobalo
                                    print('Tens agora {} robalos'.format(listaqnd[6]))
                                elif opsnrobalo=='n':
                                    print('Compra cancelada')
                                else:
                                    print('Compra inválida')
            #agr vais fazer o ultimo caso que é os gajos pedirem a comida que quiserem a qnd que quiserem e tens de ver se ha dessa comida ou a da qnd suficiente dps podes aceitar o pedido ou recusar se recusares e podias dar a comida perdes guito se recusares e nao puderes dar a comida n ganhas nada  se aceitares e poderes dar a comida recebes a guita da comida se aceitares e n puderes dar ao cliente a comida perdes guito
            case 5:
                comidaqquerem=random.randint(0,6)
                qntcomida=random.randint(1,8)
                print('Eu queria {} doses de {}, por favor.'.format(qntcomida,listadecomidas[comidaqquerem][0],))
                aceitrecus=str(input('Queres aceitar o pedido? [A (Aceitar)/R (Recusar)] ')).lower()
                if aceitrecus=='a':
                    conquistas[3][2]+=1
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
                    conquistas[3][2]+=1
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
                if opcodigo=='\gordo':
                    musicagordo=pygame.mixer.music.load('minefood.mp3')
                    pygame.mixer.music.play()
                    print('Desbloqueaste mais 99 comidas de cada comida que tinhas desbloqueado')
                    for i in range(0,7):
                        if listadecomidas[i][2]==True:
                            conquistacomidas+=99
                            listaqnd[i]+=99
                    while pygame.mixer.music.get_busy() is True:
                        conquistacodigo=True
                elif opcodigo=='\_ayrton_senna':
                    
                    musicasenna=pygame.mixer.music.load('1223.mp3')
                    pygame.mixer.music.play()
                    #Sugerido por Lucas :) (mi amigo),(A musica tbm)
                    print('AAAAAYYYYYRRRRTOOONNN SSSSEEEEENNNNNAAAAA DO BBBBRRRRAAAAASSSSSSIIIIIIILLLLLLL!!!!!')
                    print('Desbloqueaste todas as comidas')
                    for i in range(3,7):
                        conquistadesbloquear+=1
                        listadecomidas[i][2]=True
                    pygame.time.delay(1000)
                    while pygame.mixer.music.get_busy() is True:
                        conquistacodigo=True
                elif opcodigo=='\cold_desert':
                    musicamoney=pygame.mixer.music.load('mony.mp3')
                    pygame.mixer.music.play()
                    guito+=1000000000
                    print('Tens agora 1B€')
                    while pygame.mixer.music.get_busy() is True:
                        conquistacodigo=True
                elif opcodigo=='\_fuck_the_story_I_want_the_achievments':
                    conquistacodigo=True
                    for i in range(0,9):
                        musicaconquista1=pygame.mixer.music.load('minerare.mp3')
                        pygame.mixer.music.play()
                        conquistas[i][1]=True
                    while pygame.mixer.music.get_busy() is True:
                        conquistacodigo=True
                else:
                    print('O código está errado')
                
            
            case 7 :
                print('Estas são as conquistas:')
                for i in range(0,9):
                            print('{}:{}'.format(conquistas[i][0],conquistas[i][1]))
            case 8:
                print('Comidas desbloqueadas: {}\nClientes atendidos: {}\nComidas compradas: {}\nCódigos usados: {}'.format(conquistadesbloquear,conquistaclientes,conquistacomidas,conquistacodigo))
                
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
