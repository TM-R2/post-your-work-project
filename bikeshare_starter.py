"""
Module load bike trip data and analyse them and create some statistics
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

"""



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
    # get user input for city (chicago, new york city, washington). HINT: Use
    # a while loop to handle invalid inputs
    while True:
        city = input("input for city (chicago, new york city, washington):")
        if city == "new york city":
            break
        print("not valid")
    # get user input for month (all, january, february, ... , june)
    print("-" * 40)
    all_month = ["all", "january", "february", "march", "april", "may", "june"]

    while True:
        month = input("input for month (all, january, february, ... , june):")
        if month in all_month:
            break
        print("not valid")

    print('-' * 40)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    all_days = [
        "all",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"]
    # get user input for month (all, january, february, ... , june)
    while True:
        day = input("input for day of week (all, monday, tuesday, ... sunday):")
        if day in all_days:
            break
        print("not valid")

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
   # load data file
    df = pd.read_csv(CITY_DATA[city])

    # convert Start Time to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()

    # filter by month
    if month != "all":
        month_number = [
            "january", "february", "march", "april", "may", "june"
        ].index(month) + 1
        df = df[df["month"] == month_number]

    # filter by day
    if day != "all":
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    # display the most common day of week

    # display the most common start hour

    print(f"\nThis took {time.time() - start_time} seconds.")
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    # display most commonly used end station

    # display most frequent combination of start station and end station trip

    print(f"\nThis took {time.time() - start_time} seconds.")
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    # display mean travel time

    print(f"\nThis took {time.time() - start_time} seconds.")
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    # Display counts of gender

    # Display earliest, most recent, and most common year of birth

    print(f"\nThis took {time.time() - start_time} seconds.")
    print('-' * 40)


def main():
    """Main function. Call all other programm parts"""
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
