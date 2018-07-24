<template>
  <div class="edit-post">
    <el-form ref="form" :model="form" :rules="rules" label-width="80px">
      <el-form-item label="标题" prop="title">
        <el-input v-model="form.title" ></el-input>
      </el-form-item>
      <el-form-item label="正文" prop="body">
        <quillEditor v-model="form.body" ></quillEditor>

      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit('form')">立即创建</el-button>
        <el-button @click="resetForm('form')">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  import 'quill/dist/quill.core.css'
  import 'quill/dist/quill.snow.css'
  import 'quill/dist/quill.bubble.css'

  import {quillEditor} from 'vue-quill-editor'
  import api from '@/api'

  export default {
    name: "edit-post",
    data() {
      return {
        form: {
          title: '',
          body: ''

        },
        rules: {
          title: [
            {required: true, message: '请输入标题', trigger: 'blur'}
          ],
          body: [
            {required: true, message: '请输入正文', trigger: 'blur'}
          ],
        }
      }
    },
    methods: {
      onSubmit(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            console.log(valid)
            this.axios.post(api.posts, {title: this.form.title, body: this.form.body}).then(res => {
              this.$message.success('发表成功')
            }).catch(error => {
              this.$message.error(error)
            })
          }else {
            this.$message.error("请检查表单")
          }

        })

      },
      resetForm(form) {
        this.$refs[form].resetFields();
      }
    },
    components: {
      quillEditor
    }

  }
</script>

<style scoped>
  .edit-post {
    background-color: white;
    margin: 40px 100px;
    padding: 50px 50px;
    border: 1px solid #dcdfe6;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, .12), 0 0 6px 0 rgba(0, 0, 0, .04);
  }
</style>
