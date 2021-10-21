import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("\nWhich country do you want from these countries, New York City, Chicago or Washington?\n")
      if city not in CITY_DATA:
        print("please write the city correctly.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nWhich month do you want, choose from January to June or all?\n")
      if month not in ('January', 'february', 'March', 'April', 'May', 'june', 'all'):
        print("please write the month correctly.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nWhich day do you want, choose from day of week or all?\n")
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("please write the day correctly")
        continue
      else:
        break

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
        months = ['January', 'February', 'March', 'April', 'May', 'June']
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

    most_popular_month = df['month'].mode()[0]
    print('most common month:', most_popular_month)


    # TO DO: display the most common day of week

    most_popular_day = df['day_of_week'].mode()[0]
    print('most common day of week:', most_popular_day)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    most_popular_hour = df['hour'].mode()[0]
    print('most common start hour:', most_popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Most_popular_start_station = df['Start Station'].mode()[0]
    print('most commonly used start station:', Most_popular_start_station)


    # TO DO: display most commonly used end station

    Most_popular_end_station = df['End Station'].mode()[0]
    print('\nmost commonly used end station:', Most_popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip

    combination_station = (df['Start Station']+' '+df['End Station']).mode()[0]
    print('most frequent combination of start station and end station',combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_time = (df['Trip Duration']).sum()
    print('total travel time:', total_time/3600,' hours')


    # TO DO: display mean travel time

    mean_time = df['Trip Duration'].mean()
    print('mean travel time:', mean_time/3600,' hours')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types

    user_type = df['User Type'].value_counts()
    print('counts of user types:\n', user_type)

    # TO DO: Display counts of gender

    try:
      gender = df['Gender'].value_counts()
      print('\n counts of gender:\n', gender)
    except KeyError:
      print("No data available for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      earliest= int(df['Birth Year'].min())
      print('\n earliest year of birth:\n', earliest)
    except KeyError:
      print("No data available for this city.")

    try:
      recent = int(df['Birth Year'].max())
      print('\n most recent year of birth:\n', recent)
    except KeyError:
      print("No data available for this city.")

    try:
      common = int(df['Birth Year'].mode()[0])
      print('\n most common year of birth:\n', common)
    except KeyError:
      print("No data available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data) == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Would you like to continue with the next 5 rows ? Enter yes or no\n'").lower()
        continue 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
      


if __name__ == "__main__":
	main()