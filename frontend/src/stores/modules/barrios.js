import BarrioApi from '../../api/BarrioApi';

const baseState = () => ({
  barrios: [],
  selectedBarrio: null,
  loading: false,
});

const getters = {
  barrioCount (state) {
    return state.barrios.length;
  },
};

const mutations = {
    SET_BARRIOS(state, barrios) {
        state.barrios = barrios
    },
    
    ADD_BARRIO (state, barrios) {
    state.barrios.push(barrios);
    },
    
    REMOVE_BARRIO (state, id) {
    state.barrios = state.barrios.filter(barrios => barrios.id !== id);
    },

    SET_SELECTED_BARRIO (state, barrioId) {
    state.selectedBarrio = barrioId;
    },  
};


const actions = {
  async fetchBarrios ({ commit }) {
    const data = await BarrioApi.fetchBarrios();
    commit('SET_BARRIOS', data);
  },
};

export default {
  state: baseState(),
  getters,
  mutations,
  actions,
  namespaced: true,
};