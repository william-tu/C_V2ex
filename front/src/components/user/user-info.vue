<template>
  <div class="user-info">
    <div class="avatar-wrapper">
      <img :src="avatar" alt="" width="140px" height="140px" class="avatar">
    </div>
  </div>
</template>

<script>
  import store from '@/store/store'

  export default {
    name: "user-info",
    data() {
      return {
        avatar: store.state.userAvatar
      }
    }
  }
</script>

<style scoped>
  .user-info {
    width: 1152px;
    height: 300px;
    margin: 0 auto;
  }

  .avatar-wrapper {
    float: left;
    height: 155px;
    width: 148px;

  }

  .avatar {
    position: relative;
    top: 20px;
    border: 4px solid #FFF;
    box-shadow: 0 4px 8px 0 rgba(7, 17, 27, .1);
  }
</style>
