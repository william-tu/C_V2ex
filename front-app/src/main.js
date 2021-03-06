import Vue from 'vue'
import App from './App.vue'
import router from './router/index.js'
import VueMeta from 'vue-meta'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import {Message} from 'element-ui'
import store from './store/store'
import axios from './http'
Vue.config.productionTip = false

Vue.use(ElementUI);
Vue.use(VueMeta);
Vue.prototype.axios = axios;
Vue.prototype.$message = Message;
Vue.prototype.msg = function (msg) {

  return msg.replace(/<[^>]*>/g,'')

};

new Vue({
  el: '#app',
  router,
  store,
  axios,
  render: h => h(App)
}).$mount('#app');
