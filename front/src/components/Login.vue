<template>
  <div class="login">
    <el-form ref="form" :rules="rules" :model="form" label-width="80px">
      <el-form-item label="email" prop="email">
        <el-input v-model="form.email" prop="email"></el-input>
      </el-form-item>
      <el-form-item label="验证码" prop="verifyCode">
        <el-input v-model="form.verifyCode">
          <el-button slot="append" @click="sendCode" :disabled="form.isSendCode">{{form.remainTime || '发送验证码'}}
          </el-button>
        </el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit('form')">登录</el-button>
      </el-form-item>
    </el-form>


  </div>
</template>

<script>
  import types from '@/store/types'
  import store from '@/store/store'

  export default {
    name: "Login",
    data() {
      return {
        form: {
          email: '',
          verifyCode: '',
          remainTime: 0,
          isSendCode: false,
        },
        rules: {
          email: [
            {type: 'email', required: true, message: '请输入正确格式的邮箱', trigger: 'blur'}
          ],
          verifyCode: [
            {required: true, message: '请输入验证码', trigger: 'blur'}
          ]
        }
      }
    },
    methods: {
      onSubmit(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            console.log("submit");
            store.commit(types.LOGIN, {emailOrToken: this.form.email, password: this.form.verifyCode});
            this.axios({
              method: 'get',
              url: '/token',
            }).then((res) => {
              store.commit(types.LOGIN,{emailOrtoken: res.data.token});
              this.$router.push({
                path: this.$route.query.redirect || '/'

              });
            }).catch((error) => {
              if (error.response) {
                console.log(error.response);
                this.$message({
                  showClose: true,
                  message: '账号密码错误' + error.response.data.message,
                  type: 'error'
                });
              }
            })
          } else {
            this.$message.error("表单填写不正确，请检查");
            return false
          }
        })

      },
      sendCode() {
        let formError = false;
        this.$refs.form.validateField("email",(error) => {
          if (error) {
            this.$message.error(error);
            formError = true;
          }
        });
        if (formError){
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
          this.$message.error("发送验证码失败"+error.message);
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
