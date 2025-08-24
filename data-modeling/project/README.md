# Data Modeling Project - SparkifyDB ETL Process

## Summary
Sparkify, a startup company offering music streaming, required an ETL process to understand their users' consumption patterns. This process takes in usage data (`log_data`) and synthesizes it with song data (`song_data`). The resulting database can then be used by analysts for determining things like popular songs and artists, peak hours in listening times, and so on. 

### Prerequisites
- PostgreSQL 17.5+
- Python 3.10+
  - 3.10.7 was used in development and testing


### Running it
Data is assumed to be stored in the same location as the .py files, in paths `./data/log_data` and `./data/song_data`.

To run the scripts, download the files and open a terminal/command prompt with the working directory set to the location of the download. 

```bash
python create_tables.py
python etl.py
```

etl.py will output the number of files found in `./data/*` and reports progress to the console.

### Files
- data/log_data/*.json
  - Data elements regarding user actions in the Sparkify webapp.
- data/song_data/*.json
  - Data elements regarding songs in the Sparkify library
- create_tables.py
  - Creates the database and tables required for this project.
- etl.py
  - The extract-transform-load pipeline script, which will move the data from the .json files to the PSQL database and tables created by create_tables.py
- etl.ipynb
  - A lengthened version of etl.py that was used to guide its creation.
- README.md
  - This is what you are reading now. This explains various aspects of this project.
- sql_queries.py
  - A module containing:
    - Insert queries for each table
    - A SELECT query to help with generating the songplays table
    - CREATE/DROP TABLE statements
- test.ipynb
  - A notebook containing test cases used to validate table creations and correct usage of datatypes.

## Database Schema
This database is a star schema - the fact table, `songplays`, derives all of its information from the other dimension tables. This is beneficial because it makes querying easier and simpler.

### Fact Table
- songplays - records in log data associated with song plays i.e. records with page `NextSong`
    - songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables
- users - webapp users
    - user_id, first_name, last_name, gender, level
- songs - songs in music database
    - song_id, title, artist_id, year, duration
- artists - artists in music database
    - artist_id, name, location, latitude, longitude
- time - timestamps of records in songplays broken into specific units
    - start_time, hour, day, week, month, year, weekday

