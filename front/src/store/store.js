import Vue from 'vue'
import Vuex from 'vuex'
import types from './types.js'
import { Base64 } from 'js-base64'

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
      state.token = 'Basic ' + Base64.encode(payload.emailOrToken + ':' + payload.password);
      localStorage.token = state.token
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
      localStorage.removeItem('token');
      localStorage.removeItem('userID');
      localStorage.removeItem('username');
      localStorage.removeItem('userAvatar');
      state.token = null;
      state.userID = null;
      state.username = null;
      state.userAvatar = null;
    },

  },


})
