from matplotlib import pyplot as plt
from matplotlib import style


class ShowInPlot():
    def __init__(self):
        x_axis = 'X AXIS'       # Name x-Achse
        y_axis = 'Y AXIS'       # Name y_Achse
        title = 'TITEL'         # Diagrammtitel


    def show_id4_plus_test(self, id4, test, train, x_name, y_name, title):
        data_name = []  # label in Diagramm
        
        for i in range(id4.Anzahl_Spalten):
            if type(id4.y[i][0]) is str:
                data_name.append(id4.y[i][0])
                del id4.y[i][0]

        style.use('ggplot')
        fig, ax = plt.subplots(1, 1)    # Diagramm mit einer Spalte und einer Zeile
        ax.grid(True, color="b")    # Gitterfarbe und Gitter zeigen
        ax.set_xlabel(x_name)       # x-Achsenbeschriftung
        ax.set_ylabel(y_name)       # y- Achsenbeschriftung
        ax.set_title(title)         # Diagrammtitel
        for i in range(1, id4.Anzahl_Spalten):      # zeige y Daten
            ax.scatter(id4.y[0], id4.y[i], label=data_name[i], marker='+',
                       alpha=0.2)  # edgecolors='r'  # alpha = Durchsichtigkeit label=title+'_'+str(i),
            ax.legend()


        ''' test Daten darstellen '''

        ax.scatter(test.y[0], test.y[1], label='test data', marker='o', color='black',
                       alpha=0.6)  # , marker='o', color='0', edgecolors='r', alpha=0.2)  # alpha = Durchsichtigkeit label=title+'_'+str(i),
        ax.legend()

        fig.show()
        plt.savefig("ideal4_vs_test.png")

        ''' neues Diagramm mit ideal 4 und train data'''
        fig2, ax2 = plt.subplots(1, 1)  # Diagramm mit einer Spalte und einer Zeile
        ax2.grid(True, color="b")  # Gitterfarbe und Gitter zeigen
        ax2.set_xlabel(x_name)  # x-Achsenbeschriftung
        ax2.set_ylabel(y_name)  # y- Achsenbeschriftung
        ax2.set_title('ideal 4 vs train data')  # Diagrammtitel
        for i in range(1, id4.Anzahl_Spalten):  # zeige y Daten
            ax2.scatter(id4.y[0], id4.y[i], label=data_name[i], marker='+', alpha=0.2)
            ax2.legend()

        ''' train data in Diagramm 2 '''
        data_name = []  # label in Diagramm

        for i in range(train.Anzahl_Spalten):
            if type(train.y[i][0]) is str:
                data_name.append(train.y[i][0])
                del train.y[i][0]
                
        for i in range(1, train.Anzahl_Spalten):  # zeige y Daten
            ax2.scatter(train.y[0], train.y[i], label=data_name[i], marker='.', alpha=0.3)
            ax2.legend()

        fig.show()
        plt.savefig("ideal4_vs_train.png")

        print("DONE Plotting")
