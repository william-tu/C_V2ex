<template>
  <div class="article-cell">
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
      <div class="post-info"><i class="el-icon-favor" @click="changeFavor" :style="{color: color}"> </i><span>{{ favor_count }}喜欢</span>
      </div>
    </el-container>
  </div>
</template>

<script>
  import api from '@/api';
  import store from '@/store/store'

  export default {
    name: "article-cell",
    props: ['post'],
    data() {
      return {
        height: '30',
        color: '',
        favor_count: Number.parseInt(this.post.favor_users_count)

      }
    },
    mounted() {
      if (store.state.userID) {
        api.user.isFavorArticle(store.state.userID, this.post.id).then(res => {
          if (res.favor) {
            this.color = 'red'
          }
        })
      }
    },
    methods: {
      changeFavor() {
        if (store.state.userID) {
          console.log(11231)
          if (this.color === 'red') {
            this.color = ''
            this.favor_count -= 1
            api.user.cancelFavorArticle(store.state.userID, this.post.id).then(res => {
            })
          } else {
            this.color = 'red'
            this.favor_count += 1
            api.user.addFavorArticle(store.state.userID, this.post.id).then(res => {
            })
          }

        } else {
          api.user.login().then(res => {

          })
        }
      }
    },
  }
</script>

<style scoped>
  @import '../assets/icon/iconfont.css';

  .article-cell {
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

  .post-info {
    padding-left: 40px;
    padding-top: 5px;
  }

  i {
    margin-right: 10px;
  }

  span {
    color: rgb(170, 170, 170);
    font-size: 14px;
    vertical-align: text-top;
    margin-right: 20px;
  }
</style>
