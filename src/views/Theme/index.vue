<template src="./index.html" >
 
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  computed: {
    ...mapGetters(['getUserID']), // 将 getUserID 映射到当前组件的 computed 中
  },
  data() {
    return {
      form: {
        title: '',
        region: '',
        desc: ''
      }
    };
  },
  methods: {
    async onSubmit() {
      const userID = this.getUserID;
      try {
        // 使用 Axios 或其他 HTTP 请求库发送 POST 请求
        const response = await this.$axios.post('http://localhost:8000/api/post/', {
          userID: userID,
          title: this.form.title,
          region: this.form.region,
          desc: this.form.desc,
        });

        if (response.data.success) {
          this.$message.success(response.data.message);
          this.$router.push('/dashboard');
          console.log('Trying to navigate to /account');
        } else {
          this.$message.error(response.data.message);
        }
      } catch (error) {
        console.error('An error occurred during submission:', error);
        this.$message.error('An error occurred. Please try again later.');
      }
    },
    onCancel() {
      this.$message({
        message: 'cancel!',
        type: 'warning'
      });
    }
  },
};
</script>


<style src="./index.css"  scoped>
 
</style>

