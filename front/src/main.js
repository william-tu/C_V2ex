import Vue from 'vue'
import App from './App.vue'
import router from './router/index.js'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import {Message} from 'element-ui'
import store from './store/store'
import axios from './http'


Vue.use(ElementUI);
Vue.prototype.axios = axios;
Vue.prototype.$message = Message;

new Vue({
  el: '#app',
  router,
  store,
  axios,
  render: h => h(App)
}).$mount('#app');
