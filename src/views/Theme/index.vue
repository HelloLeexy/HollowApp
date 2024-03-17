<template>
  <div class="app-container">
    <div class="post-container">
      <el-form ref="form" :model="form" label-width="120px">
        <el-form-item label="Post title">
          <el-input v-model="form.title" />
        </el-form-item>
        <el-form-item label="Tag">
          <el-select v-model="form.region" placeholder="please select your post category">
            <el-option label="Programming" value="Programming" />
            <el-option label="Internet Technology" value="Internet Technology" />
            <el-option label="Advanced Programming" value="Advanced Programming" />
            <el-option label="Information Visualisation" value="Information Visualisation" />
            <el-option label="Database Theory And Analytics" value="Database Theory And Analytics" />
            <el-option label="Forensics" value="Forensics" />
            <el-option label="Enterprise Cyber Security" value="Enterprise Cyber Security" />
            <el-option label="IT+ Team Project" value="IT+ Team Project" />
            <el-option label="Software Engineering" value="Software Engineering" />
            <el-option label="System And Networks" value="System And Networks" />
            <el-option label="Human Computer Interaction Design And Evaluation" value="Human Computer Interaction Design And Evaluation" />
            <el-option label="Cryptography And Secure Development" value="Cryptography And Secure Development" />
            <el-option label="Cybersecurity Fundamentals for Msc" value="Cybersecurity Fundamentals for Msc" />
          </el-select>
        </el-form-item>
        
        <el-form-item label="Post content">
          <el-input v-model="form.desc" type="textarea" :rows="10"/>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">Create</el-button>
          <el-button @click="onCancel">Cancel</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
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
        const response = await this.$axios.post('http://8.208.87.180:443/api/post/', {
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


<style scoped>
  .app-container {
    display: flex;
    justify-content: center;
    padding: 20px;
  }

  .post-container {
    width: 95%; /* Adjust based on your preference */
    height:500px;
    background: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 12px 0 rgba(0,0,0,0.1);
  }

  .el-form-item {
    margin-bottom: 30px;
  }

  .el-input {
    width: 100%;
  }
</style>

