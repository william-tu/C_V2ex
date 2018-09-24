<template>
  <div class="user-thumbnail-avatar">
    <router-link to=""><img v-bind:src="avatar" alt="" :width="size" :height="size"
                            style="opacity:0.75;margin-right: 6px"></router-link>
  </div>
</template>

<script>
  export default {
    name: "user-thumbnail-avatar",
    props: {
      userId:{},
      avatar:{},
      size:{
        default:'16px'
      }
    }
  }
</script>

<style scoped>
  .user-thumbnail-avatar {
    display: inline;
  }
</style>
