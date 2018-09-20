import axios from './http'

export function fetch(method = 'get', url, params) {
  return new Promise((resolve, reject) => {
    axios[method](url, params)
      .then(response => {
        resolve(response.data);
      }, err => {
        reject(err);
      })
      .catch((error) => {
        reject(error)
      })
  })
}

export default {
  qiniu: {
    uploadToken: '/qiniu-auth/token',
    uploadUrl: 'http://upload-z2.qiniup.com/',
    loadDomain: 'http://pbuf1enju.bkt.clouddn.com/'
  },
  user: {
    updateInfo: '/current-user/info',
    isFavorPost(userId, postId) {
      return fetch('get', '/users/' + userId + '/favor/posts/' + postId)
    },
    addFavorPost(userId, postId) {
      return fetch('post', '/users/' + userId + '/favor/posts/' + postId)
    },
    cancelFavorPost(userId, postId) {
      return fetch('delete', '/users/' + userId + '/favor/posts/' + postId)

    },
    isFavorArticle(userId, postId) {
      return fetch('get', '/users/' + userId + '/favor/articles/' + postId)
    },
    addFavorArticle(userId, postId) {
      return fetch('post', '/users/' + userId + '/favor/articles/' + postId)
    },
    cancelFavorArticle(userId, postId) {
      return fetch('delete', '/users/' + userId + '/favor/articles/' + postId)

    },
    login() {
      return fetch('get', '/token')
    }
  },
  posts: '/posts',


}
