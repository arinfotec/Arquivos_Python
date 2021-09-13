# codigo do Projeto Python com Pandas
# ler dados excell (plan de Invetario Hardware) e fazer estatisticas
# André R Mendes - 09/21

# importando a biblioteca Pandas e colocando um apelido
import pandas as pd

# ler os dados da planilha inventario hardware.
df = pd.read_excel('Inventario21.xlsx')  # ler a planilha

print(df.columns)  # imprime nome das colunas
# print(df["S.O."].unique())                                   #imprimindo os tipos de SO
print('Tipos de SO: {}'.format(df["S.O."].unique()))  # imprimi os tipos de SO existente

# filtra e imprimie so os ocmputadores com 4G memoria
#mem = df.loc[df["Memória"] == "4G"]
#print(mem)

import matplotlib.pyplot as plt                         #import biblioteca d egraficos

#estatisticas coluna memoria
df["Memória"] = df["Memória"].astype("str")             #transformando a coluna memoria em string para ceitar grafico
#qtd_men = df.groupby(["Memória"]).count()              #conta mas coloca outras info a mais
#tipo_mem = df["Memória"].unique()                       #obtendo os tipos unicos da coluna memoria
#qtd_mem2 = df["Memória"].value_counts()                 #contando a quantidade de item por capacidade (conta a quantidade de itens iguais
df["Memória"].value_counts().plot.bar(title="Memória: Capacidade X Qtd.", rot=0)  #rot é a toração no texto - exixo
#print(qtd_men)
#print(tipo_mem)
#print(qtd_mem2)
#plt.plot(qtd_men)
#plt.plot(qtd_mem2)
#plt.bar(tipo_mem, qtd_mem2)                             #preparar grafico tipo barras, precisa exio x e y
#plt.title('Memórias Capacidade x Quantidade', color="Red")  #colocando titulo e cor para titulo
plt.ylabel('Quantidade', color="Red")                    #rotulo eixo y e a cor do texto
plt.xlabel('Capacidade', color="Red")                    #rotulo exixo e a cor
#plt.plot(df["Memória"])                                 #mostra o grafico em linha
#plt.savefig('Memoria.jpg', format='jpg')                       #salva a imagem em arquivo png
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
#filtrando duas colunas (processador x memoria y) - lista todos com estes parametros
#print(df[(df['Processador']=='Intel I3') & (df['Memória']=='2G')].value_counts())

#Estatisticas HD
df["HD"].value_counts().plot.pie(title="Tipo e Capacidade de HD.", rot=0, fontsize=7)
plt.show()


