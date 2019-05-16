
# Mastermind RESTful API

This repository contains a Django DRF RESTful API production ready for the known game [Mastermind](https://en.wikipedia.org/wiki/Mastermind_%28board_game%29). It was developed in 6 hours (without counting documentation and DevOps related stuff with Docker) with TDD.

## TECHNOLOGY STACK

 - Python
 - Django
 - Django Rest Framework
 - PyCharm (IDE)
 - Travis (CI)
 - Docker (deployment)


## ENDPOINTS

| URL | METHOD | DATA | INFO | RETURNS |
|--|--|--|--|--|
| /game | GET |  ||List of games with ids and states
| /game | POST | Optional: c1,c2,c3,c4 |Pass a color in each variable and it will create a game with that solution (this is mainly for testing purposes). If no colors are provided it creates a random game|Created game info (without the solution)
|/game/\<game:id\>|GET|||History of the game id passed. Guesses made and it's results
|/game/\<game:id\>|POST|c1,c2,c3,c4|Pass a color in each attribute to make a guess| The guess results with its black pegs (correctly guessed color and position) or white pegs (correctly guessed color but not in the exact position)

## ROADMAP / KNOWN PROBLEMS

- Travis should make tests with Docker too
- Colors should be a model with ids
- Check that colors passed in guesses are correct (because no one knows which color es "RDE")

## HOW TO USE THIS DOCKER COMPOSE

    docker-compose build
    docker-compose run mastermind python manage.py migrate
    docker-compose up -d

With this default config the API should be up and running in 0.0.0.0:8000.
In addittion, if you want to run the unittest from the docker you can run:

    docker-compose run mastermind python manage.py test
