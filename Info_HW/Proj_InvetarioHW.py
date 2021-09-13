# codigo do Projeto Python com Pandas - DIO Cognizant
# ler dados excel (plan de Invetario Hardware) e fazer estatisticas com graficos
# André R Mendes - 09/21

# importando a biblioteca Pandas e colocando um apelido
import pandas as pd

# ler os dados da planilha inventario hardware.
df = pd.read_excel('Inventario21.xlsx')  #plan tem este nome e esta no mesmo dir

# imprime nome das colunas
print(df.columns)

#import biblioteca d egraficos
import matplotlib.pyplot as plt

#estatisticas coluna memoria
df["Memória"] = df["Memória"].astype("str")             #transformando a coluna memoria em string para ceitar grafico
df["Memória"].value_counts().plot.bar(title="Memória: Capacidade X Qtd.", rot=0)
plt.ylabel('Quantidade', color="Red")                    #rotulo eixo y e a cor do texto
plt.xlabel('Capacidade', color="Red")                    #rotulo exixo e a cor
plt.savefig('Memoria.jpg', format='jpg')                       #salva a imagem em arquivo jpg
plt.show()                                                     #mostra o grafico na tela

#estatisticas coluna Processador
df["Processador"] = df["Processador"].astype("str")                                            #transformando a coluna memoria em string para ceitar grafico
df["Processador"].value_counts().plot.bar(title="Processador: Tipo X Qtd.", rot=0, fontsize=9)
plt.ylabel('Quantidade', color="Red")                                                          #rotulo eixo y e a cor do texto
plt.xlabel('Tipo', color="Red")                                                                #rotulo exixo e a cor
#plt.savefig('Tipo_Proc.jpg', format='jpg')                                                    #salva a imagem em arquivo png
plt.show()

#Estatisticas Proprietarios
df["Proprietário"].value_counts().plot.pie(title="Proprietários.", rot=0, fontsize=9)
plt.show()

#Estatisticas Sistema Operacional
df["S.O."].value_counts().plot.pie(title="Sistemas Operacionais.", rot=0, fontsize=9)
plt.show()

#Estatisticas Marcas
df["Marca"].value_counts().plot.pie(title="Marcas.", rot=0, fontsize=9)
plt.show()

#Estatisticas HD
df["HD"].value_counts().plot.pie(title="Tipo e Capacidade de HD.", rot=0, fontsize=7)
plt.show()


