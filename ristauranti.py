import random

listadecomidas=[['Estrogonofe',10.5,True],['Rojões',8.5,True],['Massa com atum',8,True],['Francesinha',20,False],['Bife',13.5,False],['Costeletas de frango',15.5,False],['Robalo',13.5,False]]
listaqnd=[random.randint(1,6),random.randint(1,6),random.randint(1,6),0,0,0,0]

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
    print('O que queres fazer?')
    print('[1]Comprar comidas\n[2]Ver stock\n[3]Ver dinheiro\n[4]Próximo cliente')
    op=int(input(('Qual vais escolher? ')))
    match op:
        case 1:
            print('Que comidas queres comprar?')
            print('[1]Francesinha (preço para desbloquear 250)\n[2]Bife (preço para desbloquear 200)\n[3]Costeletas de frango (preço para desbloquar 220\n[4]Robalo (preço para desbloquar 210) ')
            opcompracomida=int(input('Qual queres comprar? '))
            match opcompracomida:
                case 1:
                    if guito>=250:
                        guito-=250
                        listadecomidas[3][2]=True
                        frannumini=random.randint(1,3)
                        listaaddfran=listaqnd[3]+frannumini
                        listaqnd[3] = listaaddfran
                        print('Desbloquaste a francesinha\n Tens agora como prenda {} francesinha '.format(frannumini))
                    else:
                        print('Não tens dineiro suficiente')
                case 2:
                    if guito>=200:
                        guito-=200
                        listadecomidas[4][2]=True
                        bifenumini=random.randint(1,3)
                        listaaddbife=listaqnd[4]+bifenumini
                        listaqnd[4]=listaaddbife
                        print('Desbloquaste o bife\n Tens agora como prenda {} bife '.format(bifenumini))
                    else:
                        print('Não tens dinheiro suficiente')


