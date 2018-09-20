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
  import api from '@/api'
  import types from '@/store/types'

  export default {
    name: "user-profile",
    data() {
      return {
        form: {
          username: store.state.username,
        },
      }
    },
    methods: {
      onSubmit() {
        if (store.state.username === this.form.username) {
          this.$message("未修改内容");
          return;
        }
        this.axios.put('/users/'+store.state.userID+'/info', {'username': this.form.username}).then((res) => {
          store.commit(types.UPDATE, {username: this.form.username});
          this.$message({
            message: '修改成功',
            type: 'success'
          });
        })
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



</style>
