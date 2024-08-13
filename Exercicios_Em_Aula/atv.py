#Operadores Condicionais
#Codicionais Simples

#Verifique se um número é positivo
numero = 5

if numero > 0:
  print("Numero é positivo")
  
else:
  print("Numero negativo")
  

#Verifique se uma palavra contém mais de 5 caracteres

palavra = "aaaaaaaaaa"

if len(palavra) > 5:
  print("Palavra tem mais de 5 caracteres")
  
else:
  print("Palavra tem menos de 5 caracteres")
  
  
#Verifique se um ano é bissexto
ano = 2024
if(ano % 4 == 0 and ano 100 != 0)or(ano % 400 == 0):
  print("O ano é bissexto")

else:
  print('O ano nao é bissexto')
  
  
#Verifique se um numero esta entre 10 e 20
numero = 21
if numero >= 10 and numero <= 20:
  print("O numero esta entre 10 e 20")
else:
  print('O numero nao esta entre 10 e 20')
  
  
#Verifique se uma string contem letras e numeros

palavraQualquer = "Bigode123"

if palavraQualquer.isalnum() == True:
  print("A palavra contem letras ou numeros")
  
else:
  print("A palavra nao contem letras ou numeros")
  

#Verificar a faixa etária de uma pessoa

idade = 25

if idade < 13:
  print("Criança")
elif idade < 18:
  print("Adolescente")
elif idade < 60:
  print("Adulto")
else:
  print("Idoso")
  
  
#Determine a estacao do ano baseada no mes

mes = 5

if mes in [6, 7, 8]:
  print("Inverno")
elif mes in [9, 10, 11]:  
  print("Primavera")
elif mes in [12, 13, 14]:
  print("Verao")
elif mes in [15, 16, 17]:
  print("Outono")
else:
  print("Mes Invalido")
  
#imprima os numeros de 1 a 10
for i in range(1, 11):
  print(i)
  
#imprima os elementos de uma lista
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)
  
#Imprima os elementos de um dicionario
dicionario = {'a':1, 'b':2, 'c':3}
print(dicionario)

#Imrpima os numerows de 1 a 10 usando o laco while

i = 1

while i <= 10:
  print(i)
  i += 1


#Imprima os elementos de um dicionário até
#encontrar um valor específico.
