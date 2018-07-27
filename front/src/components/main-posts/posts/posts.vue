<template>
  <div class="posts">
    <div class="cell" v-for="post in posts">
      <el-container>
        <el-header v-bind:height="height">
          <div class="pic"><a href=""><img v-bind:src="post.avatar" alt="" width="16px" height="16px"
                                           style="opacity:0.75;margin-right: 6px"></a><a
            href="" style="color: #aaa;font-size:13px;vertical-align:top">{{ post.username}}</a></div>
        </el-header>
        <el-container>
          <el-main>
            <div style="margin-bottom: 10px"><a href="">{{ post.title }}</a></div>
            <div>{{ msg(post.body).slice(0,100)}}...</div>
          </el-main>

          <el-aside width="100px"><a href=""><img id='thumbnail' v-bind:src="post.cover_image" alt=""></a>
          </el-aside>
        </el-container>
      </el-container>
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
        posts: '',
        currentPage: 1,
        totalPage: 1,
        height: '30'

      }
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
              this.$set(post, 'cover_image', 'http://cdnq.duitang.com/uploads/blog/201407/18/20140718094627_uNCK2.thumb.700_0.jpeg')

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
  .cell {
    padding: 10px;
    text-align: left;
    background-color: white;
    margin-top: 30px;

  }

  #thumbnail {
    height: 100px;
    width: 100px;
    background-size: cover;
    display: block;
  }

  .el-main {
    padding: 0 40px;
  }

  .el-header {
    padding-left: 40px;
    padding-bottom: 10px;
  }

  .pic {
    line-height: 16px;
  }
</style>
