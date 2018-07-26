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
    data() {
      return {
        msg: 'Welcome to Your Vue.js App',

      }
    },
    metaInfo: {
      meta: [
        {name: 'referrer', content: 'never'}
      ]
    },
    components: {
      'navba': navba,

    }
  }
</script>

<style lang="scss">
  body {
    margin: 0px;
    background-color: #e2e2e2;

  }

  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    min-width: 1250px;
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



  .avatar {
    border-radius: 50%;

  }
</style>
