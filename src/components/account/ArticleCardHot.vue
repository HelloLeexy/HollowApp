<script setup>
import { useRouter } from 'vue-router';

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

<template src="./ArticleCardHot.html"> </template>

  
<style src="./ArticleCardHot.css" scoped> </style>
  