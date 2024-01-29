# Add required imports here:
import matplotlib.pyplot as plt
import numpy as np

# Import functions from functions file
from Project4_Functions import *

# This dictionary maps vaccine abbreviations to full names of
# infectious diseases and agents. DO NOT CHANGE THE DICTIONARY!
vaccineNames = {'BCG':'tuberculosis',\
    'DTP1':'diphteria_pertussis_tetanus','DTP3':'diptheria_pertussis_tetanus',\
    'MCV1':'meningococcal_disease','MCV2':'meningococcal_disease',\
    'HEPBB':'hepatitis B', 'HEPB3':'hepatitis B',\
    'HIB1':'Haemophilus influenzae', 'HIB3':'Haemophilus influenzae',\
    'IPV1':'polio','IPV3': 'polio', 'POL3': 'polio',\
    'PCV3':'pneumococcal disease', 'RCV1':'rubella',\
    'ROTAC':'rotavirus','YFV':'Yellow Fever Virus'}

# Your code here:

## Constants 
LINE_PLT_Y_MIN = 0
LINE_PLT_Y_MAX = 100
LINE_PLT_LABEL_ROT = 90

BAR_WIDTH = 0.2
BAR_MULTIPLIER = 0
BAR_PADDING = 1
SUBPLOT_MULTIPLIER = 1
NUM_OF_COLS = 3
Y_MIN = 0
Y_MAX = 110
X_TICK1 = .2
X_TICK2 = 1.2
X_TICK3 = 2.2

df = createVaccineDF('vaccine_data.csv')
df = createDescriptionColumn(df, 'BCG')

## Code for Line Graph
linePlotGlobal = df.loc[(df['Region'] == 'Global') & (df['Vaccine'] == 'POL3')]
linePlotLAC = df.loc[(df['Region'] == 'Latin_America_and_Caribbean') & (df['Vaccine'] == 'POL3')]
linePlotNA = df.loc[(df['Region'] == 'North_America') & (df['Vaccine'] == 'POL3')]

## Readable text for line graph data
print(linePlotGlobal.drop(['Vaccine'], axis = 1).drop(['Description'], axis = 1))
print(linePlotLAC.drop(['Vaccine'], axis = 1).drop(['Description'], axis = 1))
print(linePlotNA.drop(['Vaccine'], axis = 1).drop(['Description'], axis = 1))

## Line Graph
fig, ax = plt.subplots()
ax.plot(linePlotGlobal['Year'], linePlotGlobal['Percentage'], label = 'Global')
ax.plot(linePlotLAC['Year'], linePlotLAC['Percentage'], label = 'Latin America and Caribbean')
ax.plot(linePlotNA['Year'], linePlotNA['Percentage'], label = 'North America')

x = np.arange(len(linePlotGlobal['Year']))
ax.set(xlabel = 'Years', ylabel = 'Vaccination Rate', title = 'Polio Vaccination Rate')
ax.legend(loc = 'lower right')
ax.set_ylim(LINE_PLT_Y_MIN, LINE_PLT_Y_MAX)
ax.tick_params(axis= 'x', labelrotation = LINE_PLT_LABEL_ROT)

plt.show()

## Code for Bar Graph
east_south_africa_1980 = makeSubset(df, 'Eastern_and_Southern_Africa', 'BCG', '1980')
east_south_africa_2000 = makeSubset(df, 'Eastern_and_Southern_Africa', 'BCG', '2000')
east_south_africa_2019 = makeSubset(df, 'Eastern_and_Southern_Africa', 'BCG', '2019')


es_africa_percent_1980 = int(east_south_africa_1980['Percentage'])
es_africa_percent_2000 = int(east_south_africa_2000['Percentage'])
es_africa_percent_2019 = int(east_south_africa_2019['Percentage'])
es_africa_list = [es_africa_percent_1980, es_africa_percent_2000, es_africa_percent_2019]

## Readable text for East and South Africa for years 1980, 2000, and 2019
print('Vaccination rates for East and South Africa for 1980, 2000, and 2019, respectively: ' + str(es_africa_list))

middle_east_north_africa_1980 = makeSubset(df, 'Middle_East_and_North_Africa', 'BCG', '1980')
middle_east_north_africa_2000 = makeSubset(df, 'Middle_East_and_North_Africa', 'BCG', '2000')
middle_east_north_africa_2019 = makeSubset(df, 'Middle_East_and_North_Africa', 'BCG', '2019')

me_na_percent_1980 = int(middle_east_north_africa_1980['Percentage'])
me_na_percent_2000 = int(middle_east_north_africa_2000['Percentage'])
me_na_percent_2019 = int(middle_east_north_africa_2019['Percentage'])
me_na_list = [me_na_percent_1980, me_na_percent_2000, me_na_percent_2019]

## Readable text for the Middle East and North Africa for years 1980, 2000, and 2019
print('Vaccination rates for the Middle East and North Africa for 1980, 2000, and 2019, respectively: ' + str(me_na_list))

west_central_africa_1980 = makeSubset(df, 'West_and_Central_Africa', 'BCG', '1980')
west_central_africa_2000 = makeSubset(df, 'West_and_Central_Africa', 'BCG', '2000')
west_central_africa_2019 = makeSubset(df, 'West_and_Central_Africa', 'BCG', '2019')

wca_percent_1980 = int(west_central_africa_1980['Percentage'])
wca_percent_2000 = int(west_central_africa_2000['Percentage'])
wca_percent_2019 = int(west_central_africa_2019['Percentage'])
wca_list = [wca_percent_1980, wca_percent_2000, wca_percent_2019]

## Readable text for West and Central Africa for years 1980, 2000, and 2019
print('Vaccination rates for West and Central Africa for 1980, 2000, and 2019, respectively: ' + str(wca_list))

## Bar Graph 
years = ['1980', '2000', '2019']
percentages = {'Eastern and Southern Africa': es_africa_list, 'Middle East and North Africa': me_na_list, 'West and Central Africa': wca_list}

x = np.arange(len(years))
width = BAR_WIDTH
multiplier = BAR_MULTIPLIER

fig, ax = plt.subplots()
for region, percentage in percentages.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, percentage, width, label=region)
    ax.bar_label(rects, padding=BAR_PADDING)
    multiplier += SUBPLOT_MULTIPLIER

ax.set_ylabel('Vaccination Rate')
ax.set_xlabel('Years')
ax.set_title('Tuberculosis Percentages for all African Regions')
ax.set_xticks(x + width, years)
ax.legend(loc='upper left', ncol=NUM_OF_COLS, fontsize='6.5')
ax.set_ylim(Y_MIN, Y_MAX)
ax.set_xticks((X_TICK1, X_TICK2, X_TICK3), ('1980', '2000', '2019'))

plt.show()