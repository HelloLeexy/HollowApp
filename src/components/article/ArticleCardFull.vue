<!-- InfiniteArticle.vue -->
<template src="./ArticleCardFull.html">

</template>

<script>
import { ref, onMounted, toRefs } from 'vue';
import { useRouter } from 'vue-router';
import { Tag as VanTag } from 'vant';
import axios from 'axios';
import { ElMessage } from 'element-plus';
import { useStore } from 'vuex'; // Import useStore from 'vuex'

export default {
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
        const response = await axios.post('http://localhost:8000/api/add_favorite/', {
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
        const response = await axios.post('http://localhost:8000/api/follow/', {
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

<style src="./ArticleCardFull.css" scoped>

</style>
