import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios';
import CoreuiVue from '@coreui/vue'
import CIcon from '@coreui/icons-vue'
import { iconsSet as icons } from '@/assets/icons'
import DocsExample from '@/components/DocsExample'
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css'

const app = createApp(App)
app.use(store)
app.use(router)
app.use(CoreuiVue)
app.use(ElementPlus)
app.provide('icons', icons)
app.component('CIcon', CIcon)
app.component('DocsExample', DocsExample)
app.config.globalProperties.$axios = axios;
createApp(App).use(store).mount('#app');
// 添加 beforeCreate 钩子
app.mixin({
  beforeCreate() {
    // 检查用户是否已登录
    const storedUserID = localStorage.getItem('userID');
    if (storedUserID) {
      // 如果已登录，设置 userID 到 Vuex store
      this.$store.commit('setUserID', storedUserID);
    }
  }
});

app.mount('#app')
