<template>
  <div class="UserInfoNav">
    <user-info></user-info>
  </div>
</template>

<script>
  import user_info from './user-info'

  export default {
    name: "UserInfoNav",
    components: {
      "user-info": user_info,

    }
  }
</script>

<style scoped>
  .UserInfoNav {
    padding: 0 0;
    background: url("http://www.zcool.com.cn/community/037b5865937988ca8012193a3acb5e8.jpg") center top repeat;
    height: 120px;
    min-width: 1250px;

  }
</style>
