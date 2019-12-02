import time
import calendar as cal
import pandas as pd
import numpy as np

# This is for capturing file name using dictionary :) 
CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

MONTH_SELECTION = {'0': 'all', '1': 'January', '2': 'February', '3': 'March', '4': 'April' , '5': 'May', '6': 'June'}
DAY_SELECTION = {'0': 'all', '1': 'Monday', '2': 'Tuesday', '3': 'Wednesday', '4': 'Thursday', '5': 'Friday', '6': 'Saturday', '7': 'Sunday'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    Cities = ""
    Month = ""
    Day = ""

    for key in CITY_DATA:
        Cities += key + "| "
    for key, value in MONTH_SELECTION.items():
        tempMon = key + ': ' + value
        Month += tempMon + "| "
    for key, value in DAY_SELECTION.items():
        tempDay = key + ': ' + value
        Day += tempDay + "| "

    print('Before we begin, please select the filter that you would to use for : City, Month and Day of week \n')
    # TO DO: get user input for city (chicago, new york city, washington). 
    # HINT: Use a while loop to handle invalid inputs
    
    User_City = input("\n1. Please enter a city from these option: " + Cities + " \n").title()
    while (User_City in CITY_DATA) == False:
        User_City= input('Invalid entry!! please use a correct city: \n').title()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    User_Month = input("\n2. Please enter the month ( " + Month +"). \n Use number as an input (Ex. 0 as \'all month\', 1 as January): \n")
    while (User_Month in MONTH_SELECTION ) == False:
        User_Month = input('Invalid entry!! Please Enter a correct Month : '+ Month + "\n Use number as an input (Ex. 0 as \'all month\', 1 as January): \n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    User_Day = input("\n3. Please enter the Day of week: (" + Day + " )\n Use number as an input (Ex. 0 as \'all\', 1 as Monday): \n")
    while (User_Day in DAY_SELECTION ) == False:
        User_Day = input('Invalid entry!! Please Enter a correct Day : (' + Day + ") \n Use number as an input (Ex. 0 as \'all\', 1 as Monday): \n")

    print('-'*40)
    return User_City, User_Month, User_Day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print('Loading data, please wait','.'*20)
    df = pd.read_csv(CITY_DATA[city])
   
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['Start Time'].dt.month
    df['Day_Of_Week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != '0':
        # use the index of the months list to get the corresponding int
        #months = ['January', 'February', 'March', 'April', 'May', 'June']
        #month = months.index(month)

        # filter by month to create the new dataframe
        df = df[df['month'] == int(month)]

    # filter by day of week if applicable
    if day != '0':
        # filter by day of week to create the new dataframe
        str_day = DAY_SELECTION[day]
        df = df[df['Day_Of_Week'] == str_day]
    print('Data loading completed','.'*20)
    print('-'*40)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    Ask_show_raw_data(df)

    start_time = time.time()
    # TO DO: display the most common month
    print('Most common month: ', MONTH_SELECTION[str(df['month'].mode()[0])])
    print('With a count of: ', (df['month'] == df['month'].mode()[0]).sum())

    # TO DO: display the most common day of week
    print('Most common day of week: ', df['Day_Of_Week'].mode()[0])
    print('With a count of: ', (df['Day_Of_Week'] == df['Day_Of_Week'].mode()[0]).sum())

    # TO DO: display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    print('Most common hour: ', df['hour'].mode()[0], ' hours')
    print('With a count of: ', (df['hour'] == df['hour'].mode()[0]).sum())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    Ask_show_raw_data(df)
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common Start Station: ', df['Start Station'].mode()[0])
    print('With a count of: ', (df['Start Station'] == df['Start Station'].mode()[0]).sum())

    # TO DO: display most commonly used end station
    print('Most common End Station: ', df['End Station'].mode()[0])
    print('With a count of: ', (df['End Station'] == df['End Station'].mode()[0]).sum())

    # TO DO: display most frequent combination of start station and end station trip
    df['Combined_Start_End'] = df['Start Station'] + " | " + df['End Station']
    print('Most frequent Combined Start and End stations is: ', df['Combined_Start_End'].mode()[0])
    print('With a count of: ', (df['Combined_Start_End'] == df['Combined_Start_End'].mode()[0]).sum())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    Ask_show_raw_data(df)
    start_time = time.time()
    df['Travel Time'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    print("The total travel time is : " , (df['Travel Time'].sum()))

    # TO DO: display mean travel time
    print('The average of travel time for this data set is: ',(df['Travel Time'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    Ask_show_raw_data(df)
    start_time = time.time()

    col_name = check_if_column_exist(df,'User Type', 'Gender', 'Birth Year')

    # TO DO: Display counts of user types
    if 'User Type' in col_name:
        print('The count of user types are as follow : \n' , df['User Type'].value_counts(), '\n')

    # TO DO: Display counts of gender
    if 'Gender' in col_name:
        print('The count of Gender are as follow : \n' , df['Gender'].value_counts(), '\n')

    else:
        print('There were no information about the Gender\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in col_name:
        print('The earliest birth year is : ', int(df['Birth Year'].min()))
        print('The most recent birth year is : ', int(df['Birth Year'].max()))
        print('The most common birth year is : ', int(df['Birth Year'].mode()[0]))
    else:
        print('There were no information about the Birth Year\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def check_if_column_exist(df,*column_name):
    col_name = []
    index = 0
    while index < len(column_name):
        #Check if column exist or not
        if column_name[index] in df:
            col_name.append(column_name[index])
        index += 1
    return col_name

#Load data into dataframe based user input in load_data(city, month, day)
def start_init():
    print('Hello! Let\'s explore some US bikeshare data! \n')
    city, month, day = get_filters()
    df = load_data(city, month, day)

    return df

#This fuction with show first 5 line of data
def Ask_show_raw_data(df):
    _choice = input("Would you like to see first 5 lines of data?: [Y/N] \n").upper()
    #print(_choice)
    while (_choice != "Y" and _choice != "N"):
        _choice = input("Invalid input| Would you like to see first 5 lines of data?: [Y/N] \n").upper()
    
    if _choice == "Y" :
        print("\n")
        print(df.head(5)) 
        print("\n")

def Menu():
    print('Please select an item from the menu below (Enter a # 1-5 only ) \n')
    print('1. Displays statistics on the most frequent times of travel. \n')
    print('2. Displays statistics on the most popular stations and trip. \n')
    print('3. Displays statistics on the total and average trip duration. \n')
    print('4. Displays statistics on bikeshare users.\n')
    print('5. Fire all at once.\n')
    while True: 
        try:
            choice = int(input())
            while choice <= 0 or choice >5:
                choice = int(input('Invalid input: Please select an item from the menu below (Enter a # 1-5 only)\n'))
            return choice
        except:
            print('Invalid input: Please enter a # 1-5 only\n')
        finally:
            print("This is not a number or number is out of range, please enter a # 1-5 only\n")

def main():
    
    while True:
        df = start_init()
        
        menu_choice = Menu()
        #Try to find a switch case like other lanuage, but python does not have it :). Did a research and result with a dict/ funt(). It's easier to use If and Else
        if menu_choice == 1:
            print('1. Displays statistics on the most frequent times of travel.')
            time_stats(df)
        elif menu_choice == 2:
            print('2. Displays statistics on the most popular stations and trip.')
            station_stats(df)
        elif menu_choice == 3:
            print('3. Displays statistics on the total and average trip duration.')
            trip_duration_stats(df)
        elif menu_choice == 4:
            print('4. Displays statistics on bikeshare users.')
            user_stats(df)
        else:
            print('Fire all at once')
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while (restart != 'yes' and restart != 'y' and restart != 'no' and restart != 'n' ):
            restart = input('Invalid input| Would you like to restart? Enter yes or no.\n').lower()

        if restart.lower() != 'yes' and restart.lower() != 'y':
            print ('\n Thank you for using our statistic program, have a good day. \n')
            break


if __name__ == "__main__":
	main()
