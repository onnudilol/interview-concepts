mongoimport --db api --collection neighborhoods --type json --file /docker-entrypoint-initdb.d/neighborhoods.json
mongoimport --db api --collection restaurants --type json --file /docker-entrypoint-initdb.d/restaurants.json 
