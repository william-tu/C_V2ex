<template>
  <div class="EditPostPreview">
    <div style="text-align: center;color: rgb(170, 170, 170); font-size: 13px;">预览</div>
    <h1>{{ title }}</h1>
    <p v-html="body"></p>

  </div>
</template>

<script>
  export default {
    name: "EditPostPreview",
    props:['title','body']
  }
</script>

<style scoped>
  .EditPostPreview {
    margin-top: 50px;
    padding: 10px 40px;
    background-color: white;
    text-align: left;

  }
</style>
