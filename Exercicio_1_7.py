lista_prenomes = ['Adriana', 'Beatriz','Monica','Pedro','Roberto']
lista_sobrenomes = ['Bauer','Santos','Souza','Silva','Pontes']

if(len(lista_prenomes) != len(lista_sobrenomes)):
    print('A quantidade de informações nas listas é diferente')
    print('Qtd. nomes: '+str(len(lista_prenomes)))
    print('Qtd. sobrenomes: '+str(len(lista_sobrenomes)))
else:
    for indice in range(len(lista_prenomes)):
        print('Nome completo: ' + lista_prenomes[indice]+' '+lista_sobrenomes[indice])
    

#2. Crie uma lista de números desordenada (pelo menos 10) e retorne uma lista ordenada dos pares desses números.

from random import randint

def criar_lista_inteiros(qtd_numeros,num_inicial, num_final):
    i = 0
    lista_inteiros = []
    while(i<qtd_numeros):
        lista_inteiros.append(randint(num_inicial,num_final))        
        i += 1
    return lista_inteiros

def retornar_pares(lista_numeros):
    lista_num_pares = []
    for numero in lista_numeros:
        if numero%2 == 0:
            lista_num_pares.append(numero)
    lista_num_pares.sort()
    return lista_num_pares

minha_lista = criar_lista_inteiros(15,0,1000)
print(minha_lista)
print(retornar_pares(minha_lista))

#3. Peça o nome completo de uma pessoa e veja se realmente ela digitou o nome completo ou só o primeiro nome.

nome_completo = input('Digite o seu nome completo: ')

nome_esta_completo = True
msg = 'O nome está completo'

if nome_completo.find(' ') < 0: 
    nome_esta_completo = False
    msg = 'O nome não está completo'

print(msg)

#4. Peça a data de nascimento de uma pessoa e responda se ela já pode votar, se já pode dirigir um carro, e se pode concorrer à presidência do Brasil.

from datetime import datetime

data_nascimento = input('Digite a sua data de nascimento: ')

ano_atual = 2022
mes_atual = 1
dia_atual = 18

data_aux = data_nascimento.split('/')
dia_nascimento = int(data_aux[0])
mes_nascimento = int(data_aux[1])
ano_nascimento = int(data_aux[2])

idade = ano_atual - ano_nascimento

if mes_atual < mes_nascimento or (mes_atual == mes_nascimento and dia_atual < dia_nascimento):
    idade -= 1

podeVotar = False
podeDirigir = False
podeSerPresidente = False

if idade >= 35:
    podeVotar = True
    podeDirigir = True
    podeSerPresidente = True
elif idade >= 18:
    podeVotar = True
    podeDirigir = True
elif idade >= 16:
    podeVotar = True

print(f'Pode votar: {podeVotar}, Pode dirigir: {podeDirigir}, Pode ser candidato a presidente: {podeSerPresidente}')


#5. Peça os dados de altura e diâmetro, e calcule o volume do cilindro com 4 casas decimais de aproximação.
# π r² h

import math

val_altura = -1
val_diametro = -1

while val_altura < 0:
    val_altura = float(input('Digite a altura do cilindro (cm): '))
    
while val_diametro < 0:
    val_diametro = float(input('Digite o diametro (cm): '))
    
val_raio = val_diametro / 2

val_volume = math.pi * (val_raio**2) * val_altura
    
print(f'Volume: {val_volume:,.4f}')

# 6. Crie um menu repetitivo que sempre pergunte `[a]dicionar, [s]ubtrair, [m]ostrar resultado ou [t]erminar o programa`. 
# Quando escolhido um dos primeiros itens, adicione ou subtraia o valor informado posteriormente; 
# quando escolhido o terceiro item, mostre o resultado; e quando escolhido o último, pare de repetir o menu.

def exibir_menu():
     print('[a]dicionar')
     print('[s]ubtrair')
     print('[m]ostrar resultado')
     print('[t]erminar o programa)')

resultado = 'Nenhuma operaçao feita ainda'
while True:
    exibir_menu
    opcao_selecionada = input('Digite a opção desejada: ')
    
    if opcao_selecionada == 't':
        print('Saindo....')
        break
    elif opcao_selecionada == 'a':
        numero1 = float(input('Digite o primeiro numero: '))
        numero2 = float(input('Digite o segundo numero: '))
        resultado = numero1 + numero2
    elif opcao_selecionada == 's':
        numero1 = float(input('Digite o primeiro numero: '))
        numero2 = float(input('Digite o segundo numero: '))
        resultado = numero1 - numero2
    elif opcao_selecionada == 'm':
        print(f'Resultado: {resultado: >10}')
    else:
        print('Opcao invalida')
        
#7. Defina uma string e retorne a reversa dela (sem usar o método `.reverse()`)

def funcao_inverter_string(palavra):
    tamanho = len(palavra)-1
    inverso = ''
    
    while tamanho > -1:
        inverso = inverso + palavra[tamanho]
        tamanho-=1
        
    return  inverso
    
print(funcao_inverter_string("Maria Antonieta"))
