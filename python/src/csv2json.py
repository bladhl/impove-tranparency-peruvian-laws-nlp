import csv, json
import pandas as pd


def csv2json(path_csv, path_json):
    data = dict()
    df = pd.read_csv(path_csv, sep=';')
    # df.drop('Unnamed: 0', inplace=True, axis=1)
    # df.drop('Unnamed: 0.1', inplace=True, axis=1)
    print(df.head())
    # df.to_csv(path_csv, index=False, sep=";")

    # for i, row in df.iterrows():
    #     dict_row = dict()
    #     dict_row["expediente"] = row["Expediente"]
    #     dict_row["período"] = row["Período"]
    #     dict_row["legislatura"] = row["Legislatura"]
    #     dict_row["fecha"] = row["Fecha"]
    #     dict_row["proponente"] = row["Proponente"]
    #     dict_row["parlamento"] = row["Parlamento"]
    #     dict_row["título"] = row["Título"]
    #     dict_row["objeto"] = row["Objeto"]
    #     dict_row["topico"] = row["Topicos"]
    #     data[str(i)] = dict_row
    # with open(path_json, "w") as jsonfile:
    #     jsonfile.write(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    path_csv = "../../datasets/Presidential_Periods/PKuczynski_period.csv"
    path_json = "../../datasets/Presidential_Periods/PKuczynski_period.json"
    csv2json(path_csv, path_json)
