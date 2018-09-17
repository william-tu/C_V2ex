<template>
  <div class="Post">
    <h1>{{ post.title }}</h1>
    <p v-html="post.body"></p>
  </div>
</template>

<script>
  import api from '@/api'

  export default {
    name: "Post",
    props: ['id'],
    data() {
      return {
        post: ''
      }
    },
    mounted() {
      this.axios.get(api.posts + '/' + this.id).then((res) => {
          this.post = res.data;
        }
      ).catch((error) => {
          console.log(error)
        }
      )
    }
  }
</script>

<style scoped>
  .Post {
    background-color: white;
    padding: 10px 40px;
    text-align: left;
    overflow: hidden;

  }

</style>
