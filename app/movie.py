from dotenv import load_dotenv
from os.path import join, dirname
import json
import os
import requests
import csv
import datetime
from IPython import embed
import itertools

########### Environent Setting##################

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
api_key = os.environ.get("themoviedb_API_KEY") or "OOPS. Please set an environment variable named 'themoviedb_API_KEY'."

#api_key = "d322c4679b5b52a4ea8558d17053bcf9"

########## Menu ###############################
menu = f"""
-----------------------------------
Welcome to Your Movie Database
-----------------------------------
Please Select a Operation
    operation | description
    --------- | ------------------
    'Now'     | New Movies in Theaters Now.
    'Movie'   | Show Information of A Movie.
    'Actor'   | Filmography of an Actor/Actress.
    'Popular' | Most Popular Movies.
    'Lucky'   | Give a Random Movie Suggestion.
    'Exit'    | Exit the application. """



def now():
    print("now")
    request_url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=en-US&page=1"
    now_playing_r = requests.get(request_url)
    now_playing_all = json.loads(now_playing_r.text)
    now_playing = now_playing_all["results"]
    now_titiles = []
    now_overviews = []
    now_dates = []
    for x in now_playing:
        now_titile = x["title"]
        now_overview = x["overview"]
        now_date = x["release_date"]
        now_titiles.append(now_titile)
        now_overviews.append(now_overview)
        now_dates.append(now_date)
    print(now_titiles)




def movie_info():
    global m_search_result
    while True:
        movie_name = input("Plase Enter a Movie Name: ")
        movie_name_ns = movie_name.replace(" ", "%20")
        request_url2 = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&query={movie_name_ns}&page=1&include_adult=false"
        response = requests.get(request_url2)
        status_code = response.status_code
        #print(status_code)
        if status_code == 200:
            pass
        else:
            print("Something Went Wrong, Status Code:",status_code)
            exit()
        all_search_result = json.loads(response.text)
        check_result = int(all_search_result["total_results"])
        if check_result == 0:
            print("Please Try Again, No Search Found")
        else:
            break

    m_search_result = all_search_result["results"]
    number_result = len(m_search_result)
    total_result = int(all_search_result["total_results"])
    name_results= []
    date_results= []
    lang_results= []

    for m in m_search_result:
        name_result = m["title"]
        date_result = m["release_date"]
        lang_result = m["original_language"]
        name_results.append(name_result)
        date_results.append(date_result)
        lang_results.append(lang_result)



        #print(date_results)

    print("Movie Name Search Results")
    print("-------------------------")
    for m in range(0,number_result):
        print(f"""{m+1}. Movie Name: {name_results[m]}
        Release Date: {date_results[m]}, Original Language: {lang_results[m]}""")


def movie_info2():
    while True:
        input_id = input("Please Enter The Number of The Movie Which You Want to Know More: ")
        try:
            float(input_id)
            input_idt = int(input_id)
            if 1<=input_idt<=20:
                break
            else:
                print("YOUR INPUT IS OUT OF RANGE, PLEASE ENTER A NUMBER BETWEEN 1 AND 2O")
        except ValueError as e:
            print("CHECK YOUR INPUT. NO STRING, ONLY NUMARTIC PLEASE TRY ANOTHER (Example: 1)")

    real_input = input_idt-1
    movie_id = m_search_result[real_input]["id"]
    #print(movie_id)
    request_url3 = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    movie_detail_result = requests.get(request_url3)
    movie_detail = json.loads(movie_detail_result.text)
    #print(movie_detail)
    movie_title = movie_detail["title"]
    movie_otitle = movie_detail["original_title"]
    movie_release_date = movie_detail["release_date"]
    movie_olang = movie_detail["original_language"]
    movie_overview = movie_detail["overview"]
    request_url3 = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}"
    movie_cast_result = requests.get(request_url3)
    movie_cast_all = json.loads(movie_cast_result.text)
    movie_cast = movie_cast_all["cast"]

    chara_results = []
    name_results = []

    for p in range(0,4):
        chara_result = movie_cast[p]["character"]
        name_result = movie_cast[p]["name"]
        chara_results.append(chara_result)
        name_results.append(name_result)
    print("---------------------------------------------")
    print("Movie Original Title:", movie_otitle)
    print("Movie English Title: ", movie_title)
    print("Movie Release Date: ", movie_release_date)
    print("Movie Original Language: ", movie_olang)
    print("Movie Casts: ")
    for p in range(0,3):
        print(f""" ++ Actor {name_results[p]} as {chara_results[p]} """)
    print("Movie Overview: ", movie_overview)
    print("---------------------------------------------")

def actor():
    print("actor")
def popular():
    print("popular")
def lucky():
    print("lucky")


def run():
    fst_input = input("Please Select An Operation: ")
    fst_input = fst_input.title()

    if fst_input == "Now":
        now()
    elif fst_input == "Movie":
        movie_info()
        movie_info2()
    elif fst_input == "Actor":
        actor()
    elif fst_input == "Popular":
        popular()
    elif fst_input == "Lucky":
        lucky()
    elif fst_input == "Exit":
        quit()
    else:
        print("OOPS SORRY. PLEASE TRY AGAIN.")
        return run()


if __name__ == "__main__":
    print(menu)
    run()
