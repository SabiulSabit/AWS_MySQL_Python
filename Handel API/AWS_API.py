import requests
import pymysql
import json
from apiInfo import *

# create the connection
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = pymysql.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("cis3368.cwqlqz0ucl2d.us-east-2.rds.amazonaws.com","admin", "covid19sucks", "cis3368db")


# show all exsisting lyrics
def showAllDBData():
    sql = '''select * from results'''
    cursor = connection.cursor()
    cursor.execute(sql)
    allData = cursor.fetchall()
    print("All Saved Data: \n",allData)


# search a lyrics
def searchLyrics():
    artist_name = input("Whats's the name of the artist: ")
    track_name = input("What's the name of the track: ")
    print()
    api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
    request = requests.get(api_call)
    data = request.json()
    data = data['message']['body']
    print()
    print("Lyrics ID: ",data['lyrics']['lyrics_id'],"\n"+"Lyrics: \n"+data['lyrics']['lyrics_body'])

# search a specific lyrics and save it to db
def searchLyricsAndSaveToDB():
    artist_name = input("Whats's the name of the artist: ")
    track_name = input("What's the name of the track: ")
    print()
    api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
    request = requests.get(api_call)
    data = request.json()
    data = data['message']['body']
    ## get lyrics info
    l_id = data['lyrics']['lyrics_id']
    l_text= data['lyrics']['lyrics_body']
     
    #save to db 
    sql = '''insert into results(lyrics_id, lyrics ) values(%s, %s)'''
    cursor = connection.cursor()
    record = (l_id, l_text)
    cursor.execute(sql, record)
    connection.commit()
    print("Lyrics saved to db successfully! \n")


def sortAllDBDataByLyricsId():
    sql = '''select * from results Order By lyrics_id '''
    cursor = connection.cursor()
    cursor.execute(sql)
    allData = cursor.fetchall()
    print(allData)    


while True:
    #show the menu
    print()
    print("Musixmatch API")
    print()
    print("MENU OPTIONS")
    print("1 - Search for the lyrics of a song")
    print("2 - Search for the lyrics of a song and Save it to AWS DB")
    print("3 - Show Saved data from AWS DB")
    print("4 - Show Saved data from AWS DB Order by Lyrics ID")
    print("0 - Exit")
    print()
    choice = input("choice: ")
    print()

    if choice == "0":
        break # quite the program

    # example
    if choice == "1":
        searchLyrics() # search a specific lyrics
    if choice == "2":
        searchLyricsAndSaveToDB() # search a specific lyrics and save it to db
    if choice == "3":
        showAllDBData() # show all saved data
    if choice == "4":
        sortAllDBDataByLyricsId() # show all saved data By Lyrics Id

    print()




# Artist Name: Barbed Wire
# Track Name: Kendrick Lamer    





# create a table    
#sql = '''
# create table results (
# id int not null auto_increment,
# lyrics_id int,
# lyrics text ,
# primary key (id)
# )
# '''
# cursor = connection.cursor()
# cursor.execute(sql)