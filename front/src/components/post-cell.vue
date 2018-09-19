<template>
  <div class="post-cell">
    <el-container>
      <el-header v-bind:height="height">
        <div class="pic"><a href=""><img v-bind:src="post.avatar" alt="" width="16px" height="16px"
                                         style="opacity:0.75;margin-right: 6px"></a><a
          href="" style="color: #aaa;font-size:13px;vertical-align:top">{{ post.username}}</a></div>
      </el-header>
      <el-container>
        <el-main>
          <div style="margin-bottom: 10px">
            <router-link :to="{name:'post',params:{id:post.id}}">{{ post.title }}</router-link>
          </div>
          <div>{{ msg(post.body).slice(0,100)}}...</div>
        </el-main>

        <el-aside width="100px">
          <router-link :to="{name:'post',params:{id:post.id}}"><img id='thumbnail' v-bind:src="post.cover_image"
                                                                    alt=""></router-link>
        </el-aside>
      </el-container>
      <div class="post-info"><i class="el-icon-favor" @click="changeFavor" :style="{color: color}"> </i><span>{{ favor_count }}喜欢</span><i
        class="el-icon-comment"></i><span>{{ post.comments_count }}评论</span></div>

    </el-container>
  </div>
</template>

<script>
  import api from '@/api';
  import store from '@/store/store'

  export default {
    name: "post-cell",

    props: ['post'],
    data() {
      return {
        height: '30',
        color: '',
        favor_count: Number.parseInt(this.post.favor_users_count)
      }
    },
    mounted() {

      api.user.isFavorPost(store.state.userID, this.post.id).then(res => {
        if (res.favor) {
          this.color = 'red'
        }
      })
    },
    methods: {
      changeFavor() {
        if (this.color === 'red') {
          this.color = ''
          this.favor_count -= 1
          api.user.cancelFavorPost(store.state.userID, this.post.id).then(res => {
          })
        } else {
          this.color = 'red'
          this.favor_count += 1
          api.user.addFavorPost(store.state.userID, this.post.id).then(res => {
          })
        }
      }
    },
  }
</script>

<style scoped>
  @import '../assets/icon/iconfont.css';

  .post-cell {
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
