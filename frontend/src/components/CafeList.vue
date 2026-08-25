

<template>
  <div class="cafe-list">

    <v-card v-for="cafe in filteredCafes" :key="cafe.id" class="cafe-card">
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
import { mapState } from 'vuex'

export default {
  name: 'CafeList',

  created () {
    this.$store.dispatch('cafes/fetchCafes')
  },

  methods: {
    randomImage (id) {
      return `https://picsum.photos/seed/${id}/300/200`
    },
  },

  computed: {
    ...mapState('cafes', ['cafes']),
    selectedBarrio () {
      return this.$store.state.barrios.selectedBarrio;
    },
    filteredCafes () {
      if (!this.selectedBarrio) return this.cafes;
      return this.cafes.filter(cafe => cafe.barrio?.id === this.selectedBarrio);
    },
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
