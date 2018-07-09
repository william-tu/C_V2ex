<template>
  <div class="main-post">
    <el-tabs v-model="activeName" @tab-click="handleClick" type="border-card">
      <el-tab-pane label="用户管理" name="first">
        <div class="cell" v-for="post in posts">
          <table width="100%">
            <tbody>
            <tr>
              <td style="width: 100px;height: 100px"><a href=""><img v-bind:src="post.image_url" alt=""
                                                                     style="width: 100px;height: 100px"></a></td>
              <td>
                <div class="content" style="padding-left: 10px;text-align: left">
                  <div class="title"><a
                    href="">{{ post.title }}</a></div>
                  <p>{{ post.content.slice(0,50) }}</p></div>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </el-tab-pane>
      <el-tab-pane label="配置管理" name="second">配置管理</el-tab-pane>
      <el-tab-pane label="角色管理" name="third">角色管理</el-tab-pane>
      <el-tab-pane label="定时任务补偿" name="fourth">定时任务补偿</el-tab-pane>
    </el-tabs>

  </div>
</template>

<script>

  export default {
    name: "MainPost",
    data() {
      return {
        activeName: 'first',
        posts: '',
      };
    },
    metaInfo: {
      meta: [
        {name: 'referrer', content: 'never'}
      ]
    },
    mounted: function () {
      this.axios.get('/articles').then((res) => {
        this.posts = res.data['data']
      });
    }
    ,
    methods: {
      handleClick(tab, event) {

        console.log(tab, event);
      }
    }
  }
</script>

<style scoped>
  .main-post {
    background-color: white;
  }

  .cell {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #e2e2e2;
    background-color: white;

  }

  a, a:hover {
    color: #37a;
    text-decoration: None;

  }

</style>
