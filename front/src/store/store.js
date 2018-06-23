import Vue from 'vue'
import Vuex from 'vuex'
import types from './types.js'
import { Base64 } from 'js-base64'

Vue.use(Vuex);

export default new Vuex.Store({

  state: {
    token: null,
  },
  mutations: {
    [types.LOGIN]: (state, payload) => {
      state.token = 'Basic ' + Base64.encode(payload.emailOrToken + ':' + payload.password);
      localStorage.token = state.token
    },
    [types.LOGOUT]: (state) => {
      localStorage.removeItem('token');
      state.token = null;
      state.isLogin = false
    },

  },


})
