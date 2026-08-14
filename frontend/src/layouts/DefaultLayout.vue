<template>
  <div class="layout">
    <nav class="page-header d-flex ga-4 pa-4 justify-center">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/historyofcoffee">History of Coffee</router-link>
      <router-link to="/contact">Contact</router-link>
    </nav>

    <!-- Whichever child route matched renders here -->
    <main class="page-content">
      <router-view />
    </main>

    <footer class="page-footer">
      <p>All rights reserved.</p>
    </footer>
  </div>
</template>

<style scoped>
.layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: rgb(38, 38, 38);
}
.page-header {
  background-color: black;
  color: white;
}
.page-header a {
  color: white;
}
.page-content {
  flex: 1;
}
.page-footer {
  padding: 16px;
  text-align: center;
  background-color: black;
  color: white;
}
</style>