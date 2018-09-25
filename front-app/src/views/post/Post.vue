<template>
  <div class="Post">
    <div class="user-info" style="overflow: hidden">
      <user-thumbnail-avatar style="float: left" :user-id="1" v-bind:avatar="post.author.avatar"
                             :size="'45px'"></user-thumbnail-avatar>
      <div><span class="username">{{ post.author.username }}</span><br>简介:</div>
    </div>
    <post-preview :title="post.title" :body="post.body"></post-preview>
  </div>
</template>

<script>
  import api from '@/api'
  import postPreview from '@/components/post-preview'
  import userThumbnailAvatar from '@/components/user-thumbnail-avatar'

  export default {
    name: "Post",
    props: ['id'],
    data() {
      return {
        post: {
          author:{
            avatar: '',

          }
        }
      }
    },
    components: {
      'post-preview': postPreview,
      'user-thumbnail-avatar': userThumbnailAvatar
    },
    mounted() {
      this.axios.get(api.posts + '/' + this.id).then((res) => {
          let author = res.data.author;
          this.post = res.data
          this.axios.get(author).then(res => {
            this.$set(this.post, 'author', res.data)
          })
        }
      ).catch((error) => {
          console.log(error)
        }
      )
    }
  }
</script>

<style scoped>
  .user-info {
    margin-bottom: 10px;
    padding: 15px 10px 10px 10px;
    text-align: left;
    background-color: white;
    width: 250px;

  }

  span {
    vertical-align: top;
  }

  .username {
    font-weight: 600;
    color: #444;
  }


</style>
