import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/components/Login.vue'
import store from '@/store/store'
import types from '@/store/types'
import MainPostLayout from '@/components/main/MainPostLayout'
import UserInfoLayout from '@/components/user/UserInfoLayout'
import EditLayout from '@/components/edit/EditLayout'
import main_info from '@/components/user/UserOtherInfo'
import user_profile from '@/components/user/UserProfile'
import SinglePostLayout from '@/components/post/PostLayout'

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
    component: EditLayout
  },
  {
    path: '/post/:id',
    name: 'post',
    props: true,
    component: SinglePostLayout

  }


];

const router = new VueRouter({
  routes
});

export default router
