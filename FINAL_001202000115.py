from PyQt5.QtWidgets import (
    QApplication, QWidget, QFormLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel)


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('Alvin Sengkey - FINAL PROJECT - GPA Calculation')
        self.resize(400, 600)

        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.button_addSubject = QPushButton('Add Subject')
        self.button_calculateGPA = QPushButton('Calculate GPA')
        self.valid_message = QLabel('')
        self.valid_message.setStyleSheet('color: #ff2626')
        self.label_result = QLabel('Result:')
        self.result = QLabel('')
        self.A = QLabel('')
        self.Am = QLabel('')
        self.Bp = QLabel('')
        self.B = QLabel('')
        self.Bm = QLabel('')
        self.Cp = QLabel('')
        self.C = QLabel('')
        self.D = QLabel('')
        self.E = QLabel('')
        self.total_index = QLabel('')
        self.total_credit = QLabel('')
        self.gpa = QLabel('')

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Name', 'Score'])

        self.layout.addRow(self.button_addSubject)
        self.layout.addRow(self.button_calculateGPA)
        self.layout.addRow(self.table)
        self.layout.addRow(self.valid_message)
        self.layout.addRow(self.label_result)
        self.layout.addRow(self.result)

        self.button_addSubject.clicked.connect(self.add_row)
        self.button_calculateGPA.clicked.connect(self.gpa_calculation)
        self.table.itemChanged.connect(self.validation)

    def add_row(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)

    def gpa_calculation(self):
        tot_A = 0
        tot_Am = 0
        tot_Bp = 0
        tot_B = 0
        tot_Bm = 0
        tot_Cp = 0
        tot_C = 0
        tot_D = 0
        tot_E = 0
        index_score = 0
        tot_index = 0
        tot_credit = 0
        gpa_result = 0

        for row in range(0, self.table.rowCount()):
            data_score = self.table.item(row, 1)
            if data_score:
                if data_score.text() != '':
                    score = float(data_score.text())
                    if score >= 85:
                        index_score = 4*3
                        tot_credit += 3
                        tot_A += 1
                    elif score >= 80 and score < 85:
                        index_score = 3.67*3
                        tot_credit += 3
                        tot_Am += 1
                    elif score >= 75 and score < 80:
                        index_score = 3.33*3
                        tot_credit += 3
                        tot_Bp += 1
                    elif score >= 70 and score < 75:
                        index_score = 3*3
                        tot_credit += 3
                        tot_B += 1
                    elif score >= 67 and score < 70:
                        index_score = 2.67*3
                        tot_credit += 3
                        tot_Bm += 1
                    elif score >= 64 and score < 67:
                        index_score = 2.33*3
                        tot_credit += 3
                        tot_Cp += 1
                    elif score >= 60 and score < 64:
                        index_score = 2*3
                        tot_credit += 3
                        tot_C += 1
                    elif score >= 55 and score < 60:
                        index_score = 1*3
                        tot_credit += 3
                        tot_D += 1
                    else:
                        index_score = 0*3
                        tot_credit += 3
                        tot_E += 1

                    tot_index += index_score

                    gpa_result = tot_index/tot_credit

        self.resize(400, 750)
        self.layout.addRow(self.A)
        self.layout.addRow(self.Am)
        self.layout.addRow(self.Bp)
        self.layout.addRow(self.B)
        self.layout.addRow(self.Bm)
        self.layout.addRow(self.Cp)
        self.layout.addRow(self.C)
        self.layout.addRow(self.D)
        self.layout.addRow(self.E)
        self.layout.addRow(self.total_index)
        self.layout.addRow(self.total_credit)
        self.layout.addRow(self.gpa)

        self.A.setText('A\t\t:' + str(tot_A))
        self.Am.setText('A-\t\t:' + str(tot_Am))
        self.Bp.setText('B+\t\t:' + str(tot_Bp))
        self.B.setText('B\t\t:' + str(tot_B))
        self.Bm.setText('B-\t\t:' + str(tot_Bm))
        self.Cp.setText('C+\t\t:' + str(tot_Cp))
        self.C.setText('C\t\t:' + str(tot_C))
        self.D.setText('D\t\t:' + str(tot_D))
        self.E.setText('E\t\t:' + str(tot_E))
        self.total_index.setText('Total Index\t:%.2f' % tot_index)
        self.total_credit.setText('Total Credit\t:%.2f' % tot_credit)
        self.gpa.setText('GPA\t\t:%.2f' % gpa_result)

    def validation(self, item):
        col = item.column()
        if col == 1 and not item.text().isnumeric():
            item.setText('')
            self.valid_message.setText('')
        elif col == 1 and (float(item.text()) < 0 or float(item.text()) > 100):
            item.setText('')
            self.valid_message.setText('SCORE must be between 0 and 100')
        elif col == 1 and item.text().isnumeric():
            self.valid_message.setText('')


app = QApplication([])
window = Window()
window.show()
app.exec_()
