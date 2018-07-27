<template>
  <div class="articles">
    <div class="cell" v-for="post in posts">
      <el-container>
        <el-header :height="height">
          <div class="pic"><a target="_blank" :href="post.message_url"><img v-bind:src="post.avatar" alt="" width="16px"
                                                                            height="16px"
                                                                            style="opacity:0.75;margin-right: 6px;"></a><a
            href="" style="color: #aaa;font-size:13px;vertical-align:top">{{ post.source_from }}</a></div>
        </el-header>
        <el-container>
          <el-main>
            <div style="margin-bottom: 10px"><a target="_blank" :href="post.message_url">{{ post.title }}</a></div>
            <div v-html="post.content.slice(0,140)">...</div>
          </el-main>

          <el-aside width="100px"><a target="_blank" :href="post.message_url"><img id='thumbnail'
                                                                                   :src="post.image_url"
                                                                                   alt=""></a>
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
  export default {
    name: "articles",
    data() {
      return {
        posts: '',
        currentPage: 1,
        totalPage: 1,
        height: '30'
      }
    },
    mounted: function () {
      this.axios.get('/articles').then((res) => {
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
        let avatar_url;
        for (let post of this.posts) {
          if (post.source_from === '豆瓣') {
            avatar_url = 'https://img3.doubanio.com/favicon.ico'
          } else if (post.source_from === '果壳网') {
            avatar_url = 'https://sslstatic.guokr.com/skin/imgs/4-logo.svg'
          } else if (post.source_from === '知乎日报网') {
            avatar_url = 'http://daily.zhihu.com/img/new_home_v3/top_logo.png'
          }
          if (post.content.startsWith('http')){
            this.$set(post,'content','[图片]')
          }
          if (!post.image_url) {
            this.$set(post, 'image_url', 'http://cdnq.duitang.com/uploads/blog/201407/18/20140718094627_uNCK2.thumb.700_0.jpeg')

          }
          this.$set(post, 'avatar', avatar_url)
        }
      }
    },

    methods: {
      handlePageChange(val) {
        this.currentPage = val;
        this.axios.get('/articles', {
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
    padding-bottom: 10px;
  }

  .el-header {
    padding-left: 40px;
    padding-bottom: 10px;
  }

  .pic {
    line-height: 16px;
  }
</style>
