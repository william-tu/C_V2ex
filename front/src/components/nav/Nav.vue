<template>
  <div class="header">
    <el-container>
      <el-aside width="200px">
        <el-main>
          <router-link :to="{ path: '/'}"><img src="@/assets/logo.png" width="60px" height="60px"></router-link>
        </el-main>
      </el-aside>
      <el-main>


        <el-menu :default-active="activeIndex" class="el-menu-demo nav" mode="horizontal" @select="handleSelect">
          <el-menu-item index="1">处理中心</el-menu-item>

          <template v-if="isLogin">
            <el-submenu index="2">
              <template slot="title"><span>{{ username }}</span>&nbsp;&nbsp;<img v-bind:src="avatar" width="20px" height="20px" alt="" class="avatar"></template>
              <el-menu-item index="2-1"><router-link :to="{ name: 'user-info'}">个人资料</router-link></el-menu-item>
              <el-menu-item index="2-2">选项2</el-menu-item>
              <el-menu-item index="2-3"><a @click="logout">注销</a>
              </el-menu-item>
            </el-submenu>
          </template>
          <template v-else>
            <el-menu-item index="2">
              <router-link :to="{ name: 'login'}">

                <el-button type="primary" round>登录</el-button>
              </router-link>
            </el-menu-item>
          </template>
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
        isLogin: store.state.token,
        avatar: store.state.userAvatar,
        username: store.state.username,
      }
    },
    computed: {
      getLoginStatus() {
        return this.$store.state.token
      },
      getAvatar() {
        return store.state.userAvatar
      },
      getUsername(){
        return store.state.username
      }
    },
    watch: {
      getLoginStatus(val) {
        this.isLogin = val;
      },
      getAvatar(val) {
        this.avatar = val;
      },
      getUsername(val) {
        this.username = val;
      }
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      },
      logout() {
        store.commit(types.LOGOUT);

      }
    }
  }
</script>

<style scoped>
  .header {
    height: 80px;
    background-color: white;
  }

  h1 {
    float: left;
  }

  .nav {
    border-bottom: solid 1px white !important;
    float: right;

  }
</style>
