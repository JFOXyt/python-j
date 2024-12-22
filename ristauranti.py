import random

listadecomidas=[['Estrogonofe',10.5,True],['Rojões',8.5,True],['Massa com atum',8,True],['Francesinha',20,False],['Bife',13.5,False],['Costeletas',15.5,False],['Robalo',13.5,False]]
listaqnd=[5,5,5,0,0,0,0]

print('Tu és o gerente este restaurante!!')
print('Modos de jogo:')
print('[1]Fácil (Começas com 1000)\n[2]Médio (Começas com 500)\n[3]Difícil (Começas com 300)\n[4]Hardcore (Começas com 100)')
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
        print('[1]Desbloquear comidas\n[2]Ver stock\n[3]Ver dinheiro\n[4]Comprar comidas\n[5]Próximo cliente')
        op=int(input(('Qual vais escolher? ')))

        match op:

            case 1:

                print('Que comidas queres comprar?')
                print('[1]Francesinha (preço para desbloquear 250)\n[2]Bife (preço para desbloquear 200)\n[3]Costeletas de frango (preço para desbloquar 220\n[4]Robalo (preço para desbloquar 210) ')
                opdesbloquearcomida=int(input('Qual queres comprar? '))
                match opdesbloquearcomida:
                    case 1:
                        if listadecomidas[3][2]==False:
                            if guito>=250:
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
                            if guito>=qndestrogonofe*10.5:
                                guito= guito - (qndestrogonofe*10.5)
                                listaqnd[0]+=qndestrogonofe
                                print('Tens agora {} estrogonofes'.format(listaqnd[0]))
                            else:
                                print('Não tens dinheiro suficiente ')
                        else:
                            print('Ainda não desbloqueaste esta comida')
                    case 2:
                        if listadecomidas[1][2]==True:
                            qndrojoes=int(input('Quantos rojões queres comprar? '))
                            if guito>=qndrojoes*8.5:
                                guito=guito-(qndrojoes*8.5)
                                listaqnd[1]+=qndrojoes
                            else:
                                print('Não tens dinheiro suficiente')