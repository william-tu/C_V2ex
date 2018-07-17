import axios from 'axios'
import store from './store/store'
import types from './store/types'
import router from './router/index'
import {Base64} from 'js-base64'

axios.defaults.timeout = 5000
axios.defaults.baseURL = 'http://127.0.0.1:5000/api/v1.0'

axios.interceptors.request.use(
  config => {
    if (store.state.token) {
      console.log(store.state.token)
      config.headers.common['Authorization'] = 'Basic ' + Base64.encode(store.state.token)
    }
    return config
  },
  err => {
    return Promise.reject(err)
  })

// http response 拦截器
axios.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (error.response) {
      // console.log(error.response)
      switch (error.response.status) {
        case 401:
          console.log(router.currentRoute.name);
          // 401 清除token信息并跳转到登录页面
          store.commit(types.LOGOUT);
          if (router.currentRoute.name === types.LOGIN) {
            return Promise.reject(error)
          }
          router.replace({
            name: 'login',
            query: {redirect: router.currentRoute.fullPath}
          })
      }
    }
    return Promise.reject(error)
  });

export default axios
