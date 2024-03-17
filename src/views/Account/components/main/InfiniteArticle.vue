<script  setup>
// 文章流组件
import ArticleCardFull from '@/components/account/ArticleCardFull.vue';
import axios from 'axios';
import { ref, onMounted, toRefs } from 'vue';
import { useStore } from 'vuex';

const store = useStore();
const { getUserID } = toRefs(store.getters);
const articleList = ref([]);

onMounted(async () => {
  try {
    // 发起 GET 请求获取文章数据
    const userID = getUserID.value;
    const response = await axios.post('http://8.208.87.180:443/api/get_userPost/', { userID: userID });
    console.log(response.data)
    // 检查响应结构
    // console.log(JSON.parse(response.data.posts));
    const parsedPosts = response.data.posts;
    console.log(parsedPosts)
    for (let i = 0; i < parsedPosts.length; i++) {
      const article = parsedPosts[i];
      articleList.value.push({
        ...article,
      });
    }
  } catch (error) {
    console.error('Error fetching articles:', error);
  }
});

</script>

<template>
  <div>
    <ArticleCardFull :articleList="articleList" />
  </div>
</template>
