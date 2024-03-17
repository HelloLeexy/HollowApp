<template src="./create-account.html" >
 
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

<style src="./create-account.css" scoped>
 
</style>
