# interview-concepts
Testing ideas for giving interviews to full stack dev candidates

# Prompt for candidates

We are developing a product that lets users place orders from nearby restaurants and get them delivered to their location.

Currently, we have created part of the api to return data from our Mongo database and a Vue.js frontend to display a map and place orders.

However, the data is currently hard coded to display two points on the map.  We would like to fetch restaurants from our database instead

## Walkthrough

You can start the web app by running `docker-compose up`

All dependencies should automatically be installed and MongoDB should automatically be populated.  The code will be hot reloaded as you make changes to the code.

### API

The API is implemented in Python with [FastAPI](https://fastapi.tiangolo.com/).

The following endpoints are available

http://localhost:3000/

http://localhost:3000/restaurants

http://localhost:3000/neighborhoods

### Frontend

The frontend is a [Vue.js 3.0](https://vuejs.org/guide/introduction.html) single page app.

It will be accessible from http://localhost:8080/

The library used to render the map is [Leaflet](https://leafletjs.com/)

## Your task

Refactor the web app to fetch data from the backend API instead of the using hard coded data.  You may need to reformat the data to display it with Leaflet.

You will also be required to review a pull request that will display the delivery range when a marker on the map is clicked.

## Troubleshooting

If the dashboard errors out, try deleting the `dashboard/node_modules` directory and running `docker-compose up` again.

# Prompt for interviewers

Ask the candidate about the pros and cons for transforming the MongoDB response from the backend or frontend.

How would they choose to persist order data between page reloads?

How would they design and deploy the application in production?

For the pull request review, check the quality of their comments and if the tone is appropriate for collaborating with a team.
