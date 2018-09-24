<template>
  <div class="post-preview">
    <h1>{{ title }}</h1>
    <p v-html="body"></p>
  </div>
</template>

<script>
  export default {
    name: "post-preview",
    props: ['title', 'body']
  }
</script>

<style scoped>
  .post-preview {
    padding: 10px 40px;
    background-color: white;
    text-align: left;
    overflow: hidden;
  }
</style>
