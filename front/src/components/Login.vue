<template>
  <div class="login">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="email">
        <el-input v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item label="验证码">
        <el-input v-model="form.verifyCode">
          <el-button slot="append" @click="sendCode" :disabled="form.isSendCode">{{form.remainTime || '发送验证码'}}
          </el-button>
        </el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">登录</el-button>
      </el-form-item>
    </el-form>


  </div>
</template>

<script>
  export default {
    name: "Login",
    data() {
      return {
        form: {
          email: '',
          verifyCode: '',
          remainTime: 0,
          isSendCode: false,
        }
      }
    },
    methods: {
      onSubmit() {
        console.log('submit!');
      },
      sendCode() {
        if (!this.form.email){
          this.$message.error("email不能为空");
          return ;
        }
        this.axios({
            method: 'post',
            url: '/verifyCode',
            data: {
              email: this.form.email
            },

          }
        ).then((res) => {
          this.$message.success("发送邮件成功");
        }).catch((error) => {
          this.$message.error(error.message);
        });
        this.form.isSendCode = true;
        this.form.remainTime = 60;
        let inter = window.setInterval(
          () => {
            if ((this.form.remainTime--) <= 0) {
              this.form.isSendCode = false;
              this.form.remainTime = 0;
              window.clearInterval(inter);
            }
          }, 1000)

      }
    }
  }
</script>

<style scoped>
  .login {
    width: 40%;
    margin: 10px auto;
  }
</style>
