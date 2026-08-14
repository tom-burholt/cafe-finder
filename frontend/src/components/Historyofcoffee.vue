<template>
  <div class="era-list">
    <h1>History of Coffee</h1>

    <v-card class="era-card">
      <v-card-title>1700 - 1800</v-card-title>
      <v-card-text>Probably had coffee. Dont think starbucks was around in this time. Just Yerba Mate.</v-card-text>
    </v-card>

    <v-card class="era-card">
      <v-card-title>1800 - 1900</v-card-title>
      <v-card-text>Costa Coffee hit the UK highstreet for the first time in 1801, including wifi and free use.</v-card-text>
    </v-card>

    <v-card class="era-card">
      <v-card-title>1900 - 2000</v-card-title>
      <v-card-text>Now we`re talking, Starbucks is the epitome of late stage capitalism. There`s nothing I like more double frap frap caramel double mochinos.</v-card-text>
    </v-card>
  </div>
</template>

<style scoped>
.era-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  padding: 16px;
}
.era-card {
  width: 300px;
  padding: 10px;
}
</style>
