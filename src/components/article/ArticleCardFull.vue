<!-- InfiniteArticle.vue -->
<template>
  <div class="body" v-for="article in articleList" :key="article.poster">
    <div class="row">
      <div style="width: 100%;">
        <img
          :src= imagePaths[article.img]
          style="height: 30px; border-radius: 50%; margin-right: 15px;"
          @click="handleImageClick(article)"
        />
        {{ article.poster }}
        <span>{{ article.publish_date }}</span>
        <span style="margin-right: 10px;"> classification </span>
        <el-tag class="tag">{{ article.classification }}</el-tag>
      </div>
    </div>
    <div style="height: 10px;"></div>
    <div class="box-card">
      <div class="row">
        <div style="flex: 1;">
          <div @click="jumpDetailsPage(article.id)">
            <div class="title">{{ article.title }}</div>
            <div style="margin-top: 10px;" class="text">{{ article.content }}</div>
            <div style="height: 15px;"></div>
          </div>
          <div class="icon-container">
            <div class="icon-wrapper">
              <img src="@/assets/icons/dianzan.png" alt="Your Icon" class="scaled-icon">
              <div class="icon">{{ article.likes }}</div>
            </div>
            <div class="icon-wrapper">
              <img src="@/assets/icons/yanjing.png" alt="Your Icon" class="scaled-icon">
              <div class="icon">{{ article.views_count }}</div>
            </div>
            <div class="icon-wrapper" @click="Favorite(article)">
              <img src="@/assets/icons/favorite.png" alt="Your Icon" class="scaled-icon">
            </div>
            <!--add delete button-->
            
          </div>
        </div>

        <div style="flex: 0 0 8rem;">
          <div>
            <img :src="article.coverImg" style="height: 120px; border-radius: 7px;" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, toRefs } from 'vue';
import { useRouter } from 'vue-router';
import { Tag as VanTag } from 'vant';
import axios from 'axios';
import { ElMessage } from 'element-plus';
import { useStore } from 'vuex'; // Import useStore from 'vuex'

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
    const store = useStore(); // Initialize the store
    const { getUserID } = toRefs(store.getters);

    const router = useRouter();

    
    const Favorite = async (article) => {
      const userID = getUserID.value;
      const postID = article.id;
      try {
        console.log(userID)
        console.log(postID)
        const response = await axios.post('http://8.208.87.180:443/api/add_favorite/', {
          user_id: userID,
          post_id: postID,
        })
        // Handle the backend response if needed
        ElMessage.success(response.data);
      } catch (error) {
        console.error('Error pushing information to backend:', error);
      }
    };




    const handleImageClick = async (article) => {
      const userID = getUserID.value;
      
      const posterID = article.poster_id;
      try {
        console.log(userID)
        console.log(posterID)
        const response = await axios.post('http://8.208.87.180:443/api/follow/', {
          userID: userID,
          posterID: posterID,
        });

        // Handle the backend response if needed
        ElMessage.success(response.data);
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
      Favorite,
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
