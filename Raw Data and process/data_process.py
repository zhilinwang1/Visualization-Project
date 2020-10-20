import pandas as pd
pop = pd.read_csv('Population.csv').values
military = pd.read_csv('military.csv').values
healthcapita = pd.read_csv('healthcapita.csv').values
gdp = pd.read_csv('GDP.csv').values
educationOfGDP = pd.read_csv('edu_gdp_percent.csv')


EDU = pd.read_csv('EDU.csv').values

health = pd.read_csv('healthdiff.csv').values
dataprint = pd.read_csv('dataprint.csv').dropna(axis=1).values
# r,c = pop.shape
# arr = (military/pop)
#
#
# pd.DataFrame(arr).to_excel(excel_writer='militarycapita.xlsx')
#
# healthspend = (healthcapita*pop)
# pd.DataFrame(healthspend).to_excel(excel_writer='Healthspend.xlsx')
#
# education = gdp*educationOfGDP/100
# print(education)
# pd.DataFrame(education).to_excel(excel_writer='Education.xlsx')


# health_diff = health[:,1:]-health[:,:-1]
#
# pd.DataFrame(health_diff).to_excel(excel_writer='health_diff.xlsx')
#
# health_diff_percent = 100*health_diff/health[:,:-1]
# # print(health_diff_percent)
# pd.DataFrame(health_diff_percent).to_excel(excel_writer='health_diff_percent.xlsx')

#--------------------------print data------------------
print(dataprint.tolist())

#pd.DataFrame(EDU/pop).to_excel(excel_writer='educapita.xlsx')

EDU_diff = EDU[:,1:]-EDU[:,:-1]

pd.DataFrame(EDU_diff).to_excel(excel_writer='EDU_diff.xlsx')

EDU_diff_percent = 100*EDU_diff/EDU[:,:-1]
# print(health_diff_percent)
pd.DataFrame(EDU_diff_percent).to_excel(excel_writer='EDU_diff_percent.xlsx')