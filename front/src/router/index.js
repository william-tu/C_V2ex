import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/components/Login.vue'
import store from '@/store/store'
import types from '@/store/types'
import MainPostLayout from '@/components/layout/MainPostLayout'
import UserInfoLayout from '@/components/layout/UserInfoLayout'

Vue.use(VueRouter);


// 页面刷新时，重新赋值token
if (window.localStorage.getItem('token')) {
  store.commit(types.LOGIN, {emailOrToken: window.localStorage.getItem('token')});
  store.commit(types.setUserInfo, {
    id: window.localStorage.getItem('userID'),
    avatar: window.localStorage.getItem('userAvatar'),
    username: window.localStorage.getItem('username')
  })
}

const routes = [
  {
    path: '/',
    name: '/',
    component: MainPostLayout
  },
  {
    path: '/login',
    name: types.LOGIN,
    component: Login
  },
  {
    path: '/user-info',
    name: 'user-info',
    component: UserInfoLayout,
  }


];

const router = new VueRouter({
  mode: 'history',
  routes
});

export default router
