<template>
<v-select 
        label="Select barrio"
        :items ="barrios"
        item-title="name"
        item-value="id"
        v-model="selectedBarrio"
        clearable>
</v-select>

</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'barrioFilter',

  created () {
    this.$store.dispatch('barrios/fetchBarrios')
  },

  computed: {
    ...mapState('barrios', ['barrios']),
    selectedBarrio: {
      get () {
        return this.$store.state.barrios.selectedBarrio;
      },
      set (value) {
        this.$store.commit('barrios/SET_SELECTED_BARRIO', value);
      },
    },
  },
}
</script>