<template>
  <div class="EditLayout">
    <EditPost @titleChanged="changeTitle" @bodyChanged="changeBody"></EditPost>

    <EditPostPreview :title="title" :body="body"></EditPostPreview>

  </div>
</template>

<script>
  import EditPost from './EditPost'
  import EditPostPreview from './EditPostPreview'

  export default {
    name: "EditLayout",
    components: {
      EditPost,
      EditPostPreview
    },
    data() {
      return {
        title: '',
        body: '',
      }
    },
    methods: {
      changeTitle(val) {
        this.title = val
      },
      changeBody(val) {
        this.body = val
      }
    }
  }
</script>

<style scoped>
  .EditLayout {
    padding: 100px 100px;
  }
</style>
