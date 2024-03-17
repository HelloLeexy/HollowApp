<template>
  <div class="box-card">
    <div class="body" v-for="user in userList" :key="user.username" @click="jumpDetailsPage(user.username)">
      <div class="row">
        <div style="width: 100%;">
          <!-- 使用 imagePaths[user.img] 动态获取用户头像路径 -->
          <img :src="imagePaths[user.img]" style="height: 100px; border-radius: 50%; margin-right: 15px;" />
          {{ user.username }}
        </div>
      </div>
      <div style="height: 10px;"></div>
      <div class="row">
        <div style="flex: 1;">
          <div class="title">ID: {{ user.username }}</div>
          <div style="margin-top: 10px;" class="text">Programme: {{ user.programme }}</div>
          <div style="margin-top: 10px;" class="text">Age: {{ user.age }}</div>
          <div style="margin-top: 10px;" class="text">Year of study: {{ user.yearOfStudy }}</div>
          <div style="margin-top: 10px;" class="text">About me: {{ user.aboutMe }}</div>
          <div style="height: 15px;"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { mapState } from 'vuex';

export default {
  props: {
    userList: {
      type: Array,
      default: () => []
    }
  },
  computed: {
    imagePaths() {
      return this.$store.getters.getImagePaths;
    }
  },
  setup() {
    const router = useRouter();

    const jumpDetailsPage = (username) => {
      console.log(imagePaths[user.img])
      router.push(`/details/${username}`);
    }

    return {
      jumpDetailsPage
    };
  }
};
</script>

<style scoped>
.body {
  margin-top: 10px;
  margin-bottom: 5px;
}

.row {
  display: flex;
  justify-content: space-between;
}

.title {
  font-size: 14px;
  font-weight: bolder;
}

.text {
  font-size: 14px;
}

.box-card {
  width: 100%;
  margin-left: 0%;
  border-radius: 6px;
}
</style>
