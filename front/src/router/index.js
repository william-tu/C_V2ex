import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/components/Login.vue'
import store from '@/store/store'
import types from '@/store/types'
import MainPostLayout from '@/components/layout/MainPostLayout'
import UserInfoLayout from '@/components/layout/UserInfoLayout'
import edit_post from '@/components/edit/edit-post'
import main_info from '@/components/user/main-info'
import user_profile from '@/components/user/user-profile'

Vue.use(VueRouter);


// 页面刷新时，重新赋值token
if (window.localStorage.getItem('token')) {
  store.commit(types.REFRESH, {token: window.localStorage.getItem('token')});
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
    name: 'login',
    component: Login
  },
  {
    path: '/user',
    name: 'user',
    component: UserInfoLayout,
    children: [
      {path: 'info', name: 'user-info', component: main_info},
      {path: 'profile', name: 'user-profile', component: user_profile}
    ]
  },
  {
    path: '/edit',
    name: 'edit',
    component: edit_post
  }


];

const router = new VueRouter({
  mode: 'history',
  routes
});

export default router
