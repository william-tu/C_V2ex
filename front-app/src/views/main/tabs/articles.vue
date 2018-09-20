<template>
  <div class="articles">
    <template v-for="post in posts">
      <article_cell :post="post"></article_cell>
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
  import article_cell from '@/components/article-cell'

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
    components: {
      article_cell,
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
          if (post.content.startsWith('http')) {
            this.$set(post, 'content', '[图片]')
          }
          if (!post.image_url) {
            this.$set(post, 'image_url', 'http://img.zcool.cn/community/0117e2571b8b246ac72538120dd8a4.jpg@1280w_1l_2o_100sh.jpg')

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



</style>
