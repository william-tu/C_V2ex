<template>
  <div class="posts">
    <div class="cell" v-for="post in posts">
      <table width="100%">
        <tbody>
        <tr>
          <td style="width: 100px;height: 100px"><a target="_blank" v-bind:href="post.message_url"><img
            v-bind:src="post.avatar" alt=""
            style="width: 100px;height: 100px"></a></td>
          <td>
            <div class="content" style="padding-left: 10px;text-align: left">
              <div class="title"><a target="_blank" v-bind:href="post.message_url">{{ post.title }}</a></div>
              <p>{{ post.body.slice(0,50) }}</p></div>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
    <br>
    <el-pagination
      background
      layout="prev, pager, next"
      @current-change="handlePageChange"
      :current-page="currentPage"
      :total="totalPage">
    </el-pagination>
  </div>
</template>

<script>
  import api from '@/api'

  export default {
    name: "posts",
    data() {
      return {
        posts: [],
        currentPage: 1,
        totalPage: 1,
      }
    },
    mounted: function () {
      this.axios.get(api.posts).then((res) => {
        this.posts = res.data['data'];
        this.totalPage = res.data['pages'] * 10;
        console.log(this.posts)
        for (let post of this.posts) {
          this.axios.get(post.author).then(res => {
            post.avatar = res.data.avatar;
          })
        }
        console.log(this.posts)
      }).catch((error) => {
          console.log(error)
        }
      )
    },
    methods: {
      handlePageChange(val) {
        this.currentPage = val;
        this.axios.get(api.posts, {
          params: {
            page: this.currentPage,
          }
        }).then((res) => {
          this.posts = res.data['data']

        }).catch((error) => {
            console.log(error)
          }
        )
        ;
      }
    }
  }
</script>

<style scoped>
  .cell {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #e2e2e2;
    background-color: white;

  }
</style>
