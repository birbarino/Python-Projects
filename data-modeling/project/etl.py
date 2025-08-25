import os
import sys
import glob
import psycopg2
import pandas as pd
from sql_queries import *

def process_song_file(cur, filepath):
    """
    Description: Given a filepath and a cursor object, this
    function will insert data into the artists and songs tables
    in the database.

    Arguments:
        cur: the cursor object.
        filepath: log data or song data file path.

    Returns:
        None
    """   

    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = list(df[['song_id', 'title', 'artist_id', 'duration']].values[0])
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Description: Given a filepath and a cursor, this function inserts
    resulting data into time, users, and songplays tables in the sparkify
    database. It also constructs the broken-out columns for the time table,
    i.e. day, week, month, etc.

    Arguments:
        cur: the cursor object.
        filepath: log data or song data file path.

    Returns:
        None
    """

    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == "NextSong"]

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data = list([
        t,                    # timestamp
        t.dt.hour,
        t.dt.day,
        t.dt.strftime("%U").astype('int32'),  # week of year (starts on Sun)
        t.dt.month,
        t.dt.year,
        t.dt.strftime('%w').astype('int32')   # weekday
    ])

    column_labels = ['start_time','hour','day','week','month','year','weekday']
    time_df = pd.concat(time_data, axis=1)
    time_df.columns = column_labels

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[["userId", "firstName", "lastName", "gender", "level"]].drop_duplicates()
    user_df.reset_index(drop=True, inplace=True)

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (pd.to_datetime(row.ts, unit="ms"), 
                         row.userId, 
                         row.level, 
                         songid, 
                         artistid, 
                         row.sessionId, 
                         row.location, 
                         row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Description: Given access to a database, this function will 
    iterate over all files in the given filepath and execute the 
    provided function on them. Pending changes to the database are
    then committed.

    Arguments:
        cur: the cursor object.
        conn: connection to the PSQL database.
        filepath: log data or song data file path.
        func: function to transform the provided data with.

    Returns:
        None
    """
   
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    Description: This function performs the primary goals of this script and
    makes use of the other functions within. The result is a PSQL database
    containing the tables needed by Sparkify's analysts.

    Arguments:
        None

    Returns:
        None
    """

    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    os.chdir(sys.path[0])
    process_data(cur, conn, filepath='./data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='./data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()