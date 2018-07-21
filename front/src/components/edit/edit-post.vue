<template>
  <div class="edit-post">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="标题">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="正文">
        <quillEditor v-model="form.body"></quillEditor>

      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  import 'quill/dist/quill.core.css'
  import 'quill/dist/quill.snow.css'
  import 'quill/dist/quill.bubble.css'

  import {quillEditor} from 'vue-quill-editor'

  export default {
    name: "edit-post",
    data() {
      return {
        form: {
          name: '',
          body: ''

        }
      }
    },
    methods: {
      onSubmit() {
        console.log('submit!');
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
