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

# For interviewers

Ask the candidate about the pros and cons for transforming the MongoDB response from the backend or frontend.

How would they choose to persist order data between page reloads?

How would they design and deploy the application in production?

For the pull request review, check the quality of their comments and if the tone is appropriate for collaborating with a team.

Ideally the data should be directly projected in the correct format by MongoDB by using the aggregation pipeline like this

```
@app.get("/neighborhood")
async def get_nearest_neighborhood(lat, lon):
    pipeline = [
        {
            '$match': {
                'geometry': {
                    '$geoIntersects': {
                        '$geometry': {
                            'type': 'Point',
                            'coordinates': [lat, lon]
                        }
                    }
                }
            }
        },
        {
            '$project': {
                '_id': 0,
                'type': 'Feature',
                'properties': {
                    'name': '$name'
                },
                'geometry': '$geometry'
            }
        }
    ]
    neighborhood = await db["neighborhood"].aggregate(pipeline)

    return neighborhood
```

Check if they actually tested the PR according to the description and noticed these two bugs

1. Clicking a point will set the order name to any feature's name, even if it's a neighborhood.  It should only set the name if it's a restaurant.
2. Clicking a marker repeatedly will keep stacking layers.  The neighborhood layer should be removed before adding the nearest neighborhood to a point like this

```
  function onEachFeature(feature, layer) {
    ...

    layer.on("click", function() {

    if(layer.feature.geometry && layer.feature.geometry.type === "Point") {
      order.value.name = feature.properties.name;
      map.eachLayer(function(layer) {
      if(layer.feature && layer.feature.geometry.type === "Polygon") {
        layer.remove();
      }
    });
    }
  }
```
