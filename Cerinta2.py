import pandas as pd;
import matplotlib.pyplot as plt

def plotCsv(data, xLabel, yLabel, plotTitle):
    df = pd.DataFrame(data);
    df.plot(x = xLabel, y = yLabel, kind='line', marker='o', linestyle='-', color = 'b', label='Valori');

    plt.title = plotTitle;
    plt.xlabel = xLabel;
    plt.ylabel = yLabel;

    plt.legend();

    plt.show();
def writeCsvLine(data, x1, y1):
    try:
        data1 = data.head(x1);
        print(f"Datele pentru primele {x1} linii \n {data1} \n");
        print("Configuratia pentru tabelul 1 \n");
        xLabel = input("xLabel = ");
        yLabel = input("yLabel = ");
        plotTitle = input("plotTitle = ");

        plotCsv(data1, xLabel, yLabel, plotTitle);

        data2 = data.iloc[-y1:, :2];
        print(f"Durata si Pulsul pentru ultimele {y1} coloane: \n {data2} \n");
        print(f"Datele pentru primele {x1} linii \n {data1} \n");
        print("Configuratia pentru tabelul 2 \n");
        xLabel = input("xLabel = ");
        yLabel = input("yLabel = ");
        plotTitle = input("plotTitle = ");
        plotCsv(data2, xLabel, yLabel, plotTitle);

    except Exception as e:
        print(f"Error reading: {e}");
def problema2():
    sourceFile = "data.csv";
    data = pd.read_csv(sourceFile);

    writeCsvLine(data, 10, 12);
