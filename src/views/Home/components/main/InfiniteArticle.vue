<template src="./InfiniteArticle.html" >

</template>

<script setup>
import ArticleCardFull from '@/components/article/ArticleCardFull.vue';
import axios from 'axios';
import { ref, onMounted, toRefs,computed } from 'vue';
import { useStore } from 'vuex';
import { defineProps } from 'vue';

const articleList = ref([]);
const selectedButton=ref('Lasted');

const props = defineProps({
  selectedButton: String
});

const selectedCourses = ref('');
const favorate = ref([]);

const store = useStore();
const { getUserID } = toRefs(store.getters);



onMounted(async () => {
  try {

    const userID = getUserID.value;

    // 发起 GET 请求获取选定课程数据
    //const response = await axios.get(`http://localhost:8000/api/get_postselectedCoursesString/${userID.value}/`);
    const response = await axios.post('http://localhost:8000/api/get_postselectedCoursesString/', { userID: userID });
    selectedCourses.value = response.data.selectedCourses;
    console.log(selectedCourses.value);

    // 对选定课程进行比较和筛选

  } catch (error) {
    console.error('Error fetching selected courses:', error);
  }
});


onMounted(async () => {
  try {

    const userID = getUserID.value;
    const response = await axios.post('http://localhost:8000/api/get_user_favorite_posts/', { userID: userID });
    const info = response.data.favorite_posts;
    for (let i = 0; i < info.length; i++) {
      favorate.value.push(info[i])
    }
    // 对选定课程进行比较和筛选

  } catch (error) {
    console.error('Error fetching selected courses:', error);
  }
});


onMounted(async () => {
  try {
    // 发起 GET 请求获取文章数据
    const response = await axios.get('http://localhost:8000/api/get_post/');
    const parsedPosts = response.data.posts;

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
  const relativePath = `../../../../assets/head/${img}`;
  const imageModule = await import(relativePath);
  return imageModule.default;
}

const filteredArticles = computed(() => {
  switch(props.selectedButton) {
    case 'Latest':
      return articleList.value;
    case 'Recommend':
      if (!selectedCourses.value) return []; // 如果 selectedCoursesString 不存在，则返回空数组
      console.log('selectedCoursesArray:', selectedCourses.value);
      console.log(props.selectedButton);
      return articleList.value.filter(article => {
         return article.classification === selectedCourses.value;
      });
    case 'Attention':
      if (!favorate.value || !favorate.value.length) return []; // If favorite.value doesn't exist or is an empty array, return an empty array

      return articleList.value.filter(article => {
        return favorate.value.some(fav => fav.id === article.id);
      });
    default:
      return [];

  }
});

</script>
