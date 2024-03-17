<template src="./select-Course.html" >
  
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
          const response = await this.$axios.post('http://localhost:8000/api/creatAccount/', postData);

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

<style src="./select-Course.css" scoped>
 
</style>

