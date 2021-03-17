import pandas as pd
import pymysql

conn = pymysql.connect(host="satelpjceara.com", port=3306, user="satelp03_marcosh",
                      password="12345678", db="tb_base15")
cur = conn.cursor()




