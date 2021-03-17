import pandas as pd
import psycopg2


conn = psycopg2.connect(database='cap',host='localhost', user='postgres', password='postgres')
cur = conn.cursor()
#limpar = 'truncate tb_bi'  #comando para Limpar a tabela
#cur.execute(limpar)


df = pd.read_excel('teste.xlsx') # sintaxe pd.read_excel('caminho_do_arquivo completo",'NomePLanilha')

print(df)
etapa = df.iloc[:,0]
estoque = df.iloc[:,1]
faixa_prazo = df.iloc[:,2]
status = df.iloc[: ,3]
numero_ordem = df.iloc[: ,4]
numero_cliente = df.iloc[: ,5]
estado_os = df.iloc[: ,6]
des_servico = df.iloc[: ,7]
descricao_etapa = df.iloc[: ,8]
descricao_estado = df.iloc[: ,9]
data_ingresso = df.iloc[: ,10]
data_estado_format = df.iloc[: ,11]
tempo_total = df.iloc[: ,12]
prazo = df.iloc[: ,13]
regional = df.iloc[:,14]
lista = df.values.tolist()


for i, row in enumerate(lista):
    sql = (f"INSERT INTO tb_daniel(etapa,estoque,faixa_prazo,status,"
           f"numero_ordem,numero_cliente,estado_os,des_servico,descricao_etapa,"
           f"descricao_estado,data_ingresso,data_estado_format,tempo_total,"
           f"prazo ,regional) VALUES ('{etapa[i]}',"
           f"'{estoque[i]}','{faixa_prazo[i]}','{status[i]}',"
           f"'{numero_ordem[i]}','{numero_cliente[i]}','{estado_os[i]}','{des_servico[i]}',"
           f"'{descricao_etapa[i]}','{descricao_estado[i]}', '{data_ingresso[i]}','{data_estado_format[i]}','{tempo_total[i]}',"
           f"'{prazo[i]}','{regional[i]}')")




    cur.execute(sql)
conn.commit()
conn.close()
print("TB Bi gravado com sucesso")