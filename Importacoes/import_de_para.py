import pandas as pd
import pymysql
conn = pymysql.connect(host="satelpjceara.com", port=3306, user="satelp03_marcosh",
                      password="12345678", db="satelp03_acre")
cur = conn.cursor()
#limpar = 'truncate tb_bi'  #comando para Limpar a tabela
#cur.execute(limpar)


df = pd.read_excel('modelos.xlsx','dePara') # sintaxe pd.read_excel('caminho_do_arquivo completo",'NomePLanilha')

print(df)
codigo_energisa = df.iloc[:,0]
codigo_eac = df.iloc[:,1]
descricao_eac = df.iloc[:,2]
valor_unitario = df.iloc[: ,3]

lista = df.values.tolist()

for i, row in enumerate(lista):
    sql = (f"INSERT INTO tb_depara(codigo_energisa,codigo_eac,descricao_eac,valor_unitario) VALUES ('{codigo_energisa[i]}',"
           f"'{codigo_eac[i]}','{descricao_eac[i]}','{valor_unitario[i]}')")

    cur.execute(sql)
conn.commit()
conn.close()
print("gravado com sucesso")