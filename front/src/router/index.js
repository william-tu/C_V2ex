import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../App.vue'
import HelloWord from '../components/HelloWorld.vue'
import Login from '../components/Login.vue'

Vue.use(VueRouter);

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
      name: 'login',
      component: Login
    }


];

const router = new VueRouter({
  mode: 'history',
  routes
});

export default router
