import pandas as pd
import pymysql

conn = pymysql.connect(host="satelpjceara.com", port=3306, user="satelp03_marcosh",
                      password="12345678", db="satelp03_acre")
cur = conn.cursor()
print('Conexao OK')


df = pd.read_excel('modelos.xlsx','base15') # sintaxe pd.read_excel('caminho_do_arquivo completo",'NomePLanilha')
print(df)
estrutura = df.iloc[:, 0]
codmat = df.iloc[:, 1]
cod_eac = df.iloc[:, 2]
descricao_de_kit = df.iloc[:, 3]
un = df.iloc[:, 4]
quant = df.iloc[:, 5]
qtde_em_campo = df.iloc[:, 6]
valor_unitario = df.iloc[:, 7]
lista = df.values.tolist()

for i, row in enumerate(lista):
    sql = (f"INSERT INTO tb_base15(estrutura,codmat,cod_eac,descricao_do_kit,"
           f"un,quant,qtde_em_campo,valor_unitario) VALUES ('{estrutura[i]}',"
           f"'{codmat[i]}','{cod_eac[i]}','{descricao_de_kit[i]}',"
           f"'{un[i]}','{quant[i]}','{qtde_em_campo[i]}','{valor_unitario[i]}')")

    cur.execute(sql)
conn.commit()
conn.close()
print("TB Bi gravado com sucesso")