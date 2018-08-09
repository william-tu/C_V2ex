<template>
  <div class="single-post-layout">
    <post :id="id"></post>
  </div>
</template>

<script>
  import post from '@/components/post/post'

  export default {
    name: "SinglePostLayout",
    props: ['id'],
    components:{
      post
    }
  }
</script>

<style scoped>
  .single-post-layout{
    min-width: 1050px;
    margin: 50px 100px;
  }
</style>
