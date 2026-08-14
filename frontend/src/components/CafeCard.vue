<template>
  <v-card class="pa-4 mb-2">
    <v-card-title>{{ cafe.cafeName }}</v-card-title>
    <v-card-subtitle>{{ cafe.barrio }} - {{ cafe.address }}</v-card-subtitle>

    <v-card-text>
      <v-chip-group>
        <v-chip v-for="tag in cafe.tags" :key="tag">{{ tag }}</v-chip>
      </v-chip-group>
    </v-card-text>

    <v-card-actions>
      <v-btn color="error" variant="text" @click="onRemoveClick">Remove</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
  export default {
    name: 'CafeCard',
    props: {
      cafe: { type: Object, required: true },
    },
    emits: ['remove'],
    methods: {
      onRemoveClick () {
        this.$emit('remove', this.cafe.id)
      },
    },
  }
</script>