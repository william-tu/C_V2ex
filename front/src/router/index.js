import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '@/App.vue'
import HelloWord from '@/components/HelloWorld.vue'
import Login from '@/components/Login.vue'
import store from '@/store/store'
import types from '@/store/types'

Vue.use(VueRouter);


// 页面刷新时，重新赋值token
if (window.localStorage.getItem('token')) {
  store.commit(types.LOGIN, {emailOrToken: window.localStorage.getItem('token')})
};

const routes = [
    {
      path: '/ss',
      name: '/',
      component: Index
    },
    {
      path: "/hello",
      name: 'hello',
      component: HelloWord
    },
    {
      path: '/login',
      name: types.LOGIN,
      component: Login
    }


];

const router = new VueRouter({
  mode: 'history',
  routes
});

export default router
