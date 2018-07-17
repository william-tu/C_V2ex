<template>
  <div class="user-profile">

    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="用户名">
        <el-input v-model="form.username"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">修改</el-button>
      </el-form-item>
    </el-form>


  </div>
</template>

<script>
  import store from '@/store/store'

  export default {
    name: "user-profile",
    data() {
      return {
        form: {
          username: store.state.username,
        },
      }
    },
    methods:{
      onSubmit(){
        console.log(this.form.username)
      },

    }

  }
</script>

<style scoped>
  .user-profile {
    padding: 50px 200px;
  }

  .el-form {
    width: 460px;
  }

  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }

  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }

  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }

  .avatar {
    width: 100px;
    height: 100px;
    display: block;
  }

</style>
