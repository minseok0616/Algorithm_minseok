import pandas as pd

excel_data = pd.read_excel('C:\sample.xlsx')

excel_data = excel_data.assign(총합 = [208,232,276,214,238,214,245,195,195,218,239,218,274,176,173,256,225,191,222,170])

excel_data = excel_data.assign(평균 = [69.3,77.3,92,71.3,79.3,71.3,81.6,65,65,72.6,79.6,72.6,91.3,58.6,57.6,85.3,75,63.6,74,56.6])
excel_data = excel_data.sort_values('총합')

excel_data['학점'] = 0
excel_data.head(20)


def func(row):
    if row > 90:
        return 'A'
    elif row > 80:
        return 'B'
    else:
        return 'C'

excel_data['학점'] = excel_data['평균'].apply(func)



print(excel_data)
