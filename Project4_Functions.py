import pandas as pd

def createVaccineDF (filename):
    df = pd.read_csv('vaccine_data.csv', encoding='utf-8')
    df['Region'] = df['Region'].str.replace(' ','_').str.replace('&','and')
    df['Year'] = df['Year'].astype(str)
    return df

df = createVaccineDF('vaccine_data.csv')

def createDescriptionColumn (df, mapping):
    df['Description'] = (df['Vaccine'])
    mapping = {'BCG':'tuberculosis',\
    'DTP1':'diphteria_pertussis_tetanus','DTP3':'diptheria_pertussis_tetanus',\
    'MCV1':'meningococcal_disease','MCV2':'meningococcal_disease',\
    'HEPBB':'hepatitis B', 'HEPB3':'hepatitis B',\
    'HIB1':'Haemophilus influenzae', 'HIB3':'Haemophilus influenzae',\
    'IPV1':'polio','IPV3': 'polio', 'POL3': 'polio',\
    'PCV3':'pneumococcal disease', 'RCV1':'rubella',\
    'ROTAC':'rotavirus','YFV':'Yellow Fever Virus'}
    df['Description'] = df['Description'].apply(lambda x: mapping.get(x))
    return df

df = createDescriptionColumn(df, 'BCG')

def makeSubset(df, region = None, vaccine = None, year = None):
    if region == None and vaccine == None and year == None:
        df = df
    elif region == region and vaccine == None and year == None:
        df = df.loc[df['Region'] == region]
    elif region == None and vaccine == vaccine and year == None:
        df = df.loc[df['Vaccine'] == vaccine]
    elif region == None and vaccine == None and year == year:
        df = df.loc[df['Year'] == year]
    elif region == region and vaccine == vaccine and year == None:
        df = df.loc[(df['Region'] == region) & (df['Vaccine'] == vaccine)]
    elif region == region and vaccine == None and year == year:
        df = df.loc[(df['Region'] == region) & (df['Year'] == year)]
    elif region == None and vaccine == vaccine and year == year:
        df = df.loc[(df['Vaccine'] == vaccine) & (df['Year'] == year)]
    else:
        df = df.loc[(df['Region'] == region) & (df['Vaccine'] == vaccine) & (df['Year'] == year)]
    return df
