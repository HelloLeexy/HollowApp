import { createStore } from 'vuex';
export default createStore({
  state: {
    sidebarVisible: false,
    sidebarUnfoldable: false,
    theme: 'light',
    userID: null, 
    imagePaths: ['@/assets/images/1.png', 
                  '@/assets/images/2.png', 
                  '@/assets/images/3.png',
                  '@/assets/images/4.png',
                  '@/assets/images/5.png',
                  '@/assets/images/6.png',
                  '@/assets/images/7.png',
                  '@/assets/images/8.png',
                  '@/assets/images/9.png',
                ],

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
    getImagePaths: state => state.imagePaths,
  },
  actions: {

    //

  },
  modules: {},
});