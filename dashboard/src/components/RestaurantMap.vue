<script setup>
import { onMounted, ref } from "vue";
import "leaflet";
import "leaflet/dist/leaflet.css";
import axios from "axios";

const orders = ref([]);
const order = ref({
  name: "",
  items: [],
});

// adds items to the order
function addItem() {
  order.value.items.push({ id: crypto.randomUUID(), name: "", price: null });
}

// submits an order to the list of orders
function submitOrder() {
  orders.value.push({
    id: crypto.randomUUID(),
    name: order.value.name,
    items: order.value.items,
  });
  order.value.name = "";
  order.value.items = [];
}

onMounted(() => {
  // creates popup and sets the order name when clicking the feature
  function onEachFeature(feature, layer) {
    if (feature.properties && feature.properties.name) {
      layer.bindPopup(feature.properties.name);
      layer.on("click", () => (order.value.name = feature.properties.name));
    }
  }

  // starts the map somewhere near brooklyn, nyc
  const map = L.map("map").setView([40.730002, -73.949997], 11);
  const tileLayer = L.tileLayer(
    "https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png",
    {
      maxZoom: 18,
      attribution:
        '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>',
    }
  );
  tileLayer.addTo(map);

  // adds two restaurant markers to the map
  const geojsonFeatures = [
    {
      type: "Feature",
      properties: {
        name: "Wendy'S",
      },
      geometry: {
        type: "Point",
        coordinates: [-73.961704, 40.662942],
      },
    },
    {
      type: "Feature",
      properties: {
        name: "Brunos On The Boulevard",
      },
      geometry: {
        type: "Point",
        coordinates: [-73.8803827, 40.7643124],
      },
    },
  ];
  L.geoJSON(geojsonFeatures, {
    onEachFeature,
  }).addTo(map);
});
</script>

<template>
  <div>
    <div id="map"></div>
    <h3>Orders</h3>
    <div v-for="order of orders" :key="order.id">
      <h2>{{ order.name }}</h2>
      <div v-for="item of order.items" :key="item.id">
        <p>{{ item.name }}: ${{ item.price }}</p>
      </div>
    </div>
    <button @click="addItem">Add item</button>
    <form ref="itemForm">
      <div v-for="item in order.items" :key="item.id">
        <p>{{ order.name }}</p>
        <div>
          <label for="itemName">Item</label>
          <input v-model="item.name" name="itemName" />
        </div>
        <div>
          <label for="itemPrice">Price</label>
          <input v-model="item.price" name="itemPrice" />
        </div>
      </div>
    </form>
    <button @click="submitOrder">Submit order</button>
  </div>
</template>

<style scoped>
a {
  color: #42b983;
}
#map {
  height: 360px;
  width: 80%;
  margin: auto;
}
</style>
