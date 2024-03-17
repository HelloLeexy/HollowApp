import { createStore } from 'vuex';

export default createStore({
  state: {
    sidebarVisible: false,
    sidebarUnfoldable: false,
    theme: 'light',
    userID: null, // 新添加的 userID
  },
  mutations: {
    toggleSidebar(state) {
      state.sidebarVisible = !state.sidebarVisible;
    },
    toggleUnfoldable(state) {
      state.sidebarUnfoldable = !state.sidebarUnfoldable;
    },
    updateSidebarVisible(state, payload) {
      state.sidebarVisible = payload.value;
    },
    setUserID(state, userID) {
      state.userID = userID;
    },
  },
  getters: {
    getUserID: state => state.userID,
  },
  actions: {},
  modules: {},
});
