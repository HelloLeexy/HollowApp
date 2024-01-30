<template>
  <h1>{{ message }}</h1>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      message: "",
    };
  },
  mounted() {

    // 使用 axios 获取后端数据
    axios.get("http://localhost:8000/api/hello-world/")
        .then(response => {
          console.log(response.data); // 输出获取到的数据
          this.message = response.data.message;
        })
        .catch(error => {
          console.error(error);
          console.log('hithere');
        });
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
h1 {
  font-size: 2em;
}
</style>
