# PPHA 30537
# Spring 2023
# Homework 7

# YOUR NAME HERE: Tianhua Song

# YOUR CANVAS NAME HERE: Tianhua Song
# YOUR GITHUB USER NAME HERE: SkySong4

# Due date: Monday May 15th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Explore the data APIs available from Pandas DataReader.  Pick
# any two countries, and then 
#   a) Find two sets of data for each that cover these places for overlapping 
#      time periods.  There should be exactly four dataframes and four individual
#      downloads (e.g. do not use one line to download two datasets).
#      - At least one should be from the World Bank, and at least one should
#        not be from the World Bank.
#      - At least one should have a frequency that does not match the others,
#        e.g. annual, quarterly, monthly.
# import pandas as pd
# import pandas_datareader as pdr
# from pandas_datareader import wb
# country_1 = 'USA'
# country_2 = 'CAN'
# start_date = '2000-01-01'
# end_date = '2022-12-31'
# wb_data_usa = wb.download(indicator='NY.GDP.PCAP.KD', country=country_1, start=start_date, end=end_date)
# wb_data_can = wb.download(indicator='NY.GDP.PCAP.KD', country=country_2, start=start_date, end=end_date)
# fred_data_usa = pdr.get_data_fred('UNRATE', start=start_date, end=end_date)
# fred_data_can = pdr.get_data_fred('LRUNTTTTCAQ156S', start=start_date, end=end_date)


#   b) Adjust the data so that all four are at the same frequency (you'll have
#      to look this up), then merge them together into one long (tidy) format
#      dataframe.
# fred_data_usa_annual = fred_data_usa.resample('A').mean()
# fred_data_can_annual = fred_data_can.resample('A').mean()
# wb_data_usa_reset = wb_data_usa.reset_index().rename(columns={'year': 'Year', 'NY.GDP.PCAP.KD': 'GDP per Capita'})
# wb_data_can_reset = wb_data_can.reset_index().rename(columns={'year': 'Year', 'NY.GDP.PCAP.KD': 'GDP per Capita'})
# fred_data_usa_reset = fred_data_usa_annual.reset_index().rename(columns={'UNRATE': 'Unemployment Rate'})
# fred_data_can_reset = fred_data_can_annual.reset_index().rename(columns={'LRUNTTTTCAQ156S': 'Unemployment Rate'})
# usa_data = pd.merge(wb_data_usa_reset, fred_data_usa_reset, on='Year')
# usa_data['Country'] = 'USA'
# can_data = pd.merge(wb_data_can_reset, fred_data_can_reset, on='Year')
# can_data['Country'] = 'CAN'
# final_data = pd.concat([usa_data, can_data], ignore_index=True)


#   c) Finally, go back and change your earlier code so that the
#      countries and dates are set in variables at the top of the file.  Your
#      final result for parts a and b should allow you to (hypothetically) 
#      modify these values easily so that your code would download the data
#      and merge for different countries and dates.
#      - You do not have to leave your code from any previous way you did it
#        in the file. If you did it this way from the start, congrats!
#      - You do not have to account for the validity of all the possible 
#        countries and dates, e.g. if you downloaded the US and Canada for 
#        1990-2000, you can ignore the fact that maybe this data for some
#        other two countries aren't available at these dates.
import pandas as pd
import pandas_datareader as pdr
from pandas_datareader import wb

country_1 = 'USA'
country_2 = 'CAN'
start_date = '2000-01-01'
end_date = '2022-12-31'

wb_data_country_1 = wb.download(indicator='NY.GDP.PCAP.KD', country=country_1, start=start_date, end=end_date)
wb_data_country_2 = wb.download(indicator='NY.GDP.PCAP.KD', country=country_2, start=start_date, end=end_date)
fred_data_country_1 = pdr.get_data_fred('UNRATE', start=start_date, end=end_date)
fred_data_country_2 = pdr.get_data_fred('LRUNTTTTCAQ156S', start=start_date, end=end_date)

fred_data_country_1_annual = fred_data_country_1.resample('A').mean()
fred_data_country_2_annual = fred_data_country_2.resample('A').mean()
wb_data_country_1_reset = wb_data_country_1.reset_index().rename(columns={'year': 'Year', 'NY.GDP.PCAP.KD': 'GDP per Capita'})
wb_data_country_2_reset = wb_data_country_2.reset_index().rename(columns={'year': 'Year', 'NY.GDP.PCAP.KD': 'GDP per Capita'})
fred_data_country_1_reset = fred_data_country_1_annual.reset_index().rename(columns={'UNRATE': 'Unemployment Rate'})
fred_data_country_2_reset = fred_data_country_2_annual.reset_index().rename(columns={'LRUNTTTTCAQ156S': 'Unemployment Rate'})

fred_data_country_1_reset['Year'] = fred_data_country_1_reset['DATE'].dt.year.astype(str)
del fred_data_country_1_reset['DATE']
fred_data_country_2_reset['Year'] = fred_data_country_2_reset['DATE'].dt.year.astype(str)
del fred_data_country_2_reset['DATE']

country_1_data = pd.merge(wb_data_country_1_reset, fred_data_country_1_reset, on='Year')
# country_1_data['Country'] = country_1
country_2_data = pd.merge(wb_data_country_2_reset, fred_data_country_2_reset, on='Year')
# country_2_data['Country'] = country_2

final_data = pd.concat([country_1_data, country_2_data], ignore_index=True)

#   d) Clean up any column names and values so that the data is consistent
#      and clear, e.g. don't leave some columns named in all caps and others
#      in all lower-case, or a column of mixed strings and integers.  Write 
#      the dataframe you've created out to a file named q1.csv, and commit
#      it to your repo.
final_data.columns = [col.title() for col in final_data.columns]
final_data['Year'] = pd.to_datetime(final_data['Year']).dt.year
final_data['Gdp Per Capita'] = final_data['Gdp Per Capita'].astype(float)
final_data['Unemployment Rate'] = final_data['Unemployment Rate'].astype(float)
print(final_data)
final_data.to_csv('q1.csv', index=False)




# Question 2: On the following Harris School website:
# https://harris.uchicago.edu/academics/design-your-path/certificates/certificate-data-analytics
# There is a list of six bullet points under "Required courses" and ten 
# bullet points under "Elective courses".  Using requests and BeautifulSoup: 
#   - Collect the text of each of these bullet points
#   - Add each bullet point to the csv_doc file below as strings (following 
#     the header already specified). The first string you add should be: 
#     'required,30535 or 30537,Data and Programming for Public Policy I\n'
#     (recall that \n is the new-line character in text)
#   - Using context management, write the contents of csv_doc out to a file named q1.csv
#   - Finally, import Pandas and test loading q1.csv with the read_csv function.
#     Use asserts to test that the dataframe has 16 rows and three columns.

from bs4 import BeautifulSoup
import requests
import re
url = 'https://harris.uchicago.edu/academics/design-your-path/certificates/certificate-data-analytics'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
body_content = soup.find('div', class_='node--content--main--body')
required_courses_1 = body_content.find_all('ul')[5].find_all('li')  # 6th ul
required_courses_2 = body_content.find_all('ul')[6].find_all('li')  # 7th ul
elective_courses = body_content.find_all('ul')[7].find_all('li')  # 8th ul

data = []
for course in required_courses_1:
    data.append({'type': 'required', 'course tittle': course.text})
for course in required_courses_2:
    data.append({'type': 'required', 'course tittle': course.text})
for course in elective_courses:
    data.append({'type': 'elective', 'course tittle': course.text})
df = pd.DataFrame(data)
# extract course codes from a string
def extract_codes(s):
    parts = re.split(r'([A-Z]+\s*\d+)', s)
    codes = [part for part in parts if re.match(r'[A-Z]+\s*\d+', part)]
    title = [part for part in parts if not re.match(r'[A-Z]+\s*\d+', part)]
    return ' '.join(codes), ' '.join(title).strip()
# create the 'code' and 'course title' columns
df['code'], df['course title'] = zip(*df['course tittle'].map(extract_codes))
df = df.drop(columns='course tittle')
df = df[['type', 'code', 'course title']]
df['course title'] = df['course title'].str.replace('or', '').str.replace('/', '').str.strip()
print(df)
# Add each bullet point to the csv_doc file
csv_doc = [
    'type,code,course title\n', 
    'required,"PPHA 30535 or PPHA 30537",Data and Programming for Public Policy I\n', 
    'required,"PPHA 30536 or PPHA 30538",Data and Programming for Public Policy II\n', 
    'required,"PPHA 30545 or PPHA 30546",Machine Learning\n', 
    'required,BUSN 41204,Machine Learning\n', 
    'required,CMSC 35300,Mathematical Foundations of Machine Learning\n', 
    'required,MACS 33002,Introduction to Machine Learning\n', 
    'elective,PPHA 30560,"Data Visualization (not offered in 2022-2023)"\n', 
    'elective,PPHA 34600,Program Evaluation\n', 
    'elective,PPHA 38829,Artificial Intelligence for Public Policy\n', 
    'elective,PPHA 42000,Applied Econometrics I\n', 
    'elective,PPHA 42100,Applied Econometrics II\n', 
    'elective,PPHA 60000,"Policy Labs (with permission of the Certificate Director)"\n', 
    'elective,BUSN 37304,Digital and Algorithmic Marketing\n', 
    'elective,BUSN 41100,Applied Regression Analysis\n', 
    'elective,"CAPP 30300 or PPHA 30581","Data Science Clinic (offered Autumn, Winter, Spring)"\n', 
    'elective,PPHA 41400,"Applied Regression Analysis (not offered in 2022-2023)"\n'
]
# write the contents of csv_doc out to a file named q2.csv
with open('q2.csv', 'w') as file:
    file.writelines(csv_doc)
# Check the DataFrame has 16 rows and 3 columns
df = pd.read_csv('q2.csv')
assert df.shape == (16, 3)
