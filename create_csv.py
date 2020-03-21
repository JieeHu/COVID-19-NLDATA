import pandas as pd

col_names = ["datum", "totaal aantal patiënten in ziekenhuis (geweest)", "aantal overleden patiënten"]
data = [["01-03-2020", 1, 0],
        ["02-03-2020", 1, 0],
        ["03-03-2020", 1, 0],
        ["04-03-2020", 5, 0],
        ["05-03-2020", 7, 0],
        ["06-03-2020", 12, 1],
        ["07-03-2020", 24, 1],
        ["08-03-2020", 36, 3],
        ["09-03-2020", 36, 3],
        ["10-03-2020", 36, 4],
        ["11-03-2020", 62, 5],
        ["12-03-2020", 86, 5],
        ["13-03-2020", 115, 10],
        ["14-03-2020", 136, 12]]

df =pd.DataFrame(data, columns=col_names)
df.to_csv("COVID-19-NLDATA/rivm_covid_19_data/covid_19_deaths_timeseries/time_series_total_deaths_NL.csv", index=False)


