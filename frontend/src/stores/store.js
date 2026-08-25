import { createStore } from 'vuex'
import cafes from './modules/cafes'
import barrios from './modules/barrios'

export default createStore({
  modules: {
    cafes,
    barrios
  }
})
