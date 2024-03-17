<!-- 文章卡片缩小版 -->
<script setup>
import { useRouter } from 'vue-router';
// 应该接收数据
import { defineProps } from 'vue';
const props = defineProps({
    articleList: {
        type: Array,
        default: () => []
    }
});

const router = useRouter();
const jumpArticlePage = (aid) => {
    
}


</script>

<template src="./ArticleCardHot.html" >
</template>

  
<style src="./ArticleCardHot.css" scoped>

</style>
  