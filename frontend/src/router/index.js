/**
 * router/index.js
 *
 * Automatic routes for ./src/pages/*.vue
 */

// Composables
import { createRouter, createWebHistory } from 'vue-router'
import About from '@/components/About.vue'
import Contact from '@/components/Contact.vue'
import DefaultLayout from '../layouts/DefaultLayout.vue'
import Home from '../components/Home.vue'
import Historyofcoffee from '../components/Historyofcoffee.vue'

const routes = [
  {
    path: '/',
    component: DefaultLayout,
    children: [
      {path: '', component: Home,  beforeEnter: (to,from) => {
          console.log("Welcome Zhen Cai")
        }},
      {path: 'about', component: About,
        beforeEnter: (to,from) => {
          console.log("Welcome Dhruv Kumar")
        }},
      {path: 'contact', component: Contact,
        beforeEnter: (to,from) => {
          console.log("Welcome Adam Blake")
        }},
      {path: 'historyofcoffee', component : Historyofcoffee,
        beforeEnter: (to,from) => {
          console.log("Welcome Dog")
        }},
         {path: 'about', component : About,
        beforeEnter: (to,from, next) => {
          console.log("Welcome Dog")
        }},
    ]
  }
]


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router