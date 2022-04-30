<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import RestaurantMap from './components/RestaurantMap.vue'
</script>

<template>
  <div>
    <img id="logo" alt="logo" src="./assets/logo.png" />
    <h1>RestoRun</h1>
    <RestaurantMap />
  </div>
</template>

<style>
img#logo {
  height: 180px;
  width: 180px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
