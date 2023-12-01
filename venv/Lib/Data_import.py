# class for importing data from csv

class DataToImport:
    def __init__(self):
        self.data_path = None
        self.file_content = [None]
        self.x = []
        self.y = []  # []
        self.Anzahl_Spalten = 0  # Zaehler fuer die gesamte Anzahl der Spalten

    def separate_lines(self, f_content, spalten):
        """
        function seperates the file content in two variables.
        :param f_content: is in two columns, e.g. ['4.234','3.12']
        :spalten: Anzahl der gesamten Spalten
        :return: two seperate variables
        """

        sp = 1  # Spaltenindex, kann bei 1 beginnen, da Spaltenindex die x-Werte enthaelt
        b_x_valid = False   # konnte x gelesen werden?
        x = []

        # Liste fuer y-Werte erzeugen
        y = []
        for i in range(spalten):
            y.append([])

        # print("Laenge file_content: ", len(f_content))
        i = 0     # Laufindex muss zurueck gesetzt werden
        # solange das Ende des Inhalts nicht erreicht ist lese ein
        while i < len(f_content):
            # x einlesen, erster Wert muss 'x' sein
            try:
                if i > 0:
                    x.append(float(f_content[i][0]))
                else:
                    x.append(f_content[i][0])
                b_x_valid = True
            except:
                print(f"Punkt {i}  kann nicht verarbeitet werden")

            # y einlesen, wenn der x-Wert eingelesen werden konnte

            if b_x_valid:
                for sp in range(spalten-1):
                    try:

                        if i > 0:
                            y[sp+1].append(float(f_content[i][sp+1]))
                        else:
                            y[sp+1].append(f_content[i][sp+1])
                    except:
                        print(f"Punkt {i} kann nicht verarbeitet werden. Zugehoeriges x wird gelöscht")
                        del x[i]

                        for j in range(1, spalten):
                            try:
                                del y[j][i]
                            except:
                                print(f"Index {j} | {i} nicht zu loeschen!")
                                sp = sp+1        # Index ans Ende der Spalten setzen, damit diese nicht importiert werden
                        break   # notwendig um die restlichen y-Werte nicht zu lesen
                sp += 1
            sp = 1              # Ruecksetzen fuer naechsten Durchlauf fuer x
            b_x_valid = False   # Gueltigkeitswert ruecksetzen
            i += 1

        # print("DONE x and y")
        return x, y

    def importieren(self, data_path):
        """
        function to import a file content
        :param data_path: file to import
        :return: nothing, x and y are self
        """
        try:
            with open(data_path, "r") as csv_import_file:
                for line in csv_import_file.read().split("\n"):
                    self.file_content.append(line.split(","))  # = csv_import_file.read()
                self.file_content.__delitem__(0)    # None in erster Zeile löschen

            # Anzahl Spalten der Daten zaehlen
            for self.Anzahl_Spalten in range(len(self.file_content[0])):
                self.Anzahl_Spalten += 1
            # print("Spalten: ", self.Anzahl_Spalten)
            # print("Importieren Done")
        except:
            print("EXCEPTION importieren, Datei kann nicht geöffnet werden")

        self.x, self.y = self.separate_lines(self.file_content, self.Anzahl_Spalten)
         # print("seperate DONE")
