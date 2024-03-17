<template src="./FollowCardFull.html" >

</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { Tag as VanTag } from 'vant';
import axios from 'axios';
import { ElMessage } from 'element-plus';
import { useStore } from 'vuex';

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
    const store = useStore();
    const userID = store.getters.getUserID;
    const router = useRouter();
    const reactiveArticleList = ref(props.articleList);

    const handleImageClick = async (article) => {
      const posterID = article.user_id;
      try {
        const response = await axios.post('http://localhost:8000/api/unfollow/', {
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

<style src="./FollowCardFull.css" scoped>

</style>
