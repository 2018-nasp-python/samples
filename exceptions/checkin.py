#! /usr/bin/env python3
'''
Simple mood checkin application.

It requires a location and a mood parameter.

Sample Usage:

    python checkin.py "work" "concerned"


Creates and uses `checkins.csv` to persist data
'''
import csv
import datetime
import os
import sys
from typing import Tuple


checkin_file = 'checkins.csv'


def last_checkin() -> Tuple[datetime.datetime, str, str]:
    '''
    Gets the last checkin from the checkin file and returns the datetime,
    location and mood

    Returns:
        tuple: datetime, location string, mood string
    '''
    try:
        with open(checkin_file, 'r') as checkins:
            checkin_reader = csv.DictReader(checkins)
            for row in checkin_reader:
                last_checkin = row

            return (datetime.datetime.fromisoformat(last_checkin['date_time']),
                    last_checkin['location'],
                    last_checkin['mood'])

    except IndexError:
        print('Corrupt checkin file')
        sys.exit(1)

    except FileNotFoundError:
        now = datetime.datetime.now()
        checkin("initial location", "initial mood", dtime=now)
        return now, "initial location", "initial mood"


def checkin(location: str, mood: str, dtime: datetime.datetime = None) -> datetime.datetime:
    '''
    Checkin with a specific time or use current time as default along with your
    current location, and mood

    Args:
        location (str):  a brief description of your current location
        mood (str): a brief description of your current mood
        dtime (datetime.datetime, optional):  The date time of your checkin
                                              Defaults to current time

    Returns:
        datetime.datetime: the date time of the checkin
    '''
    if dtime is None:
        dtime = datetime.datetime.now()

    try:
        if os.path.isfile(checkin_file):
            with open(checkin_file, 'a', newline='') as chk_file:
                writer = csv.writer(chk_file)
                writer.writerow([dtime.isoformat(timespec='seconds'),
                                location,
                                mood])
        else:
            with open(checkin_file, 'a', newline='') as chk_file:
                writer = csv.writer(chk_file)
                writer.writerow(['date_time', 'location', 'mood'])
                writer.writerow([dtime.isoformat(timespec='seconds'),
                                location,
                                mood])

        return dtime

    except OSError as error:
        print('File writing error: {}'.format(error))
        sys.exit(1)


def timedelta_to_words(time_diff: datetime.timedelta) -> str:
    '''
    Convert timedelta to string of words descripting the time period

    Args:
        time_diff (datetime.timedelta): timedelta

    Returns:
        str: written description of timedelta
    '''
    time_diff_words = ""

    if time_diff.days > 0:
        time_diff_words += "{} days ".format(time_diff.days)

    hours = time_diff.seconds // 36000
    if hours > 0:
        time_diff_words += "{} hours ".format(hours)

    minutes = time_diff.seconds // 60 % 60
    if minutes > 0:
        time_diff_words += "{} minutes ".format(minutes)

    seconds = time_diff.seconds % 60
    if seconds > 0:
        time_diff_words += "{} seconds".format(seconds)

    return time_diff_words


def main():
    '''
    Simple implementation of mood checkin app
    '''
    try:

        location = sys.argv[1]
        mood = sys.argv[2]

    except IndexError as error:
        print('Please specify both a location and a mood when you check-in')
        print('Example: python checkin.py home meh')
        sys.exit(1)

    prev_chkin, prev_location, prev_mood = last_checkin()
    cur_chkin = checkin(location, mood)
    checkin_gap = cur_chkin - prev_chkin
    gap_string = timedelta_to_words(checkin_gap)
    print('It has been {} since your last checkin'.format(gap_string))
    print('Your have moved from {} to {}'.format(prev_location, location))
    print('Your mode has gone from {} to {}'.format(prev_mood, mood))


if __name__ == '__main__':
    main()
