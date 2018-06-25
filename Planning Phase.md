# Proposal-Phase

## Problem Statement

###Primary User

Anyone who loves watching movie

####User Needs Statement

As a movie lover who watch movies all the time have the need to know who are the main actor and actress in a certain film and when will the movie be in theater and sometime they don't know what movie to watch.

#####As-is Process Description
User currently either need to search for a movie and look for who are the actor and actress in the file or they don't know what movie to watch.
If they are looking up informaiton for a certain movie they wil need to need to find out the date when the film will be in thrater.
If they don't know what film to watch, they will search online and look for recommandation.
After review through recommandtation then they will decide what file to watch.

#####To-be Process Description
If they want info for a movie they can input the name of the film and get results.
If they want info for an actor they can input the actor name and get results.
If they want to know what movies are in theater now they can input "now" and get results.
If they want to know what are the popular movies they can input "popular" and get results.
If they just want raffle for whant movie to watch, they can simplily type suggestion then the application will output suggestion.

## Information Requirements

### Information Inputs

Choose any operation then input request info
1. Movie Name (partial are fine )
2. Actor Name (partial are fine )

### Information Outputs

1. List Movies in Theater Now
2. Movie Info
3. Actor/Actress Casting History
4. Current Popular Movies
5. Movie Suggestion

## Technology Requirements

### APIs and Web Service Requirements

[The Movie DB API Database](https://www.themoviedb.org/?language=en)

### Python Package Requirements
```
dotenv
json
os
requests
datetime
random
pdb
```

### Hardware Requirements

The application will be running on my own local laptop.
