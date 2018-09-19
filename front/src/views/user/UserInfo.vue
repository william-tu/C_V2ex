<template>
  <div class="UserInfo">
    <div class="avatar-wrapper">
      <el-upload
        class="avatar-uploader"
        action="http://upload-z2.qiniup.com"
        :data="qiniu"
        :show-file-list="false"
        :on-success="handleAvatarSuccess"
        :before-upload="beforeAvatarUpload" v-loading="loading">
        <el-tooltip class="item" effect="dark" content="更改头像" placement="bottom">
          <img :src="avatar" width="140px" height="140px" class="avatar"   >
        </el-tooltip>
      </el-upload>
    </div>
    <div class="user-info-right">
      <div class="user-name">{{ username }}
        <p style="margin-top: 0px;text-align: left">
          <router-link :to="{name:'user-profile'}" style="font-size: initial;"><i class="el-icon-edit"></i>编辑
          </router-link>
        </p>
      </div>
      <div class="other-info">

      </div>
    </div>
  </div>
</template>

<script>
  import store from '@/store/store'
  import api from '@/api'
  import types from "../../store/types";

  export default {
    name: "UserInfo",
    data() {
      return {
        avatar: store.state.userAvatar,
        username: store.state.username,
        qiniu: {
          token: '',
        },
        loading: false
      }
    },
    computed: {
      getAvatar() {
        return store.state.userAvatar
      },
      getUsername() {
        return store.state.username
      }
    },
    watch: {
      getAvatar(val) {
        this.avatar = val
      },
      getUsername(val) {
        this.username = val
      }
    },
    mounted() {
      this.axios.get(api.qiniu.uploadToken).then((res) => {
        this.qiniu.token = res.data.token
      }).catch((error) => {
        this.$message.error(error);
      })
    },
    methods: {
      handleAvatarSuccess(res, file) {
        console.log(res);
        store.commit(types.UPDATE,{userAvatar:api.qiniu.loadDomain + res.key });
        this.axios.put(api.user.updateInfo, {avatar: store.state.userAvatar}).then((res) => {
          console.log(res)
        })
        this.loading = false;

      },
      beforeAvatarUpload(file) {
        this.loading = true;

        const isLt2M = file.size / 1024 / 1024 < 2;
        console.log(file);
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!');
        }
        return isLt2M;
      }
    }
  }
</script>

<style scoped>
  .UserInfo {
    width: 1152px;
    height: 300px;
    margin: 0 auto;
  }

  .avatar-wrapper {
    float: left;
    height: 155px;
    width: 148px;

  }

  .avatar {
    position: relative;
    top: 20px;
    border: 4px solid #FFF;
    box-shadow: 0 4px 8px 0 rgba(7, 17, 27, .1);
  }

  .user-info-right {
    float: right;
    width: 980px;
  }

  .user-name {
    float: left;
    margin-top: 48px;
    font-weight: 600;
    font-size: 24px;
    line-height: 28px;
    color: slategray;

  }

</style>
