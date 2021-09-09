# codigo de testes inicial com biblioteca pandas
# lerdados de uma planilha em excel
# André R Mendes - 09/21

# importando a biblioteca Pandas e colocando um apelido
import pandas as pd

# so comandos para testes e aprendizado inicial com frase
# f = "Teste com uma Frase"
# print(f)          #imprimie frase inteira
# print(f[0])       #imprime só o caracter da posição 1 da frase
# print(f[0:10])    #imprimir os caracterers de 0 ate 9 da frase = total 10 caracteres
# print(f[:12])     #imprimir até o 11 caracter d afrase
# print(f.count("Teste"))  #conta quantas vezes a palavra teste aparece na frase
# print(f.lower())   #altera todos caracteres para minustulo
# print(f.upper())   #muda tudo para maiuculo
# print(f.replace("Teste", "Testando"))   #muda a palavra teste por testando na frase

# ler os dados de uma planilha excel e trabalhar com os dados para testes e aprendizado.


df = pd.read_excel('/temp/python/examespacs.xlsx')           #ler a planilha
print(df.head())                                             #imprimir 5 linhas
print(df.dtypes)                                            #imprimi tipo de dados dos campo
print(df.columns)                                           #imprime nome das colunas
print(df["Data Realizado"])                                 #imprimindo valores coluna Dados realizado




