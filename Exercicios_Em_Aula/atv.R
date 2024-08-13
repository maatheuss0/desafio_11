#Operadores Condicionais
#Codicionais Simples

#Verifique se um número é positivo
numero <- 5

if (numero > 0){
  print("Numero é positivo")
}else{
  print("Numero negativo")
}

#Verifique se uma palavra contém mais de 5 caracteres

palavra = "aaaaaaa"

if (nchar(palavra) > 5){
  print("Palavra tem mais de 5 caracteres")
}else{
  print("Palavra tem menos de 5 caracteres")
}


#Verifique se um ano é bissexto
ano <- 2024
if(ano %% 4 == 0 && ano %% 100 != 0){
  print("O ano é bissexto")
}
else{
  print('O ano nao é bissexto')
}

#Verifique se um numero esta entre 10 e 20
numero <- 15
if(numero >= 10 & numero <= 20){
  print("O numero esta entre 10 e 20")
}else{
  print('O numero nao esta entre 10 e 20')
}

#Verifique se uma string contem letras e numeros

palavraQualquer <- "Bigode"

if(any(grepl("[A-Za-z]",palavraQualquer)) & any(grepl("[0-9]",palavraQualquer))){
  print("A string possui letras e numeros")  
}else{
  print("A string nao possui letras e numeros")
}

#Determine a estacao do ano baseada no mes

mes <- 5

if (mes %in% c(6,7,8)) {
  print("Inverno")
} else if (mes %in% c(9,10,11)) {  
  print("Primavera")
} else if (mes %in% c(12,1,2)) {
  print("Verão")
} else if (mes %in% c(3,4,5)) {
  print("Outono")
} else {
  print("Mês Inválido")
}


#imprima os elementos de uma lista
lista = c(1,2,3,4,5)
for (elemento in lista){
  print(elemento)
}

#Imrpima os numerows de 1 a 10 usando o laco while

i <- 1

while (i<=10){
  print(i)
  i <- i+1
}