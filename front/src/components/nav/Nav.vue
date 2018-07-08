<template>
  <div class="header">
    <el-container>
      <el-aside width="200px">
        <el-main>
          <router-link :to="{ path: '/'}"><img src="../../assets/logo.png" width="60px" height="60px"></router-link>
        </el-main>
      </el-aside>
      <el-main>


        <el-menu :default-active="activeIndex" class="el-menu-demo nav" mode="horizontal" @select="handleSelect">
          <el-menu-item index="1">处理中心</el-menu-item>
          <el-submenu index="2">
            <template slot="title">我的工作台</template>
            <el-menu-item index="2-1">选项1</el-menu-item>
            <el-menu-item index="2-2">选项2</el-menu-item>
            <el-menu-item index="2-3">选项3</el-menu-item>
            <el-submenu index="2-4">
              <template slot="title">选项4</template>
              <el-menu-item index="2-4-1">选项1</el-menu-item>
              <el-menu-item index="2-4-2">选项2</el-menu-item>
              <el-menu-item index="2-4-3">选项3</el-menu-item>
            </el-submenu>
          </el-submenu>

          <el-menu-item index="3">

              <el-button type="primary" round v-if="isLogin" @click="logout">注销</el-button>

            <router-link :to="{ name: 'login'}" v-else>
              <el-button type="primary" round>登录</el-button>
            </router-link>
          </el-menu-item>
        </el-menu>
      </el-main>
    </el-container>
  </div>
</template>

<script>
  import types from '@/store/types'
  import store from '@/store/store'

  export default {
    name: "Nav",
    data: function () {
      return {
        activeIndex: '1',
        isLogin: this.$store.state.token
      }
    },
    computed: {
      getLoginStatus(){
        return this.$store.state.token
      }
    },
    watch:{
      getLoginStatus(val){
        this.isLogin = val;
      }
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      },
      logout(){
        store.commit(types.LOGOUT);

      }
    }
  }
</script>

<style scoped>
  .header {
    /*height: 80px;*/
  }

  h1 {
    float: left;
  }

  .nav {
    border-bottom: solid 1px white !important;
    float: right;
  }
</style>
