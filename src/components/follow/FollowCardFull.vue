<template>
  <div class="body" v-for="article in articleList" :key="article.poster">
    <img :src="imagePaths[article.img]" style="height: 50px; border-radius: 50%; margin-right: 15px;"/>
    <div class="row">
      <div style="width: 100%;">
      </div>
    </div>
    <div style="height: 10px;"></div>
    <div class="box-card">
      <div class="row">
        <div style="flex: 1;">
          <div class="title">Name {{ article.username }}</div>
          <div class="title">Birth day {{ article.dbo }}</div>
          <div class="title">Study of Year {{ article.studyOfYear }}</div>
          <div style="margin-top: 10px;" class="text">{{ article.aboutMe }}</div>
          <div style="height: 15px;"></div>
        </div>
        <div style="flex: 0 0 7rem; display: flex; flex-direction: column; align-items: flex-end;">
          <el-button type="danger" @click="handleImageClick(article)">UnFollow</el-button>
          <div>
            <img :src="article.coverImg" style="height: 120px; border-radius: 10px; margin-top: 10px;" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { Tag as VanTag } from 'vant';
import axios from 'axios';
import { ElMessage } from 'element-plus';
import { useStore } from 'vuex';

export default {
  computed: {
    imagePaths() {
      return this.$store.state.imagePaths;
    },
  },
  components: {
    VanTag,
  },
  props: {
    author: {
      type: Number,
      required: true,
    },
    articleList: {
      type: Array,
      default: () => [],
    },
  },

  setup(props) {
    const store = useStore();
    const userID = store.getters.getUserID;
    const router = useRouter();
    const reactiveArticleList = ref(props.articleList);

    const handleImageClick = async (article) => {
      const posterID = article.user_id;
      try {
        const response = await axios.post('http://8.208.87.180:443/api/unfollow/', {
          userID,
          posterID,
        });

        // Handle the backend response if needed
        ElMessage.success(response.data);

        // Update the reactiveArticleList to trigger a reactivity change
        reactiveArticleList.value = reactiveArticleList.value.filter(person => person.user_id !== posterID);
      } catch (error) {
        console.error('Error pushing information to backend:', error);
      }
    };

    const jumpDetailsPage = (aid) => {
      router.push(`/details/${aid}`);
    };

    return {
      handleImageClick,
      jumpDetailsPage,
      reactiveArticleList,
    };
  },
};
</script>

<style scoped>
.icon-container {
  display: flex;
}

.icon-wrapper {
  display: flex;
  align-items: center; /* Align items vertically in the center */
  margin-right: 20px; /* Add some margin between the icon and text for spacing */
}

.scaled-icon {
  width: 20px; /* Set the width of the icon as needed */
  height: 20px; /* Set the height of the icon as needed */
  margin-right: 5px; /* Adjust the margin as needed */
  margin-bottom: -5px;
}

.icon {
  display: inline-block;
}


.row {
  display: flex;
  align-items: center; /* 垂直居中 */
}



.body {
  margin-top: 10px;
  margin-bottom: 5px;
}

.title {
  font-size: 14px;
  font-weight: bolder;
}

.text {
  font-size: 14px;
}

.tag {
  margin-right: 5px;
}



.box-card {
  width: 100%;
  margin-left: 0%;
  border-radius: 6px;
  border: 2px solid #ccc;
  padding: 15px;
  box-shadow: 10px 10px 10px rgba(0, 0, 0, 0.1);
}
</style>
