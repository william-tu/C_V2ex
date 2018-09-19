<template>
  <div class="main-post">
    <el-tabs v-model="activeName" @tab-click="handleClick" type="border-card">
      <el-tab-pane label="用户管理" name="first">
        <articles></articles>
      </el-tab-pane>
      <el-tab-pane label="文章" name="second"><posts></posts></el-tab-pane>
      <el-tab-pane label="角色管理" name="third">角色管理</el-tab-pane>
      <el-tab-pane label="定时任务补偿" name="fourth">定时任务补偿</el-tab-pane>
    </el-tabs>

  </div>
</template>

<script>
  import articles from './tabs/articles'
  import posts from './tabs/posts'

  export default {
    name: "MainPost",
    data() {
      return {
        activeName: 'first',

      };
    },
    components: {
      'articles': articles,
      posts
    },
    methods: {
      handleClick(tab, event) {

        console.log(tab, event);
      },

    }
  }
</script>

<style >
  .main-post {
    background-color: white;
  }




</style>
