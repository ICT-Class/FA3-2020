# An example of FA3 in the context of Pokemon

This is an exmaple project for FA3 created by Mr Wong.

## /API Server

API Server is a REST API that serve data through API endpoints.
API Server uses SQLite database and demonstrates the use of SQL to perform CRUD operations.
No object-relational mapper like sqlalchemy used.

![ER](https://github.com/IT-class-repo/FA3-2020/raw/master/ERD.png "ER")

Endpoints as follows:

##### Pokemon Api

- pokemon (GET) - Retrieve allpokemon
- pokemon/\<int> (GET, PUT, DELETE) - Retrieve, update, delete a pokemon
- pokemon/add (POST) - Add a pokemon

##### User Api

- user (GET) - Retrieve user
- user/\<int> (GET, PUT, DELETE) - Retrieve, update, delete a user
- user/add (POST) - Add a user

##### Comment Api

- comment (GET) - Retrieve comment
- comment/\<int> (GET, PUT, DELETE) - Retrieve, update, delete a comment
- comment/userId/\<int>/ (GET) - Retrieve comment(s) from a given userId only
- comment/caughtId/\<int>/ (GET) - Retrieve comment(s) from a given caughtId only
- comment/add (POST) - Add a comment

##### Caught Api

- caught (GET) - Retrieve caught
- caught/\<int> (GET, PUT, DELETE) - Retrieve, update, delete a caught
- caught/pokeId/\<int>/ (GET) - Retrieve caught(s) from a given pokeId only
- caught/userId/\<int>/ (GET) - Retrieve caught(s) from a given userId only
- caught/add (POST) - Add a caught

## /Web Server

/Web Server uses Flask framework and connects to the API server

![UI](https://github.com/IT-class-repo/FA3-2020/raw/master/Pokemon Social UI.png "UI")

## Copyright

This project is licensed under the terms of the MIT license - mit
