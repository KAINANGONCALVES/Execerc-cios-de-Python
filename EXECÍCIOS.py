#nome 
nome = input('Qual é seu nome?')
idade = input('Qual é sua idade?')
peso = input('Qual é seu peso')
print(nome, idade, peso)

#Mes
nome = input ('olá, poderia me dizer seu nome?')
print('olá,',nome,'seja muito bem vindo')
print('Qual é sua data de nacimento?')
dia = input ('que dia voce nasceu?')
mes = input ('qual mes voce nasceu?')
ano = input ('qual ano vc nasceu?')
print ('voce nasceu no',dia,'do',mes,'do',ano)

#soma
n1 = int(input('valor 1'))
s = n1 - 1
m = n1 + 1

print('antes {}, é {},depois de {} é {}'.format(n1,s,n1,m))

#raiz
n1 = int(input('valor 1'))
d = n1 * 2
t = n1 * 3
r = n1**(1/2)
print('o dobro do valor de {} é {} e seu tripo é {} e sua raiz quadrada é {:.3f}'.format(n1,d,t,r))

#media 
n1 = float(input('Nota 1'))
n2 = float(input('Nota 2'))
n3 = float(input('nota 3'))
s = (n1 + n2 + n3)/3
print('A media desse aluno é {}'.format(s))

#tabuada 
n1 = int(input('Digite um número'))
M1 = n1 * 1
M2 = n1 * 2
M3 = n1 * 3
M4 = n1 * 4
M5 = n1 * 5
M6 = n1 * 6
M7 = n1 * 7
M8 = n1 * 8
M9 = n1 * 9
M10 = n1 * 10
print('A tabuada do {} é \n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(n1,M1,M2,M3,M4,M5,M6,M7,M8,M9,M10))


#jeito bonito
num = int(input('Digite um número para ver sua tabuada:'))
print('-'* 12)
print('{} x {} = {}'.format(num,1,num*1))
print('{} x {} = {}'.format(num,2,num*2))
print('{} x {} = {}'.format(num,3,num*3))
print('{} x {} = {}'.format(num,4,num*4))
print('{} x {} = {}'.format(num,5,num*5))
print('{} x {} = {}'.format(num,6,num*6))
print('{} x {} = {}'.format(num,7,num*7))
print('{} x {} = {}'.format(num,8,num*8))
print('{} x {} = {}'.format(num,9,num*9))
print('{} x {} = {}'.format(num,10,num*10))
print('-'*12)

#medida
medida = float(input('Uma distencia'))
cm = medida * 100
mm = medida * 1000
print('A medida de {} M  coresponde a {} cm e {} mm'. format(medida,cm,mm))

#convertor
real = float(input('Digite a quantidade que voce tem na carteira R$ '))
dolar = real / 5.33
print('Com R${:.2f} voce pode comprar U$ {:.2f} em dolar '.format(real,dolar))

#tinta                                                            
larg = float(input('Qual é a largura da sua parede'))
alt =  float(input('Qual é a altura da sua parede'))
área =  larg * alt
print('A {}m² x {}m² tem o total de {} m²'.format(larg,alt,área))
tinta = área / 2
print('Para pintar sua parede {}m² voce va

# desconto
preço = float(input('Qual é o preço do produto R$: '))
novo = preço - (preço * 5/ 100)
print('O desconto de 5% do valor de R$ {:.2f} correspode a R$ {:.2f} '.format(preço,novo))

#aumento 
nome = input('qual é seu nome?')
salario = float(input('qual é o seu salário R$: '))
novo = salario + (salario * 15/ 100)
print('{},o aumento de 15% do seu Salário R$ {:.2f} correspode a R$ {:.2f} '.format(nome,salario,novo))

#fazer
c = float(input('informe a temperatura °C:'))
f = ((9*c)/5)+32
print('A temperatura de {}°C corresponde a {}°F'.format(c,f))

#aluguel       
D = int(input('quantos dias voce ficou com o carro'))
km = float(input('quantos Km rodados?'))
soma = (D * 60) + (km * 0.15)
print('O total que voce vai pagar pelo aluguel é R${:.2f}'.format(soma))

#segunda leva de exercicios

#ex 01
import math
num = float(input('Digite um valor'))
print('O valor inteiro de {} é {}'.format(num,math.trunc(num)))

num = float(input('Digite um valor'))
print('O valor inteiro de {} é {}'.format(num,int(num)))

#ex 02
co = float(input('Conprimento do cateto oposto'))
ca = float(input('Conprimento do cateto adjacente'))
hi = (co ** 2 + ca ** 2 ) **(1/2)
print('{:.2f}'.format(hi))
      
#ex 03
import math
angulo = float(input('digite o ângulo'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente =  math.tan(math.radians(angulo))
print('{:.2f} {:.2f} {:.2f}'.format(seno,cosseno,tangente))

#ex 04
import random
n1 = input('Diga um nome de aluno (a)')
n2 = input('Diga um nome de aluno (a)')
n3 = input('Diga um nome de aluno (a)')
n4 = input('Diga um nome de aluno (a)')
lista = [n1,n2,n3,n4]
escolha = random.choice(lista)
print('O aluno que foi sorteado é {}'.format(escolha))

#ex 05
import random
n1 = input('nome')
n2 = input('nome')
n3 = input('nome')
n4 = input('nome')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem vai ser:')
print(lista)

#ex 07

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O número {} é formado por:'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))

#ex 08
cid = str(input('Digite um nome de uma cidade')).strip()
print(cid[:6].upper() == 'SANTOS')

#ex 09
nome = str(input('Digite seu nome: '))
print('Só um segundo estamos analisando seu nome...')
print('Em seu nome tem Santos ou Lopes ? {}'.format('santos'in nome.lower()))

#exe 10
frase = str(input('Qual é seu nome? ')).strip().upper()
print('A letra A aparece {}'.format(frase.count('A')))
print('A letra A aparece pela Primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez na posição {}'.format(frase.rfind('A')))

#exe 11
frase = str(input('Qual é seu nome? ')).strip().upper()
print('A letra A aparece {}'.format(frase.count('A')))
print('A letra A aparece pela Primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez na posição {}'.format(frase.rfind('A')))

#exe 12
n = str(input('nome'))
nome  = n.split()
print(nome[0])
print(nome [len(nome)-1])

#exe  13
import random
computador = random.randint(0, 10)
print('=' * 25)
print('Vou escolher um número de 0 a 10')
print('=' * 25)
jogador: int = int(input('Qual número eu pensei ?'))

if jogador == computador:
    print('Você acertou')
else:
    print('Você errou, eu escolhi o número {}'.format(computador))
    
#exe 14
velo = float(input('Qual é sua velocidade'))
if velo > 80:
    print('FOI MULTADO ! você passou do limite de velocidade')
    multa = (velo - 80) * 7
    print('Você vai pagar uma multa de R${:.2f}'.format(multa))
print('Tenha uma ótima viagem ')

#exe 15
numero = int(input('Digite um número'))
resultado = numero % 2
if resultado == 0:
    print('O número é PAR')
else:
    print('O número é Ímpar')
    
#exe 16
distancia = int(input('Qual é a distância da sua viagem: '))
print('A sua viagem tem como distância de {} Km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('A sua viagem de {} km vai sair pelo valor de {:.2f}'.format(distancia, preco))

#exe 17
import datetime
ano = int(input('Qual é o ano: '))
if ano == 0:
    ano == datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é BISSEXTO'.format(ano))
else:
    print('o ano {} é NORMAL'.format(ano))
    
#exe 18
a = int(input('Digite um número'))
b = int(input('Digite mais um número'))
c = int(input('Digite mais outro número'))
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))

#exe 19
salário = float(input('qual seu salário?'))
if salário <= 1250:
    novo = salário + ( salário * 15 / 100 )
else:
    novo = salário + ( salário * 10 / 100 )
print('R${:.2f}'.format(novo))

#exe 20
r1 = float(input('1°Segmento'))
r2 = float(input('2°Segmento'))
r3 = float(input('3°Segmento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel formar um triângulo')
else:
    print('Não é possivel formar um triângulo ')

