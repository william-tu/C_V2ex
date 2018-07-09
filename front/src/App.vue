<template>
  <div id="app">

    <navba></navba>
    <div class="main-wrapper">
      <router-view></router-view>
      <div class="main">
        <el-row :gutter="20">
          <el-col :span="18">
            <div class="grid-content ">
              <main-post></main-post>
            </div>
          </el-col>
          <el-col :span="6">
            <div class="grid-content"> oterh </div>
          </el-col>
        </el-row>

      </div>
    </div>
  </div>
</template>

<script>
  import navba from './components/nav/Nav.vue'
  import MainPost from './components/MainPost'


  export default {
    name: 'app',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App',

      }
    },
    metaInfo: {
      meta: [
        { name: "referrer" ,content: "never" }
      ]
    },
    components: {
      'navba': navba,
      'main-post': MainPost,
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
  }

  .main-wrapper {
    margin: 50px 100px;
  }

  .main {
    margin: 10px auto;

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
