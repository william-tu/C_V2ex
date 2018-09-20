<template>
  <div class="posts">
    <template v-for="post in posts">
      <post v-bind:post="post"></post>
    </template>
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
  import post from '@/components/post-cell'

  export default {
    name: "posts",
    data() {
      return {
        posts: '',
        currentPage: 1,
        totalPage: 1,
      }
    },
    components: {
      post,
    },
    mounted: function () {
      this.axios.get(api.posts).then((res) => {
          this.posts = res.data['data'];
          this.totalPage = res.data['pages'] * 10;
        }
      ).catch((error) => {
          console.log(error)
        }
      )
    },
    watch: {
      posts(val) {
        for (let post of this.posts) {
          this.axios.get(post.author).then(res => {
            this.$set(post, 'avatar', res.data.avatar)
            this.$set(post, 'username', res.data.username)
            if (!post.cover_image) {
              this.$set(post, 'cover_image', 'http://img.zcool.cn/community/0117e2571b8b246ac72538120dd8a4.jpg@1280w_1l_2o_100sh.jpg')

            }
          })
        }
      }
    }
    ,
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


</style>
