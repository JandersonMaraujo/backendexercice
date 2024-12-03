# backendexercice
An API to provide information for common and admin users

## Development Environment

- The server needs to have  <strong>Docker</strong> and <strong>Docker Compose</strong> installed.
- Clone the given repository with the following command: `git clone https://github.com/JandersonMaraujo/backendexercice.git`

## Environment Variables

The file with environment variables is located in the subdirectory `deploy`. Use the file `env.example` as reference.

- `deploy/.env`: Docker Compose variables

- Do not forget to setup proxy variables if you're behind a proxy server

## Pre deploy
Execute the pre_deploy shell file to prepare the volumes:
- got ot deploy folder and execute:
- `sh ./prepare_deploy`

- ## Build

- Access the subdirectory `deploy` from Backend Exercice root directory and execute:
 
#### Development
- `docker-compose -f dev.yml build --no-cache`
- `docker-compose -f dev.yml pull`
- `docker-compose -f dev.yml up -d`

#### Production
- `docker-compose -f prod.yml build --no-cache`
- `docker-compose -f prod.yml pull`
- `docker-compose -f prod.yml up -d`

#### Migrations
- For the very first time you access the app <strong>backendexercice</strong> container, run migrations:
  - `python manage.py migrate`

#### Users and JWT tokens
- As well as you did with migrations, you need to create a superuser in order to better manage your app:
  - `python manage.py createsuperuser`
- Create a JWT toke to him calling the endpoint `/token` and providing username and password:
- Now, it's time to create at least more two users, just to get the API easy to exercice. It is optional. This users will have the `user` and `admin` roles, respectively. You can do this providing the following fields in the payload:
- <stong>User</stong> role user
  `{
	"username": "user",
	"first_name": "John",
	"last_name": "Doe",
	"email": "john@example.com",
	"role": "user",
	"password": "L0XuwPOdS5U"
}`
- <stong>Admin</stong> role User
  -  `{
	"username": "admin",
	"first_name": "Admin",
	"last_name": "Master",
	"email": "admin@example.com",
	"role": "admin",
	"password": "JKSipm0YH"
}`

## API documentation

All endpoints available (except `/health`,`token`,`user` and `admin`) have `get`, `post`, `patch` and `delete` verbs:
- `/token` to refresh the the jwt token for the current user((anyone can perform thisaction)
  - `post`
- `/health` to check whether the api is healthy (anyone can perform actions)
  - `get`
- `user` to get information about the current user as well as his purchases (only users with `user` role can perform actions)
  - `get`
- `admin` to get information about the current user as well as his reports (only users with `admin` role can perform actions)
  - `get`
- `/product` to manage products (only users with `admin` role can perform actions)
  - `get`
  - `post`
  - `patch`
  - `delete`
- `/sale` to manage sales (only users with `admin` role can perform actions)
  - `get`
  - `post`
  - `patch`
  - `delete`
- `/report` to manage reports (only users with `admin` role can perform actions)
  - `get`
  - `post`
  - `patch`
  - `delete`
- `/server-user` to manage users (only users with `admin` role can perform actions)
  - `get`
  - `post`
  - `patch`
  - `delete`

