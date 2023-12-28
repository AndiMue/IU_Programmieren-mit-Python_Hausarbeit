import sqlalchemy as sql
from sqlalchemy.exc import OperationalError as sqlOpErr
from Lib.Data_import import DataToImport


class DataToDatabase(DataToImport):     # erbt Dataimport Klasse
    
    def __init__(self):

        self.rows = 0

        super().__init__()

    def create_table(self, tablename, di, connection):
        """
        Die Funktion erzeugt eine Tabelle in der Datenank
        :param tablename: übergebener Tabellenname
        :param di: Inhalt der Tabelle
        :param connection: Verbindung zur Datenbank
        kann die Tabelle nicht erzeugt werden wird eine Exception ausgelöst
        """
        # text fuer Create bauen (x float, y0 float, y1 float, ... )
        if len(di.x) > 0:
            text_create = "(" + di.x[0] + " float, "
            for i in range(di.Anzahl_Spalten - 1):
                text_create += di.y[i + 1][0] + " float, "
            if tablename == 'test':
                text_create = text_create[:-7]
                text_create += "string, "
            text_create = text_create[:-2]
            text_create += ")"
        else:
            print("Array ist leer. kann nicht ausgeführt werden")
            pass
        
        rowsintable = 0     # Tabelle als leer vorbelegen

        try:
            connection.execute(sql.text("CREATE TABLE " + tablename + " " + text_create))   # Tabelle einfügen
        except sqlOpErr:
            print("Tabelle existiert schon")
            result = connection.execute(sql.text("SELECT * FROM " + tablename))
            for row in result:
                rowsintable += 1  # i > 0 → Tabelle ist schon befüllt   # prüfen, ob Tabelle befüllt ist, wenn sie existiert
        self.rows = rowsintable

    def create_table_id4(self, tablename, di, connection):
        """
        Die Funktin erzeugt die Tabelle für die 4 idealen Funktionen,
        nötig weil das Format anders ist als oben
        :param tablename: übergebener Tabellenname
        :param di: Inhalt für die Tabelle
        :param connection: Verbindung zur Datenbank
        """
        # text fuer Create bauen (x float, y0 float, y1 float, ... )
        text_create = "(" + di.y[1][0][0] + " float, "
        for i in range(1, di.Anzahl_Spalten):
            text_create += di.y[i][3][2] + " float, "
        text_create = text_create[:-2]
        text_create += ")"

        rowsintable = 0 # Tabelle als leer vorbelegen

        try:
            connection.execute(sql.text("CREATE TABLE " + tablename + " " + text_create))
        except sqlOpErr:
            print("Tabelle existiert schon")
            result = connection.execute(sql.text("SELECT * FROM " + tablename))
            for row in result:
                rowsintable += 1  # i > 0 → Tabelle ist schon befüllt
        self.rows = rowsintable


    def data_to_table(self, tablename, di, connection):
        """
        Funktion befüllt die Tabelle
        :param tablename: übergebener Tabellenname
        :param di: Inhalt für die Tabelle
        :param connection: Verbindung zur Datenbank
        """
        rowsintable = self.rows

        if rowsintable == 0:
            # TEXT_INSERT bauen (x, y1, y2, ...)
            text_insert = "(" + di.x[0] + ", "
            for i in range(di.Anzahl_Spalten - 1):
                text_insert += di.y[i + 1][0] + ", "
            text_insert = text_insert[:-2]
            text_insert += ")"

            # TEXT VALUES bauen VARIABEL  (:x, :y1, :y2, ...)
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



    def data_to_table_id4(self, tablename, di, connection):
        """
        Funktion befüllt die Tabelle der 4 idealen Funktionen
        :param tablename: übergebener Tabellenname
        :param di: Inhalt für die Tabelle
        :param connection: Verbindung zur Datenbank
        """
        rowsintable = self.rows

        if rowsintable == 0:
            ####### TEXT_INSERT bauen (x, y1, y2, ...)
            text_insert = "(" + di.y[1][0][0] + ", "    # 'x'
            # for i in range(di.Anzahl_Spalten - 2):
            for i in range(1, di.Anzahl_Spalten):      # 'ynr' Nummer der Funktion, z.B. y36
                text_insert += di.y[i][1][0] + ", "
            text_insert = text_insert[:-2]
            text_insert += ")"

            ####### TEXT VALUES bauen VARIABEL  (:x, :y1, :y2, ...)
            text_values = "(:" + di.y[1][0][0] + ", :"
            # for i in range(di.Anzahl_Spalten - 2):
            for i in range(1, di.Anzahl_Spalten):
                text_values += di.y[i][1][0] + ", :"
            text_values = text_values[:-3]
            text_values += ")"

            for j in range(1, len(di.y[1][0])):  # j steht für die Zeilen
                dict2 = {di.y[1][0][0]: di.y[1][0][j]}      # 'x: x-Wert'
                for i in range(1, di.Anzahl_Spalten):  # i steht für die Spalten; 4 Spalten für die 4 idealen Funktionen -
                    dict2.update({di.y[i][1][0]: di.y[i][1][j]})  # dictionary zeilenweise bauen
                connection.execute(sql.text("INSERT INTO " + tablename + " " + text_insert + " VALUES " + text_values), [dict2])  # an Datenbank senden
            connection.commit()
        else:
            print("Tabelle bereits befüllt")

