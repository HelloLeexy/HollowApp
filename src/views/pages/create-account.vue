<template>
  <div class="account-container">
    <el-form ref="accountForm" :model="accountForm" :rules="accountRules" class="account-form" auto-complete="on" label-position="left">

      <div class="title-container">
        <h3 class="title">Create your account</h3>
      </div>

      <el-form-item prop="username">
        <el-input v-model="accountForm.username"
                  placeholder="User Name"
                  name="username"
                  type="text"
                  auto-complete="on" />
      </el-form-item>

      <el-form-item prop="password">
        <el-input v-model="accountForm.password"
                  placeholder="Password"
                  name="password"
                  type="password"
                  auto-complete="on" />
      </el-form-item>

      <el-form-item prop="age">
        <el-input v-model="accountForm.age"
                  placeholder="Age"
                  name="age"
                  type="number"
                  auto-complete="on" />
      </el-form-item>

      <el-form-item prop="dob">
        <el-input v-model="accountForm.dob"
                  placeholder="Date of birth DD/MM/YY"
                  name="dob"
                  type="text"
                  auto-complete="on" />
      </el-form-item>

      <el-form-item prop="yearOfStudy">
        <el-input v-model="accountForm.yearOfStudy"
                  placeholder="Year of study"
                  name="yearOfStudy"
                  type="text"
                  auto-complete="on" />
      </el-form-item>

      <el-form-item prop="programme">
        <el-input v-model="accountForm.programme"
                  placeholder="Programme"
                  name="programme"
                  type="text"
                  auto-complete="on" />
      </el-form-item>

      <el-form-item prop="aboutMe">
        <el-input v-model="accountForm.aboutMe"
                  placeholder="About me"
                  name="aboutMe"
                  type="text"
                  auto-complete="on" />
      </el-form-item>

      <el-button type="primary" style="width:100%;" @click="handleContinue">Continue</el-button>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'CreateAccount',
  data() {
    return {
      accountForm: {
        username: '',
        password: '',
        age:'',
        dob:'',
        yearOfStudy:'',
        programme:'',
        aboutMe:'',
        // Add other form fields here
      },
    };
  },
  methods: {
    async handleContinue() {
      this.$router.push({
            path: '/selectCourse',
            query: { accountForm: JSON.stringify(this.accountForm) },
          });
      // try {
      //   // Send the account data to the Django backend
      //   const response = await this.$axios.post('http://localhost:8000/api/creatAccount/', this.accountForm);

      //   if (response.data.success) {
      //     // Successfully created account, navigate to the next page
      //     this.$router.push('/selectCourse');
      //   } else {
      //     // Handle unsuccessful account creation
      //     console.error(response.data.message);
      //   }
      // } catch (error) {
      //   console.error('An error occurred during account creation:', error);
      // }
    },
  },
};
</script>

<style scoped>
  .account-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f2f2f2; /* 灰色背景 */
    background-image: url('https://www.timeshighereducation.com/sites/default/files/institution/header_image/the_profile_cover_image_-_main_building4_4.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center bottom;
    min-height: 100vh;
    width: 100%;
  }

  .title-container {
    margin-bottom: 20px;
  }

  .title {
    text-align: center;
    color: #333; /* 标题颜色 */
  }

  .account-form {
    width: 700px; /* 表单宽度 */
    max-width: 100%;
    padding: 30px;
    background-color: #fff; /* 白色背景 */
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* 阴影效果 */
  }

  .el-form-item {
    margin-bottom: 20px;
  }

  .el-button {
    width: 100%;
    background-color: #007bff; /* 默认的蓝色按钮背景 */
    color: #fff;
    border: none;
    border-radius: 5px;
    transition: background-color 0.3s;
  }

    .el-button:hover {
      background-color: #0056b3; /* 鼠标悬停时的按钮背景颜色 */
    }
</style>
