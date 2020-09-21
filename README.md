# OverAchiever: A study-your-own-way-app

This application allows users to create, read, update and delete flash cards to help them study for any topic they choose.

## Setup Steps for back-end Django/Python application
1. Start a new project repository.
2. 'cd' into the newly renamed cloned repo.
3. Creat a .env file
4. Add a development key to this file with a value of development (to prepare to deploy this application when ready)
5. Add a secret key in the .env file with the key of SECRET.
6. Run pipenv shell.
7. Run pipenv install.
8. Run psql
9. Run CREATE DATABASE "your_database_name";
10. Exit psql with '/q'

## Important Links
- [Deployed Api]()
- [Client Repo]()
- [Deployed Client]()

## Planning
- When brainstorming about this project, I considered that I wanted to experiment with using Django and Python on my back-end, so I wanted a fairly simple project concept with which to work. I kept with the theme of a majority of my projects (education) and thought of something I would want to use in a learning environment: flash cards! To plan out the nitty gritty of the front-end, I used a an online Miro board, a physical white board, Figma online, and regular old post-its.
- [Planning](https://imgur.com/Bax5P1E)

## User Stories
1. User must be able to create a new deck
2. User must be able to update a deck
3. User must be able to delete a deck
4. User must be able to view a single or multiple decks.
5. User must be able to create a new card in a deck.
6. User must be able to update a card in a deck.
7. User must be able to delete a card in a deck.
8. User must be able to view a single or multiple cards in a deck.
9. User must be able to sign up.
10. User must be able to sign in.
11. User must be able to change password.
12. User must be able to sign out.

## Technologies Used
- Node js
<!-- - React js -->
- Javascript
<!-- - HTML -->
<!-- - CSS/Sass -->
- Django
- Python
- Postman

<!-- ## Catalog of Routes
Verb         |	URI Pattern
------------ | -------------
GET | /decks
GET | /decks/:id
POST | /decks
PATCH | /decks/:id
DELETE | /decks/:id
GET | /cards
GET | /cards/:id
POST | /cards
PATCH | /cards/:id
DELETE | /cards/:id
GET | /sign-in
POST | /sign-up
PATCH | /change-pw
DELETE | /sign-out -->

## API End Points/ Catalog of Routes

| Verb   | URI Pattern            | Controller#Action           | Token Required  |
|--------|------------------------|-----------------------------|-----------------|
| POST   | `/sign-up/`            | `users#signup`              | `false`         |
| POST   | `/sign-in/`            | `users#signin`              | `false`         |
| DELETE | `/sign-out/`           | `users#signout`             | `true`          |
| PATCH  | `/change-pw/`          | `users#changepw`            | `true`          |
| GET    | `/cards/`              | `cards#index`               | `true`          |
| POST   | `/cards/`              | `cards#create`              | `true`          |
| GET    | `/cards/<int:pk>`      | `cards#show`                | `true`          |
| PATCH  | `/cards/<int:pk>`      | `cards#update`              | `true`          |
| DELETE | `/cards/<int:pk>`      | `cards#delete`              | `true`          |
| GET    | `/decks/`              | `decks#index`               | `true`          |
| POST   | `/decks/`              | `decks#create`              | `true`          |
| GET    | `/decks/<int:pk>`      | `deck#show`                 | `true`          |
| PATCH  | `/decks/<int:pk>`      | `cards#update`              | `true`          |
| DELETE | `/decks/<int:pk>`      | `cards#delete`              | `true`          |

## Unsolved Problems
- Still need to... edit card_views and card serializers to include the ability to patch and delete cards.
- Would eventually like to ... update the model of the cards and decks to include an ability to toggle 'nailed it', as a user.

## Images
#### Wireframes:
![Screen Shot 2020-09-16 at 8 47 36 AM](https://media.git.generalassemb.ly/user/27368/files/17b4c800-fc23-11ea-8114-dca1816082bb)

---

#### ERD:
![Screen Shot 2020-09-16 at 8 47 55 AM](https://media.git.generalassemb.ly/user/27368/files/5fd3ea80-fc23-11ea-80d2-f12a73c17bc0)

---

<!-- django deployed app -->
