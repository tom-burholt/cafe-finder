import CafeApi from '../../api/CafeApi';

const baseState = () => ({
  cafes: [],
  loading: false,
});

const getters = {
  cafeCount (state) {
    return state.cafes.length;
  },
};

const mutations = {
  SET_CAFES (state, cafes) {
    state.cafes = cafes;
  },
  ADD_CAFE (state, cafe) {
    state.cafes.push(cafe);
  },
  REMOVE_CAFE (state, id) {
    state.cafes = state.cafes.filter(cafe => cafe.id !== id);
  },
};

const actions = {
  async fetchCafes ({ commit }) {
    const data = await CafeApi.fetchCafes();
    // commit('SET_CAFES', data.map(cafe => ({
    //   id: cafe.id,
    //   cafeName: cafe.name,
    //   barrio: cafe.barrio.name,
    //   address: cafe.address,
    //   tags: cafe.tags,
    // })));
    commit('SET_CAFES', data);
  },
};

export default {
  state: baseState(),
  getters,
  mutations,
  actions,
  namespaced: true,
};