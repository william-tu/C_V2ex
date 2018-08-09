<template>
  <div class="main">
    <el-row :gutter="20">
      <el-col :span="18">
        <div class="grid-content ">
          <main-post></main-post>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content"> oterh</div>
      </el-col>
    </el-row>

  </div>
</template>

<script>
  import MainPost from './MainPost'

  export default {
    name: "MainPostLayout",
    components: {
      'main-post': MainPost,
    }
  }
</script>

<style scoped>
  .main{
     margin: 50px 100px;
  }
</style>
