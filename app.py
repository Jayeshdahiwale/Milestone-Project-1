""" enter 'a' to add movie, enter 'l' to see movies, enter 'f' to find your movies and enter 'q' to quit movies
-add movies
-see movies
-find movies
-stop running the program
tasks:
[]:decide where to store movies
[]:show the user the main interface and get their inputs
[]:allow users to add movies
[]:shoe all their movies
[]:find a movie
[]:stop running the progrm when they type 'q'
"""
movies=[]
'''   movie={'name':........
     'director'=.....
     'year':......}
'''
def menu():
    user_input=input("enter 'a' to add movie, enter 'l' to see movies, enter 'f' to find your movies and enter 'q' to quit program")
    while user_input!='q':
      if user_input=='a':
        add_movies()
      elif user_input=='l':
        see_movies(movies)
      elif user_input=='f':
        find_movies()
      else :
          print('unknown command please try again')

      user_input = input(
          "enter 'a' to add movie, enter 'l' to see movies, enter 'f' to find your movies and enter 'q' to quit movies")
def add_movies():
    name=input('enter the movie name:')
    director=input('enter the director name:')
    year=input('enter the year of release:')
    movies.append({'name':name,
                   'director':director,
                  'year':year   } )
def find_movies():
    find_by=input('what property of the movie you are looking for(name/director/year):')
    looking_for=input('what are you searching for:')
    found_movies =find_by_atribute(movies,looking_for,lambda x:x[find_by])
    show_movies(found_movies)
def find_by_atribute(items,expected,finder):
    for i in items :
        found=[]
        if finder[i]==expected :
            found.append(i)
    return found
def see_movies(movies_list):
    for movie in movies_list:
      show_movies(movie)
def show_movies():

    for movie in movies:
        print(f"name:{movie['name']}")
        print(f"director:{movie['director']}")
        print(f"year:{movie['year']}")




menu()
