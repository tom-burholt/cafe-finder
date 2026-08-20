

<template>
  <div class="cafe-list">
    <h1>The Porteño Cafe Finder</h1>

    <v-card>
      <div class="card-body">
        There are {{cafeCount}} cafes in Buenos Aires
      </div>
    </v-card>

    <v-card v-for="cafe in cafes" :key="cafe.id" class="cafe-card">
      <v-img :src="randomImage(cafe.id)" height="200" cover />
      <v-card-title>{{ cafe.name }}</v-card-title>
      <div class="card-body">
        <div class="mt-2"><v-icon start>mdi-map-marker</v-icon> {{ cafe.address }}</div>
        <v-btn
              class="mt-2"
              @click="cafe.showTags = !cafe.showTags"
              :prepend-icon="cafe.showTags ? 'mdi-chevron-up' : 'mdi-chevron-down'">
                Toggle tags
        </v-btn>
        <div class="mt-8" v-show="cafe.showTags">
          <v-chip v-for="(tag, index) in cafe.tag" :key="index" class="ma-1">
            {{ tag }}
          </v-chip>
        </div>
      </div>

    </v-card>
  </div>
</template>

<script>
import axios from "axios"
import CafeApi from "../api/CafeApi";
import {Store, storeKey, useStore} from 'vuex';

export default {
  name: 'Home',
  
  data() {
    return {
      cafes: [],
      showTags: false
    }
  },

  created(){
  this.fetchCafes(),
  this.$store.dispatch('cafes/fetchCafes')
  },

  methods: {
    randomImage(id) {
      return `https://picsum.photos/seed/${id}/300/200`
    },
    async fetchCafes() {
      const response = await axios.get("http://localhost:8000/api/cafes/");
      this.cafes = response.data

    },
    async loadCafes(){
      const data = await CafeApi.fetchCafes()
      this.cafes = data.map(cafe=>({
        id:cafe.id,
        cafeName:cafe.name,
        cafeAddress:cafe.address,
      }))
    },
  },
  computed: {
    cafeCount() {
      return this.$store.getters['cafes/cafeCount']
    }
  },
}
</script>

<style scoped>
.cafe-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  padding: 16px;
}
.cafe-card {
  width: 300px;
}
.card-body {
  padding: 0 16px 16px;
}
</style>
