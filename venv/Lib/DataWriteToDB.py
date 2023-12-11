import sqlalchemy as sql
from sqlalchemy.exc import OperationalError as sqlOpErr
from Lib.Data_import import DataToImport


class DataToDatabase(DataToImport):
    def __init__(self):
        # DatabaseName
        # TableName
        self.rows = 0

        super().__init__()

    def create_table(self, tablename, di, connection):
        ####### text fuer Create bauen (x float, y0 float, y1 float, ... )
        text_create = "(" + di.x[0] + " float, "
        for i in range(di.Anzahl_Spalten - 1):
            text_create += di.y[i + 1][0] + " float, "
        text_create = text_create[:-2]
        text_create += ")"

        rowsintable = 0

        try:
            connection.execute(sql.text("CREATE TABLE " + tablename + " " + text_create))
        except sqlOpErr:
            #    pass
            print("Tabelle existiert schon")
            result = connection.execute(sql.text("SELECT * FROM " + tablename))
            for row in result:
                rowsintable += 1  # i > 0 → Tabelle ist schon befüllt
        self.rows = rowsintable

    def create_table_id4(self, tablename, di, connection):
        ####### text fuer Create bauen (x float, y0 float, y1 float, ... )
        text_create = "(" + di.x[0] + " float, "
        for i in range(1, di.Anzahl_Spalten-2):
            text_create += di.y[1][i][0] + " float, "
        text_create += di.y[1][3][0] + " string)"

        rowsintable = 0

        try:
            connection.execute(sql.text("CREATE TABLE " + tablename + " " + text_create))
        except sqlOpErr:
            #    pass
            print("Tabelle existiert schon")
            result = connection.execute(sql.text("SELECT * FROM " + tablename))
            for row in result:
                rowsintable += 1  # i > 0 → Tabelle ist schon befüllt
        self.rows = rowsintable
        print("DONE Data_to_table id4")
    def data_to_table(self, tablename, di, connection):
        rowsintable = self.rows

        if rowsintable == 0:
            ####### TEXT_INSERT bauen (x, y1, y2, ...)
            text_insert = "(" + di.x[0] + ", "
            for i in range(di.Anzahl_Spalten - 1):
                text_insert += di.y[i + 1][0] + ", "
            text_insert = text_insert[:-2]
            text_insert += ")"

            ####### TEXT VALUES bauen VARIABEL  (:x, :y1, :y2, ...)
            text_values = "(:" + di.x[0] + ", :"
            for i in range(di.Anzahl_Spalten - 1):
                text_values += di.y[i + 1][0] + ", :"
            text_values = text_values[:-3]
            text_values += ")"

            for j in range(1, len(di.x)):  # j steht für die Zeilen
                dict2 = {di.x[0]: di.x[j]}
                for i in range(1, di.Anzahl_Spalten):  # i steht für die Spalten
                    dict2.update({di.y[i][0]: di.y[i][j]})  # dictionary bauen
                connection.execute(sql.text("INSERT INTO " + tablename + " " + text_insert + " VALUES " + text_values), [dict2])
            connection.commit()
        else:
            print("Tabelle bereits befüllt")
        pass


    def data_to_table_id4(self, tablename, di, connection):
        rowsintable = self.rows

        if rowsintable == 0:
            ####### TEXT_INSERT bauen (x, y1, y2, ...)
            text_insert = "(" + di.x[0] + ", "
            for i in range(di.Anzahl_Spalten - 2):
                text_insert += di.y[1][i + 1][0] + ", "
            text_insert = text_insert[:-2]
            text_insert += ")"

            ####### TEXT VALUES bauen VARIABEL  (:x, :y1, :y2, ...)
            text_values = "(:" + di.x[0] + ", :"
            for i in range(di.Anzahl_Spalten - 2):
                text_values += di.y[1][i + 1][0] + ", :"
            text_values = text_values[:-3]
            text_values += ")"

            for j in range(1, len(di.x)):  # j steht für die Zeilen
                dict2 = {di.x[0]: di.x[j]}
                for i in range(1, di.Anzahl_Spalten-1):  # i steht für die Spalten
                    dict2.update({di.y[1][i][0]: di.y[1][i][j]})  # dictionary bauen
                connection.execute(sql.text("INSERT INTO " + tablename + " " + text_insert + " VALUES " + text_values), [dict2])
            connection.commit()
        else:
            print("Tabelle bereits befüllt")
        pass
