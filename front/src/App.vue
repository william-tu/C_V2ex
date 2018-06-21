<template>
  <div id="app">
    <navba></navba>

    <router-view></router-view>

  </div>
</template>

<script>
  import navba from './components/nav/Nav.vue'

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',

    }
  },
  components: {
    'navba': navba
  }
}
</script>

<style lang="scss">
  body{
    margin: 0px;
  }
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
