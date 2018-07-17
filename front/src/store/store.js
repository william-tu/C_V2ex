import Vue from 'vue'
import Vuex from 'vuex'
import types from './types.js'

Vue.use(Vuex);

export default new Vuex.Store({

  state: {
    token: null,
    userID: null,
    username: null,
    userAvatar: null,
  },
  mutations: {
    [types.LOGIN]: (state, payload) => {
      if (payload.password) {
        state.token = payload.emailOrToken + ':' + payload.password
      } else {
        state.token = payload.emailOrToken + ':'
      }
      localStorage.token = state.token
    },
    [types.REFRESH]: (state, payload) => {
      state.token = payload.token


    },
    [types.setUserInfo]: (state, userInfo) => {
      state.userID = userInfo.id;
      state.username = userInfo.username;
      state.userAvatar = userInfo.avatar;
      localStorage.userID = state.userID;
      localStorage.username = state.username;
      localStorage.userAvatar = state.userAvatar;
    },
    [types.LOGOUT]: (state) => {
      console.log(state.token)
      localStorage.removeItem('token');
      localStorage.removeItem('userID');
      localStorage.removeItem('username');
      localStorage.removeItem('userAvatar');
      state.token = null;
      state.userID = null;
      state.username = null;
      state.userAvatar = null;
    },
    [types.UPDATE]: (state,payload) => {
      for (let p in payload){
        state[p] = payload[p];
        localStorage[p] = payload[p]
      }


    }


  },


})
