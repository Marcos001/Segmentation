
import os
import csv
import example_plot as pl

def ler_arquivos_csv_pandas(path_file):
    import pandas as pd
    import matplotlib.pyplot as plt
    result = pd.read_csv(path_file)
    cm = result[['VP','VN','FP','FN']].as_matrix()
    #cm = result[['VP', 'VN', 'FP', 'FN']]
    #print(result[['VP', 'VN', 'FP', 'FN']])
    #print(cm)
    plt.matshow(cm)
    plt.colorbar()
    plt.show()
    #classe = ['Segmentadas','mascara']
    #pl.plot_confusion_matrix(cm,classe)







def ler_arquivos_csv(path_file):

    with open(path_file, 'rb') as ficheiro:
        reader = csv.reader(ficheiro, delimiter=',',quoting=csv.QUOTE_NONE)
        for linha in reader:
            print(linha)

if __name__ == '__main__':
    print('predict > ')
    file = os.getcwd()+'/reultados/resultad_geral.csv'
    ler_arquivos_csv_pandas(file)
