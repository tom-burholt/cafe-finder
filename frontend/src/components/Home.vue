<template>
  <div class="big-container">
  <div class="left-side">
    <div>
      <h1>The Porteño Cafe Finder</h1>
    </div>
    <v-card>
      <div class="card-body" style="padding:16px">
        There are {{cafeCount}} cafes in Buenos Aires
      </div>
    </v-card>
    <BarrioFilter />
  </div>
  <div class="cafe-list">
 
    <CafeList />
  </div>
  </div>
</template>

<script>
import axios from "axios"
import CafeApi from "../api/CafeApi";
import {Store, storeKey, useStore} from 'vuex';
import { mapGetters } from "vuex/dist/vuex.cjs.js";
import BarrioFilter from './BarrioFilter.vue'
import CafeList from './CafeList.vue'


export default {
  name: 'Home',
  components: {CafeList, BarrioFilter},
  
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
    ...mapGetters('cafes',['cafeCount'])
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
.big-container{
  display: inline-flex;
  border: 0px red solid;
}
.left-side{
  width: 50vw;
  padding: 0 5vw 0 20vw;
  border: 0px rgb(0, 64, 255) solid;
}

</style>
