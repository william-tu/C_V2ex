<template>
  <div class="post-layout">
    <post :id="id"></post>
  </div>
</template>

<script>
  import post from '@/components/post/Post'

  export default {
    name: "PostLayout",
    props: ['id'],
    components:{
      post
    }
  }
</script>

<style scoped>
  .post-layout{
    min-width: 1050px;
    margin: 50px 100px;
  }
</style>
