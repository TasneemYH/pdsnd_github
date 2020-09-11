import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        choice_c = input ('Select a city to filter by: \n Enter the letter associated with the city name to select it \n [c: chicago, n: new york city, w: washington]\n')
        if choice_c.lower() == 'c':
            city ='chicago'
            print('You selected '+ city)
            break
        elif choice_c.lower() == 'w':
            city = 'washington'
            print('You selected '+ city)
            break
        elif choice_c.lower() == 'n':
            city = 'new york city'
            print('You selected '+ city)
            break
        else:
            print('That is not a valid selection!, Try again')
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        choice_m = int(input ('Select a month to filter by: \n Enter the month number to select it \n [0: All (no filter), 1: January, 2: February, 3: March, 4: April, 5: May, 6:June]\n'))
        if choice_m <=6:
            months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
            month = months[choice_m]
            print('You selected '+ month)
            break
        else:  
            print('That is not a valid selection!, Try again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        choice_d = int(input ('Select a day to filter by: \n Enter the day number to select it \n [0: All (no filter), 1: Monday, 2: Tuesday, 3: Wednesday, 4: Thursday, 5: Friday, 6:Saturday, 7: Sunday]\n'))
        if choice_d <=7:
            days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            day = days[choice_d]
            print('You selected '+ day)
            break
        else:
            print('That is not a valid selection!, Try again')
         
    print('-'*40)
    return city, month, day


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:', popular_day)
    
    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df ['trip'] = 'From:' + df['Start Station'] + ' To:' + df['End Station']
    popular_trips = df['trip'].mode()[0]
    print('Most Popular Trip:', popular_trips)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total Travel Time (in hrs):', total_travel/60/60)

    # TO DO: display mean travel time
    avg_travel = total_travel/len(df['Trip Duration'])
    print('Average Travel Time (in sec):', avg_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':      
        earliest_year = df['Birth Year'].min()
        print(earliest_year)
        
        recent_year = df['Birth Year'].max()
        print(recent_year)
        
        common_year = df['Birth Year'].mode()[0]
        print('Most Common Year of Birth:', common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays row data."""
    i = 0
    row_data = 'y'
    while row_data.lower() == 'y' or row_data.lower() == 'yes':
        row_data = input ('\nDo you want to see raw data?\n')
        print (df.iloc[i:i+5])
        i += 5
    else:
        print('-'*40)
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes' or 'y':
            break


if __name__ == "__main__":
	main()
