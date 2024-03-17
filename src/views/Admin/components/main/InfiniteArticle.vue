<script  setup>
// 文章流组件
import ArticleCardFull from '@/components/admin/adminCardFull.vue';
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
    const response = await axios.get('http://localhost:8000/api/get_admin/');
    console.log(response.data)
    // 检查响应结构
    // console.log(JSON.parse(response.data.posts));
    const parsedPosts = response.data.posts;
    console.log(parsedPosts)
    for (let i = 0; i < parsedPosts.length; i++) {
      const article = parsedPosts[i];
      articleList.value.push({
        ...article,
        imgSrc: await requireImage(article.img),
      });
    }
  } catch (error) {
    console.error('Error fetching articles:', error);
  }
});

async function requireImage(img) {
  // 动态导入图片
  const relativePath = `../../../../assets/head/${img}`;
  console.log(relativePath);
  // 动态导入图片，使用相对路径
  const imageModule = await import(relativePath);
  return imageModule.default;
}

</script>

<template src="./InfiniteArticle.html" >

</template>
