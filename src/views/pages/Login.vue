<template src="./Login.html" >
  
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
               const response = await this.$axios.post('http://localhost:8000/api/login/', {
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

<style src="./Login.css" scoped>
 
</style>
