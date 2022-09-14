import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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
    city = input("which city u want data about (chicago, new york city, washington) \n").lower()
    if city == 'chicago' or city == 'new york city' or city == 'washington':
        print('Going to get info about ', city.title())
    else:
        while city != 'chicago' or city != 'new york city' or city != 'washington':
            city = input("please enter name of the city as presented: (chicago, new york city, washington) \n").lower()
            if city == 'chicago' or city == 'new york city' or city == 'washington':
                break

    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    s = input("would u like to filter the data for day , month or both \n")
    if s == 'both':
        month = input("enter the month, as follow : jan, feb, mar, apr, may, jun \n").lower()
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        while month not in months:
            month = input('invalid data please enter the month exactly as follow : jan, feb, mar, apr, may, jun \n').lower()
            if month in months:
                break
        day = input(
            "enter the day as follow : sunday , monday , tuesday , wednesday , thursday , friday , saturday \n").lower()
        days = ['sunday', ' monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        while day not in days:
            day = input(
                'invalid data please enter the month exactly as follow : sunday , monday , tuesday , wednesday , thursday , friday , saturday  \n').lower()
            if day in days:
                break
    elif s == 'day':
        month = 'all'
        day = input("enter the day as follow : sunday , monday , tuesday , wednesday , thursday , friday , saturday \n").lower()
        days = ['sunday' ,' monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday' ]
        while day not in days:
            day = input(
                'invalid data please enter the month exactly as follow : sunday , monday , tuesday , wednesday , thursday , friday , saturday  \n').lower()
            if day in days:
                break
    elif s == 'month':
        day = 'all'
        month = input("enter the month, as follow : jan, feb, mar, apr, may, jun \n").lower()
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        while month not in months:
            month = input('invalid data please enter the month exactly as follow : jan, feb, mar, apr, may, jun \n').lower()
            if month in months :
                break

    print('-' * 40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if month != 'all':
        month = months.index(month) + 1
        df = df.loc[(df['Start Time'].dt.month == int(month))]
    if day != 'all':
        df = df.loc[(df['Start Time'].dt.day_name() == day.title())]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Common Month: ', popular_month)

    # TO DO: display the most common day of week
    df['weekday'] = df['Start Time'].dt.weekday_name
    popular_weekday = df['weekday'].mode()[0]
    print('Most Common day of week: ', popular_weekday)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start = df['Start Station'].mode()[0]
    print('The most start station is:\n', most_start)

    # TO DO: display most commonly used end station
    most_end = df['End Station'].mode()[0]
    print('The most end station is:\n', most_end)

    # TO DO: display most frequent combination of start station and end station trip
    most_freq = (df['Start Station'] + df['End Station']).mode()[0]
    print('The most freq station is:\n', most_freq)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()


    print('The Total Trip duration \n', total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The mean Trip duration \n', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()


    print('The total count of the Users:\n', user_count)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('The total count of the Users gender:\n', gender_count)
    else:
        print('Sorry, The data about the chosen city gender of users is not available')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        early_year = df['Birth Year'].min()
        last_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('The Earliest year of birth is: ', early_year)
        print('The last year of birth is: ', last_year)
        print('The most common year of birth is: ', common_year)
    else:
        print('Sorry, The data about the chosen city birth date of users is not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
def display_data(df):
    x = 0
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? \n").lower()
    while view_data == 'yes':
        print(df.iloc[x:x+5])
        x = x +5
        view_display = input("Do you wish to continue?: \n").lower()
        if view_display == 'no':
            break
        elif view_display == 'yes':
            continue
        else:
            q = input('invalid date,Do you wish to continue? answer by (yes) or (no) \n').lower()
            while q != 'yes' or q != 'no':
                q=input('invalid date,Do you wish to continue? answer by (yes) or (no) \n').lower()
                if q == 'yes' or q == 'no' :
                    break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
