import os
import sys
import pymysql
import pandas as pd
from pythonProject.OrcaAcre.orcaAcre import *
from pythonProject.OrcaAcre.variaveis import *
from xhtml2pdf import pisa
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QApplication,QTableWidgetItem,QMessageBox
conn = pymysql.connect(host="satelpjceara.com", port=3306, user="satelp03_marcosh",
                      password="12345678", db="satelp03_acre")
cur = conn.cursor()

class Principal(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnAddEstr.clicked.connect(self.prenchEstruturaMTBT)
        self.btnAddTrafo.clicked.connect(self.prenchTrafo)
        self.btnAddAterramento.clicked.connect(self.prenchAterramento)
        self.btnAddEqui.clicked.connect(self.prenchEquipamento)
        self.btnCondutorMTComp.clicked.connect(self.prenchCondutoresMTCOMP)
        self.btnCondutorMTNU.clicked.connect(self.prenchCondutoresMTNU)##
        self.btnAddCondutorBT.clicked.connect(self.prenchCondBT)
        self.btnAddPoste.clicked.connect(self.prencherPoste)
        self.btnAddEstai.clicked.connect(self.prencherEstai)
        self.btnAddKitEstribo.clicked.connect(self.preencherKitEstribo)
        self.btnaddKitInterno.clicked.connect(self.preencherKitinerno)
        self.btnGeraPDF.clicked.connect(self.geraPdf)
        self.btn_remover.clicked.connect(self.removerItem)
        self.btnTeste.clicked.connect(self.teste)




        row = 0
        while row <=40:
            self.tbKit.setItem(row, 0, QTableWidgetItem(''))
            row = row+1

        row_w = 0
        while row_w <= 40:
            self.tb_detalhamento.setItem(row_w, 0, QTableWidgetItem(''))
            row_w = row_w + 1





        sql = "SELECT item,categoria FROM satelp03_acre.tb_base"
        loadEquipamentos = pd.read_sql(sql,conn).values.tolist()
        x = 0
        while loadEquipamentos[x][1] == 'ESTRUTURAS MT/BT':
            self.ddlEstruturas.addItem(loadEquipamentos[x][0])
            x = x+1


        while loadEquipamentos[x][1] == 'TRANSFORMADORES':
            self.ddlTrafo.addItem(loadEquipamentos[x][0])
            x = x + 1
        while loadEquipamentos[x][1] == 'ATERRAMENTOS':
            self.ddlAterramento.addItem(loadEquipamentos[x][0])
            x = x + 1
        while loadEquipamentos[x][1] == 'EQUIPAMENTOS':
            self.ddlEqup.addItem(loadEquipamentos[x][0])
            x = x + 1
        while loadEquipamentos[x][1] == 'CONDUTORES MT COMP':
            self.ddlCondutorMTComp.addItem(loadEquipamentos[x][0])
            x = x + 1
        while loadEquipamentos[x][1] == 'CONDUTORES MT NU':
            self.ddlCondutorMTNU.addItem(loadEquipamentos[x][0])
            x = x + 1
        while loadEquipamentos[x][1] == 'CONDUTORES BT':
            self.ddlCondutorBT.addItem(loadEquipamentos[x][0])
            x = x + 1
        while loadEquipamentos[x][1] == 'POSTES':
            self.ddlPoste.addItem(loadEquipamentos[x][0])
            x = x + 1


    def prenchEstruturaMTBT(self):
        estruturasMTBT = str(self.ddlEstruturas.currentText())
        qtdEstruMTBT = str(self.spnEstrMTBT.text())
        try:
            ver = False
            row = 0
            while ver == False:
                if self.tbKit.item(row, 0).text() != '':
                    row = row + 1
                else:
                    self.tbKit.setItem(row, 0, QTableWidgetItem(estruturasMTBT))
                    self.tbKit.setItem(row, 1, QTableWidgetItem(qtdEstruMTBT))
                    ver = True
            self.prencheDetalhamento(estruturasMTBT)


        except:
            print('erro')



    def prenchTrafo(self):
        trafo = self.ddlTrafo.currentText()
        qtdtrafo = self.spinTrafo.text()
        try:
            ver = False
            row = 0
            while ver == False:
                if self.tbKit.item(row, 0).text() != '':
                    row = row + 1
                else:
                    self.tbKit.setItem(row, 0, QTableWidgetItem(trafo))
                    self.tbKit.setItem(row, 1, QTableWidgetItem(qtdtrafo))
                    ver = True
            self.prencheDetalhamento(trafo)

        except:
            print('erro')
        self.prencheDetalhamento(trafo)



    def prenchAterramento(self):
        aterramento = self.ddlAterramento.currentText()
        qtdAterramento = self.spinAterramento.text()

        try:
            ver = False
            row = 0
            while ver == False:
                if self.tbKit.item(row, 0).text() != '':
                    row = row + 1
                else:
                    self.tbKit.setItem(row, 0, QTableWidgetItem(aterramento))
                    self.tbKit.setItem(row, 1, QTableWidgetItem(qtdAterramento))
                    ver = True
        except:
            print('erro Aterramento')
        self.prencheDetalhamento(aterramento)

    def prenchEquipamento(self):
        equipamento = self.ddlEqup.currentText()
        qtdEquipamento = self.spinEquip.text()
        try:
            ver = False
            row = 0
            while ver == False:
                if self.tbKit.item(row, 0).text() != '':
                    row = row + 1
                else:
                    self.tbKit.setItem(row, 0, QTableWidgetItem(equipamento))
                    self.tbKit.setItem(row, 1, QTableWidgetItem(qtdEquipamento))
                    ver = True
        except:
            print('erro Equipamento')
        self.prencheDetalhamento(equipamento)

    def prenchCondutoresMTCOMP(self):
        conduroresMT = self.ddlCondutorMTComp.currentText()
        qtdCondMT = self.spinCondutorMTComp.text()
        try:
            ver = False
            row = 0
            while ver == False:
                if self.tbKit.item(row, 0).text() != '':
                    row = row + 1
                else:
                    self.tbKit.setItem(row, 0, QTableWidgetItem(conduroresMT))
                    self.tbKit.setItem(row, 1, QTableWidgetItem(qtdCondMT))
                    ver = True
        except:
            print('erro')
        self.prencheDetalhamento(conduroresMT)


    def prenchCondutoresMTNU(self):
        conduroresMTNU = self.ddlCondutorMTNU.currentText()
        qtdCondMTNU = self.spinCondutorMTNU.text()
        try:
            ver = False
            row = 0
            while ver == False:
                if self.tbKit.item(row, 0).text() != '':
                    row = row + 1
                else:
                    self.tbKit.setItem(row, 0, QTableWidgetItem(conduroresMTNU))
                    self.tbKit.setItem(row, 1, QTableWidgetItem(qtdCondMTNU))
                    ver = True
        except:
            print('erro')
        self.prencheDetalhamento(conduroresMTNU)

    def prenchCondBT(self):
        condutorBT = self.ddlCondutorBT.currentText()
        qtdCondBT = self.spinCondutorBT.text()
        try:
            ver = False
            row = 0
            while ver == False:
                if self.tbKit.item(row, 0).text() != '':
                    row = row + 1
                else:
                    self.tbKit.setItem(row, 0, QTableWidgetItem(condutorBT))
                    self.tbKit.setItem(row, 1, QTableWidgetItem(qtdCondBT))
                    ver = True
        except:
            print('erro')
        self.prencheDetalhamento(condutorBT)

    def prencherPoste(self):
        poste = self.ddlPoste.currentText()
        qtdposte = self.spinPoste.text()
        try:
            ver = False
            row = 0
            while ver == False:
                if self.tbKit.item(row, 0).text() != '':
                    row = row + 1
                else:
                    self.tbKit.setItem(row, 0, QTableWidgetItem(poste))
                    self.tbKit.setItem(row, 1, QTableWidgetItem(qtdposte))
                    ver = True
        except:
            print('erro')
        self.prencheDetalhamento(poste)

    def prencherEstai(self):
        estai = self.ddlEstai.currentText()
        qtdEstai = self.spinEstai.text()
        try:
            ver = False
            row = 0
            while ver == False:
                if self.tbKit.item(row, 0).text() != '':
                    row = row + 1
                else:
                    self.tbKit.setItem(row, 0, QTableWidgetItem(estai))
                    self.tbKit.setItem(row, 1, QTableWidgetItem(qtdEstai))
                    ver = True
        except:
            print('erro')

        self.prencheDetalhamento(estai)

    def preencherKitEstribo(self):
        KitEstribo = self.ddlKitEstribo.currentText()
        qtdKitEstribo = self.spinKitEstribo.text()
        try:
            ver = False
            row = 0
            while ver == False:
                if self.tbKit.item(row, 0).text() != '':
                    row = row + 1
                else:
                    self.tbKit.setItem(row, 0, QTableWidgetItem(KitEstribo))
                    self.tbKit.setItem(row, 1, QTableWidgetItem(qtdKitEstribo))
                    ver = True
        except:
            print('erro')
        self.prencheDetalhamento(KitEstribo)


    def preencherKitinerno(self):
        Kitinerno = self.ddlKitInterno.currentText()
        qtdKitinerno = self.spinKitInterno.text()
        try:
            ver = False
            row = 0
            while ver == False:
                if self.tbKit.item(row, 0).text() != None:
                    row = row + 1
                else:
                    self.tbKit.setItem(row, 0, QTableWidgetItem(Kitinerno))
                    self.tbKit.setItem(row, 1, QTableWidgetItem(qtdKitinerno))
                    ver = True
        except:
            print('erro')

    def removerItem(self):
        try:
            deleteRow = self.tbKit.currentRow()
            self.tbKit.removeRow(deleteRow)
        except:
            print('erro')


    def prencheDetalhamento(self, item):
        try:

            sql = f"SELECT cod_eac,descricao_do_kit,un,valor_unitario " \
                  f"FROM satelp03_acre.tb_base15 where estrutura like '%{item}%' "
            df = pd.read_sql(sql, conn)
            cod_eac = df.iloc[:, 0]
            descricao_do_kit = df.iloc[:, 1]
            un = df.iloc[:, 2]
            valor_unitario = df.iloc[:, 3]
            lista = df.values.tolist()
            ver = False
            row = 0
            print(ver)
            while ver == False:
                print(ver)
                if self.tb_detalhamento.item(row, 0).text() != '':
                    row = row + 1
                else:
                    print('chegou aquiok')
                    x = row
                    for i, linha in enumerate(lista):
                        self.tb_detalhamento.setItem(x, 0, QTableWidgetItem(str(cod_eac[i])))
                        self.tb_detalhamento.setItem(x, 1, QTableWidgetItem('energisa'))
                        self.tb_detalhamento.setItem(x, 2, QTableWidgetItem(str(descricao_do_kit[i])))
                        self.tb_detalhamento.setItem(x, 3, QTableWidgetItem(str(un[i])))
                        self.tb_detalhamento.setItem(x, 4, QTableWidgetItem(str(valor_unitario[i])))
                        x = x + 1
                    ver = True

        except:
            print('erro')




    def geraPdf(self):
        hoje = (datetime.now().strftime('%d/%m/%Y'))
        local = os.getcwd()
        print(local)
        destino = os.getcwd() + '/Comprovantes/'
        try:

            output_filename = destino  + "orcamento.pdf"
            source_html = fonte.replace('#HOJE',hoje)
            result_file = open(output_filename, "w+b")
            pisa_status = pisa.CreatePDF(source_html, dest=result_file)
            result_file.close()
            QMessageBox.about(self, "OK", "Comprovante Gerada!")
            return pisa_status.err
        except:
            print('f')


    def teste(self):
        item = 'U4'
        sql = f"SELECT cod_eac,descricao_do_kit,un,valor_unitario " \
              f"FROM satelp03_acre.tb_base15 where estrutura like '%{item}%' "
        df = pd.read_sql(sql, conn)
        cod_eac = df.iloc[:, 0]
        descricao_do_kit = df.iloc[:, 1]
        un = df.iloc[:, 2]
        valor_unitario = df.iloc[:, 3]
        lista = df.values.tolist()

        ver = False
        row = 0
        print(ver)
        while ver == False:
            print(ver)
            if self.tb_detalhamento.item(row, 0).text() != '':
                row = row + 1
            else:
                print('chegou aquiok')
                x = row
                for i, linha in enumerate(lista):
                    self.tb_detalhamento.setItem(x, 0, QTableWidgetItem(str(cod_eac[i])))
                    self.tb_detalhamento.setItem(x, 1, QTableWidgetItem('energisa'))
                    self.tb_detalhamento.setItem(x, 2, QTableWidgetItem(str(descricao_do_kit[i])))
                    self.tb_detalhamento.setItem(x, 3, QTableWidgetItem(str(un[i])))
                    self.tb_detalhamento.setItem(x, 4, QTableWidgetItem(str(valor_unitario[i])))
                    x = x+1
                ver = True


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    cap = Principal()
    cap.show()
    qt.exec_()