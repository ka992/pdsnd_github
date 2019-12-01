import time
import calendar as cal
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
"""
MONTH_SELECTION = pd.DataFrame({'all', 'january', 'february', 'march', 'april' , 'may', 'june'})
DAY_SELECTION = pd.DataFrame(cal.day_name)
DAY_SELECTION = DAY_SELECTION.append('all')

"""




def main():
    path = 'G:/System back up/Desktop/School/Udacity/Data for Enterprise/Python/Project - Bike Share/'
    print(path+CITY_DATA['chicago'])
    df = pd.read_csv(path+CITY_DATA['chicago'])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['Day_of_week'] = df['Start Time'].dt.weekday_name
    
    print(df['User Type'].value_counts())
    print(df)




if __name__ == "__main__":
	main()
