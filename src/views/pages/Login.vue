<template>
  <div class="login-container">
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form" auto-complete="on" label-position="left">

      <div class="title-container">
        <h3 class="title">Login Form</h3>
      </div>

      <el-form-item prop="username">
        <div class="input-with-icon">
          <div class="icon-wrapper">
            <img src="@/assets/icons/user.png" alt="User Icon" class="scaled-icon">
          </div>
          <div class="el-input__inner">
            <el-input ref="username"
                      v-model="loginForm.username"
                      placeholder="Username"
                      name="username"
                      type="text"
                      tabindex="1"
                      auto-complete="on" />
          </div>
        </div>
      </el-form-item>

      <el-form-item prop="password">
        <div class="input-with-icon">
          <div class="icon-wrapper">
            <img src="@/assets/icons/lock.png" alt="Lock Icon" class="scaled-icon">
          </div>
          <div class="el-input__inner">
            <el-input :key="passwordType"
                      ref="password"
                      v-model="loginForm.password"
                      :type="passwordType"
                      placeholder="Password"
                      name="password"
                      tabindex="2"
                      auto-complete="on"
                      @keyup.enter.native="handleLogin" />
          </div>
          <div class="show-pwd" @click="showPwd">
            <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" class="password-icon" />
          </div>
        </div>
      </el-form-item>

      <el-button :loading="loading" type="primary" style="width:100%;" @click.native.prevent="handleLogin">Login</el-button>
      <el-button style="margin-left: 320px;
                   margin-top:5px;
                   background-color: transparent;
                   border: none; padding: 5px 10px;
                   line-height: 1.5;
                   color: #4A90E2;
                   font-size: 14px; "
                 @click="handleCreateAccount">Create Account</el-button>
    </el-form>
  </div>
</template>

<script>

  export default {
    name: 'Login',
    data() {
      const validateUsername = (rule, value, callback) => {
        if (value.length < 1) {
          callback(new Error('Please enter the correct user name'))
        } else {
          callback()
        }
      }
      const validatePassword = (rule, value, callback) => {
        if (value.length < 6) {
          callback(new Error('The password can not be less than 6 digits'))
        } else {
          callback()
        }
      }
      return {
        loginForm: {
          username: '',
          password: ''
        },
        loginRules: {
          username: [{ required: false, trigger: 'blur', validator: validateUsername }],
          password: [{ required: true, trigger: 'blur', validator: validatePassword }]
        },
        loading: false,
        passwordType: 'password',
        redirect: undefined
      }
    },
    watch: {
      $route: {
        handler: function (route) {
          this.redirect = route.query && route.query.redirect
        },
        immediate: true
      }
    },
    methods: {
      async handleLogin() {
        try {
              if (this.loginForm.username == 'ITgroup') {
              // Redirect to a new page for ITgroup
                 console.log('Login to Admin');
                 this.$router.push({ path: '/itgroup-dashboard' });
            } else {
              // Redirect to the regular dashboard
               const response = await this.$axios.post('http://8.208.87.180:443/api/login/', {
                 username: this.loginForm.username,  // Make sure the field names match your Django model
                 password: this.loginForm.password,
              });
              
               if (response.data.success) {
                console.log('Received ID:', response.data.userID);

                 this.$store.commit('setUserID', response.data.userID);
                // 假设这是处理登录响应的部分
                 this.$store.commit('setIsSuperuser', response.data.is_superuser);

                 if (this.loginForm.username === 'ITgroup') {
              // Redirect to a new page for ITgroup
                     this.$router.push({ path: '/itgroup-dashboard' });
            } else{
              // Redirect to the regular dashboard
                     this.$router.push({ path: '/dashboard' });
            }
              } else {
                // Handle unsuccessful login
                console.error(response.data.message);
              }
            }
            } catch (error) {
              console.error('An error occurred during login:', error);
            } finally {
              this.loading = false;
            }

        // this.$refs.loginForm.validate(async (valid) => {
        //   if (valid) {
        //     this.loading = true;

        //     try {
        //       const response = await this.$axios.post('http://localhost:8000/api/login/', {
        //         username: this.loginForm.username,  // Make sure the field names match your Django model
        //         password: this.loginForm.password,
        //       });
              
        //       if (response.data.success) {
        //         this.$router.push({ path: '/dashboard' });
        //       } else {
        //         // Handle unsuccessful login
        //         console.error(response.data.message);
        //       }
        //     } catch (error) {
        //       console.error('An error occurred during login:', error);
        //     } finally {
        //       this.loading = false;
        //     }
        //   } else {
        //     console.log('Error submitting the form.');
        //   }
        // });
      },

      handleCreateAccount() {
        this.$router.replace({ path: '/createAccount' });
      }
    }
  }
</script>

<style scoped>
  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f2f2f2;
    background-image: url('https://www.timeshighereducation.com/sites/default/files/institution/header_image/the_profile_cover_image_-_main_building4_4.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center bottom;
    min-height: 100vh;
    width: 100%;
  }

  .login-form {
    width: 500px;
    background-color: #fff;
    border-radius: 8px;
    padding: 30px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  }

  .tips {
    font-size: 14px;
    color: #888; /* 改变提示颜色以更清晰 */
    margin-left: 30px;
  }

  .title-container {
    text-align: center;
    margin-bottom: 20px;
  }

  .title {
    font-size: 24px;
    color: #333;
  }

  .input-with-icon {
    position: relative;
    margin-bottom: 5px; /* 添加底部间距 */
    width: 420px;
  }

  .icon-wrapper {
    position: absolute;
    left: 1px; /* 调整图标的位置 */
    top: 40%;
    transform: translateY(-50%);
    color: #333; /* 图标颜色，根据需要调整 */
  }

  .scaled-icon {
    width: 30px; /* Adjust the width as needed */
    height: 30px; /* Adjust the height as needed */
    display: block; /* This makes sure the icon aligns properly */
  }

  .show-pwd {
    position: absolute;
    right: 30px;
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
  }

  .el-input, .el-input__inner {
    width: 100%; /* 输入框占满全部宽度 */
    border: none;
    padding-left: 20px; /* 为左侧图标留出空间 */
  }

  .el-input__inner {
    background-color: transparent;
    height: 40px; /* 输入框高度 */
  }

  .create-account-btn {
    color: #4a90e2;
    margin-top: 10px; /* 创建账号按钮的上间距 */
  }

  /* 响应式调整 */
  @media (max-width: 600px) {
    .login-form {
      width: 90%; /* 较小屏幕上宽度占比更高 */
      padding: 20px; /* 较小屏幕上减少内边距 */
    }

    .input-with-icon, .el-input, .el-input__inner {
      width: auto; /* 让宽度自适应，而非固定 */
    }

    .icon-wrapper, .show-pwd {
      display: none; /* 可能在小屏幕上隐藏图标以节省空间 */
    }

    .el-button {
      margin-left: 0; /* 移除登录按钮的左边距 */
      width: 100%; /* 按钮宽度调整为100% */
    }
  }
</style>
