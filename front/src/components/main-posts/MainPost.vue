<template>
  <div class="main-post">
    <el-tabs v-model="activeName" @tab-click="handleClick" type="border-card">
      <el-tab-pane label="用户管理" name="first">
        <articles></articles>
      </el-tab-pane>
      <el-tab-pane label="配置管理" name="second">配置管理</el-tab-pane>
      <el-tab-pane label="角色管理" name="third">角色管理</el-tab-pane>
      <el-tab-pane label="定时任务补偿" name="fourth">定时任务补偿</el-tab-pane>
    </el-tabs>

  </div>
</template>

<script>
  import articles from './posts/articles'

  export default {
    name: "MainPost",
    data() {
      return {
        activeName: 'first',

      };
    },
    components: {
      'articles': articles,
    },
    methods: {
      handleClick(tab, event) {

        console.log(tab, event);
      },

    }
  }
</script>

<style>
  .main-post {
    background-color: white;
  }

  a, a:hover {
    color: #37a;
    text-decoration: None;

  }


</style>
