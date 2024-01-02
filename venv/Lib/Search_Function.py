import math
from Lib.NoMatchFoundError import NoMatchFoundError


class lookupthings():
    def __init__(self):
        self.x = [[],[],[],[], []]
        self.y = [[[],[],[],[]], [[],[],[],[]], [[],[],[],[]], [[],[],[],[]], [[],[],[],[]]]
        self.criterion = 0.25
        self.criterion_Test_in_ideal4 = 0.7
        self.Anzahl_Spalten = 5

    def lookup_train_in_ideal(self, source, destination):       # source: Instanz train_data; destination: Instanz ideal_data
        """
        zu den trainingsdaten passende Funktionen in den 50 idealen Funktionen finden
        :param source: Quelldatei -> trainings Daten
        :param destination: Zieldatei -> ideal Daten
        """

        # Header schreiben
        self.x[0] = 'x'
        for i in range(1, 5):
            self.y[i][0].append('x')
            self.y[i][1].append('y')
            self.y[i][2].append('Differenz')
            self.y[i][3].append('QuellFunktion')

        # alle yse in Quelle (train, y1 bis y4)
        for pos_outer_src in range(1,len(source.y)):

            # alle x in Quelle (train_data, x 1 bis 400)
            for pos_inner_dest in range(1, len(source.x)):
                pos_inner_src = pos_inner_dest

                # alle y in Ziel (50 ideale) in x Richtung durchlaufen 1 - 50
                for pos_outer_dest in range(1, len(destination.y)):
                    middleValue = (destination.y[pos_outer_dest][pos_inner_dest] + source.y[pos_outer_src][pos_inner_src])/2        # Mittelwert
                    difference = math.sqrt(0.5 * ((source.y[pos_outer_src][pos_inner_src] - middleValue)**2 + (destination.y[pos_outer_dest][pos_inner_dest] - middleValue)**2))        # quadr. mittlere Abweichung
                    if difference <= self.criterion:
                        self.x[pos_outer_src].append(source.x[pos_inner_src])
                        self.y[pos_outer_src][0].append(source.x[pos_inner_src])        # x-Wert schreiben in y Liste
                        self.y[pos_outer_src][1].append(destination.y[pos_outer_dest][pos_inner_dest])      # y-Wert schreiben
                        self.y[pos_outer_src][2].append(difference)     # Differenz schreiben
                        self.y[pos_outer_src][3].append(destination.y[pos_outer_dest][0])       # Name der Quellfunktion
                        pass                            # if Wert <= Sqrt(2)
                    pass                                # y dest
                pass                                    # x_xrc
            pass

        self.cleanup()  # bereinigen

        print("DONE LOOKUP")


    def lookup_test_in_ideal4(self, source, destination):
        """
        testdaten mit den 4 gefundenen idealen Funktionen vergleichen
        :param source: testdaten
        :param destination: 4 ideale funktionen
        """
        self.x = []
        self.y = [[], [], [], []]
        # Ueberschriften anlegen
        self.y[0].append('x')
        self.y[1].append('y')
        self.y[2].append('Differenz')
        self.y[3].append('QuellFunktion')
        found = False

        # lenFileContent = len(source.file_content)
        for i in range(len(source.file_content)):
            xTest = source.file_content[i][0]   # x Wert suchen

            for j in range(1, len(destination.y[0])):
                xDest = destination.y[0][j]
                found = False
                if destination.y[0][j] == xTest:
                    for z in range(1, len(destination.y)):  # für alle y se in y bei x
                        yTest = source.file_content[i][1]
                        middleValue = (destination.y[z][j] + source.file_content[i][1]) / 2.0
                        difference = math.sqrt(0.5 * ((source.file_content[i][1] - middleValue) ** 2 + (destination.y[z][j] - middleValue) ** 2))  # quadr. mittlere Abweichung
                        try:
                            if difference < self.criterion_Test_in_ideal4:
                                self.y[0].append(xTest)
                                self.y[1].append(yTest)
                                self.y[2].append(difference)
                                self.y[3].append(destination.y[z][0])
                                found = True
                            elif found == False and z == len(destination.y)-1:
                                raise NoMatchFoundError     # benutzerdefinierte Excpetion

                        except NoMatchFoundError:
                            print(NoMatchFoundError().message)
                            
                        pass
                else:
                    # print("else Pfad")
                    if xDest > xTest:
                        break       # Schleife beenden, wenn x aus Destination > als x aus Testdaten, da Daten sortiert sind
                    pass
                pass
        self.x = self.y[0]
        self.Anzahl_Spalten = len(self.y)


    def cleanup(self):
        """
        Funktion bestimmt die am häufigsten gefundene ideale Funktion und löscht die nicht zugehörigen
        """
        i = 0
        for j in range(1, len(self.y)):     # durchlaufe alle y 1-5
            # die Funktion mit den meisten Matches ermitteln
            zwischending = [[], []]
            for z in range(1, 51):  # bei 1 starten wegen Namen y1 bis y50
                zwischending[0].append('y' + str(z))    # interimsarray mit Funktionsnamen
                zwischending[1].append(self.y[j][3].count('y' + str(z)))    # zugehörige Anzahl der gefundenen Matches
                
            max_value = max(zwischending[1])    # Maximale Anzahl
            max_value_index = zwischending[1].index(max_value)  # Index der maximalen Anzahl
            search_value = zwischending[0][max_value_index]     # hier steht die ermittelte am häufigsten gefundene Funktion

            for i in range(len(self.y[j][3]), 1, -1):   # lösche die anderen Werte der Funktionen, die nicht am häufigsten enthalten sind
                if self.y[j][3][i-1] != search_value:   # zaehle von hinten her
                    for todelete in range(len(self.y[j])):
                        del self.y[j][todelete][i-1]    # von i muss 1 subtrahiert werden, da hier der Index benötigt wird in i ist aber die gesamte Anzahl an Stellen enthalten

        # Ab hier cleanup um Funktionen createTable und dataToTable nutzen zu können -> umformatieren in eindimensional (x) und zweidimensional (y)
        for i in range(1, 5):           # Funktionsnamen in y Spalte Platz [0] schreiben als Überschrift
            self.y[i][1][0] = self.y[i][3][1]

        self.x = []       # x löschen, indem neu definiert wird
        self.x = self.y[1][0]   # es werden die x-Werte aus y[0] in neues x geschrieben

        for i in range(5):
            del self.y[i][3]        # lösche Quellfunktion
            del self.y[i][2]        # lösche Differenz

        self.y[0][0] = self.y[1][0]       # x Werte in nulltes Array schreiben
        del self.y[0][1]
        self.y[0] = self.y[0][0]
        del self.y[1][0]
        self.y[1] = self.y[1][0]
        del self.y[2][0]
        self.y[2] = self.y[2][0]
        del self.y[3][0]
        self.y[3] = self.y[3][0]
        del self.y[4][0]
        self.y[4] = self.y[4][0]

        print("DONE cleanup")