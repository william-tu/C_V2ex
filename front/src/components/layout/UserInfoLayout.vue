<template>
  <div class="UserInfoLayout">
    <user-info-nav></user-info-nav>
    <div class="main-info-wrapper">
      <router-view></router-view>
    </div>

  </div>
</template>

<script>
  import UserInfoNav from '@/components/nav/UserInfoNav'

  export default {
    name: "UserInfoLayout",
    components: {
      "user-info-nav": UserInfoNav,
    }

  }
</script>

<style scoped>


  .main-info-wrapper {
    background-color: white;
    padding: 90px 50px;

  }

</style>
