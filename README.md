# Setting up The Subscriptions Web API

1. Use the command `git clone ` to clone the repository.
2. Change your working directory to *backend*.
3. Install dependencies with `pip3 install -r requirements.txt`
4. Create a *.env* file defining the following environment variables:
```
FLASK_ENV=development
POSTGRES_USER=postgres
POSTGRES_PASSWORD=[password of your choice]
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=subscriptions
```
5. Run the docker command `docker run -d --name subscriptions -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=abcde12345 -e POSTGRES_DB=subscriptions -e POSTGRES_HOST=localhost -e POSTGRES_PORT=5432 -v db_volume:/var/lib/postgresql postgres:latest` to containerize the database.
6. Run the 3 commands: `flask db init`, `flask db migrate`, and `flask db upgrade` to initialize, make migrations, apply migrations to your postgres database.
7. Start your flask api with the command `flask run --host localhost --port 8000`. 
8. To limit user error, subscription types are manually entered into the database and referenced by their uuid when adding customers. This can be done by using Postico or another GUI to add fields to your local database. To create a uuid for each row, it is recommended to open a python shell in your terminal and import the uuid module using `import uuid` and then print a new uuid to use for each subscription type using `print(uuid.uuid4())`
9. The 'POST' request used in the example can be tested using Insomnia or another API Client with the following json data:
```
{
  "customer": {
    "first_name": "Ernest",
    "last_name": "Hemingway",
    "address_1": "907 Whitehead St",
    "address_2": "",
    "city": "Key West",
    "state": "FL",
    "postal_code": "33043",
    "subscription_id": uuid_from_step_8,    
    "gifts":[
      {
        "gifter_email": "tester@gmail.com",
        "recipient_email": "rec3@gmail.com",
        "subscription_id": uuid_from_step_8
      }, {
        "gifter_email": "tester@gmail.com",
        "recipient_email": "rec4@gmail.com",
        "subscription_id": uuid_from_step_8
        }
    ]
  }
}
```