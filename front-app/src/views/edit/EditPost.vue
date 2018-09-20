<template>
  <div class="edit-post">
    <el-form ref="form" :model="form" :rules="rules" label-width="80px">
      <el-form-item label="标题" prop="title">
        <el-input v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item label="正文" prop="body">
        <editor
          useCustomImageHandler
          :editorOptions="editorSettings"
          @imageAdded="handleImageAdded" v-model="form.body"></editor>

      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit('form')">立即创建</el-button>
        <el-button @click="resetForm('form')">清空</el-button>
      </el-form-item>
    </el-form>

  </div>
</template>

<script>


  import api from '@/api'
  import {VueEditor, Quill} from 'vue2-editor'
  import ImageResize from 'quill-image-resize-module'

  Quill.register('modules/imageResize', ImageResize)

  export default {
    name: "edit-post",

    components: {
      'editor': VueEditor
    },

    data() {
      return {
        form: {
          title: '',
          body: ''

        },
        editorSettings: {
          modules: {
            imageResize: {modules: ['Resize', 'DisplaySize', 'Toolbar']}
          }
        },
        qiniu: {
          token: '',
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
    mounted() {
      this.axios.get(api.qiniu.uploadToken).then((res) => {
        this.qiniu.token = res.data.token;
      }).catch((error) => {
        this.$message.error(error);
      });
    },
    methods: {
      onSubmit(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.axios.post(api.posts, {title: this.form.title, body: this.form.body}).then(res => {
              this.$message.success('发表成功')
              this.$router.push({name: 'post', params: {id: res.data.id}})
            }).catch(error => {
              this.$message.error(error)
            })
          } else {
            this.$message.error("请检查表单")
          }

        })

      },
      resetForm(form) {
        this.$refs[form].resetFields();
      },
      handleImageAdded(file, Editor, cursorLocation, resetUploader) {

        let formData = new FormData();
        formData.append('file', file);
        formData.append('token', this.qiniu.token);
        this.axios.post(api.qiniu.uploadUrl, formData).then((res) => {
          let url = api.qiniu.loadDomain + res.data.key;
          Editor.insertEmbed(cursorLocation, 'image', url);
          resetUploader();
        })
      }
    },
    computed: {
      getTitle() {
        return this.form.title
      },
      getBody() {
        return this.form.body
      }
    },
    watch: {
      getTitle(val) {
        this.$emit('titleChanged', val)
      },
      getBody(val) {
        this.$emit('bodyChanged', val)
      }
    }

  }
</script>

<style scoped>
  .edit-post {
    background-color: white;
    padding: 50px 50px;
    border: 1px solid #dcdfe6;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, .12), 0 0 6px 0 rgba(0, 0, 0, .04);
  }
</style>
