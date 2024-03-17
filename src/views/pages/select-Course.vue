<template>
  <div class="course-selection-container">
    <el-form ref="courseSelectionForm" :model="courseSelectionForm" class="course-selection-form" label-position="top">

      <div class="title-container">
        <h3 class="title">Select Your Courses</h3>
        <p class="subtitle">Pick tags that you want to see in your home page</p>
      </div>

      <el-form-item class="course-item">
        <el-checkbox-group v-model="courseSelectionForm.selectedCourses">
          <el-checkbox label="Programming" name="courseProgramming">Programming</el-checkbox>
          <el-checkbox label="Internet Technology" name="courseInternetTechnology">Internet Technology</el-checkbox>
          <el-checkbox label="Advanced Programming" name="courseAdvancedProgramming">Advanced Programming</el-checkbox>
          <el-checkbox label="Information Visualisation" name="courseInformationVisualisation">Information Visualisation</el-checkbox>
          <el-checkbox label="Database Theory And Analytics" name="courseDatabaseTheoryAndAnalytics">Database Theory And Analytics</el-checkbox>
          <el-checkbox label="Forensics" name="courseForensics">Forensics</el-checkbox>
          <el-checkbox label="Enterprise Cyber Security" name="courseEnterpriseCyberSecurity">Enterprise Cyber Security</el-checkbox>
          <el-checkbox label="IT+ Team Project" name="courseITPlusTeamProject">IT+ Team Project</el-checkbox>
          <el-checkbox label="Software Engineering" name="courseSoftwareEngineering">Software Engineering</el-checkbox>
          <el-checkbox label="System And Networks" name="courseSystemAndNetworks">System And Networks</el-checkbox>
          <el-checkbox label="Human Computer Interaction Design And Evaluation" name="courseHCI">Human Computer Interaction Design And Evaluation</el-checkbox>
          <el-checkbox label="Cryptography And Secure Development" name="courseCryptographyAndSecureDevelopment">Cryptography And Secure Development</el-checkbox>
          <el-checkbox label="Cybersecurity Fundamentals for Msc" name="courseCybersecurityFundamentalsForMsc">Cybersecurity Fundamentals for Msc</el-checkbox>
        </el-checkbox-group>
      </el-form-item>

      <el-button type="primary" :disabled="courseSelectionForm.selectedCourses.length === 0" @click="handleContinue">Select at least 1 to continue</el-button>
    </el-form>
  </div>
</template>

<script>
  import { createStore } from 'vuex';
  export default {
    name: 'SelectCourses',
    data() {
      return {
        courseSelectionForm: {
          selectedCourses: []
        },
        receivedAccountForm: null,
        selectedCoursesString:'',
      };
    },
    created() {
    // 检查是否有 accountForm 作为 query 参数
    if (this.$route.query.accountForm) {
      // 解析 JSON 字符串
      this.receivedAccountForm = JSON.parse(this.$route.query.accountForm);

      // 在这里可以使用 this.receivedAccountForm
      console.log('Received accountForm:', this.receivedAccountForm);
    }
  },
    methods: {
      async handleContinue() {
        // 将 selectedCourses 数组拼接成字符串，用 '|' 分隔
        this.selectedCoursesString = this.courseSelectionForm.selectedCourses.join('|');

        // 将拼接好的字符串添加到 courseSelectionForm 中
        this.courseSelectionForm.selectedCoursesString = this.selectedCoursesString;  // Corrected this line

        try {
          // 合并 courseSelectionForm 和 receivedAccountForm
          const postData = {
            ...this.courseSelectionForm,  // Corrected this line
            ...this.receivedAccountForm,
          };

          // 发送数据到后端
          const response = await this.$axios.post('http://8.208.87.180:443/api/creatAccount/', postData);

          if (response.data.success) {
            // 成功，跳转到 dashboard 页面或其他需要的页面
            console.log('Received ID:', response.data.userID);
            this.$store.commit('setUserID', response.data.userID);
            this.$router.push('/dashboard');
          } else {
            // 处理后端返回的错误
            console.error(response.data.message);
          }
        } catch (error) {
          console.error('An error occurred during data submission:', error);
        }
},

    }
  };
</script>

<style scoped>
  .course-selection-container {
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

  .subtitle {
    text-align: center;
    color: #666; /* 副标题颜色 */
    margin-bottom: 30px;
  }

  .course-selection-form {
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

    .el-button:disabled {
      background-color: #9ecbff; /* 按钮禁用时的背景颜色 */
      color: #fff;
      cursor: not-allowed;
    }

  .el-checkbox-group {
    width: 100%;
    border: none;
  }

  .el-checkbox {
    margin-right: 10px; /* 复选框间距 */
  }

  .el-checkbox__label {
    color: #333; /* 复选框标签颜色 */
  }
</style>

