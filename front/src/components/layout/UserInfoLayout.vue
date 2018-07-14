<template>
  <div class="UserInfoLayout">
    <div class="header-info">
      <user-info></user-info>
    </div>
    <div class="main-info-wrapper">
      <main-info></main-info>
    </div>

  </div>
</template>

<script>
  import user_info from '@/components/user/user-info'
  import main_info from '@/components/user/main-info'
  export default {
    name: "UserInfoLayout",
    components: {
      "user-info": user_info,
      "main-info": main_info
    }

  }
</script>

<style scoped>
  .header-info {
    padding: 0 0;
    background: url("http://www.zcool.com.cn/community/037b5865937988ca8012193a3acb5e8.jpg") center top no-repeat;
    height: 120px;

  }



  .main-info-wrapper {
    background-color: white;
    padding: 90px 50px;
  }

</style>
