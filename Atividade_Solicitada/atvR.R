dicionario <- list(a = 1,b = 2,c = 3)

valor_especifico <- 2

for (chave in names(dicionario)) {
  valor <- dicionario[[chave]]
  print(paste("Chave:", chave, ", Valor:", valor))
  if (valor == valor_especifico) {
    break
  }
}
