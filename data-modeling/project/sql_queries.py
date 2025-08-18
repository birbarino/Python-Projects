# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id int,
        start_time timestamp,
        user_id int,
<<<<<<< HEAD
        level text,
        song_id text,
        artist_id text,
=======
        level int,
        song_id int,
        artist_id int,
>>>>>>> 79bbf51b52144a72f679aaea7fc64766f91c708a
        session_id int,
        location text,
        user_agent text,
        PRIMARY KEY (songplay_id)
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id int,
        first_name text,
        last_name text,
        gender text,
<<<<<<< HEAD
        level text,
=======
        level int,
>>>>>>> 79bbf51b52144a72f679aaea7fc64766f91c708a
        PRIMARY KEY (user_id)
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
<<<<<<< HEAD
        song_id text,
        title text,
        artist_id text,
=======
        song_id int,
        title text,
        artist_id int,
>>>>>>> 79bbf51b52144a72f679aaea7fc64766f91c708a
        year int,
        duration numeric,
        PRIMARY KEY (song_id)
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
<<<<<<< HEAD
        artist_id text,
=======
        artist_id int,
>>>>>>> 79bbf51b52144a72f679aaea7fc64766f91c708a
        name text,
        location text,
        latitude numeric,
        longitude numeric,
        PRIMARY KEY (artist_id)
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time timestamp,
        hour int,
        day int,
        month int,
        year int,
        weekday int,
        PRIMARY KEY (start_time)
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
<<<<<<< HEAD
    INSERT INTO songplay 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    INSERT INTO users 
    VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, duration) 
    VALUES (%s, %s, %s, %s);
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude) 
    VALUES (%s, %s, %s, %s, %s);
                       
=======
    INSERT INTO songplay VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    INSERT INTO users VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, duration) VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
    INSERT INTO artists VALUES (%s, %s, %s, %s, %s);
>>>>>>> 79bbf51b52144a72f679aaea7fc64766f91c708a
""")


time_table_insert = ("""
<<<<<<< HEAD
    INSERT INTO time 
    VALUES (%s, %s, %s, %s, %s, %s);
=======
    INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s);
>>>>>>> 79bbf51b52144a72f679aaea7fc64766f91c708a
""")

# FIND SONGS

song_select = ("""
    
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]