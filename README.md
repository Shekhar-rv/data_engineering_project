# Data Engineering Project

I'm using this as a learning opportunity to work on a few data engineering projects taught by Darshil Parmar. Here is a link to the medium article.

```link
https://medium.com/@darshilp/7-end-to-end-data-engineering-projects-for-free-bf9e86d7bfe0
```

This repo will house 3 projects (with the possibility to expand).

### Project 1:
In this project the main aim is to identify an open source dataset and design a data model to ingest this data into postgres. The following are the requirements for the project:
  1. Find datasets from any of the sites such as opendata, kaggle etc (links found in description of the youtube video).
  2. Build a data model (minimum 3 tables).
  3. Write python code to create the required tables.
  4. Insert data from the files into the tables.

I found a vehicle sales data from kaggle which I feel would be good dataset for this project. The data set can be found here (also saved under src/data/):

```link
https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data?resource=download
```

## Prerequisite
  1. You should have docker installed on your local machine.
  2. An IDE for SQL, I personally use Dbeaver. You can add another service to the docker compose file such as PGAdmin which has a web UI.

## Setup
In this repo I'm trying to include a dev container which would potentially help develop a developer setup a local environment that is supported on all major platforms. This includes:
  1. Docker containers that run python and postgres at the moment.


## TODO
  1. Setup necessary packages on devcontainer
  2. Create a schema and tables
  3. Start the course to see if you were able to take into account the requirements.
  4. Add setup instructions.
  5. Set up .env file to handle postgres credentials and pass in the postgres uri to the python image.
  6. Find a way to dynamically assign postgres uri (IP address of container is static at the moment)