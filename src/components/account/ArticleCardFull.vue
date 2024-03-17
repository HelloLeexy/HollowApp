<template src="./ArticleCardFull.html"> </template>
<style src="./ArticleCardFull.css" scoped> </style>
<script>
import { ref, defineProps } from 'vue';
import { useRouter } from 'vue-router';
import { Tag as VanTag } from 'vant';

export default {
  components: {
    VanTag,
    // 其他组件...
  },
  props: {
    author: {
      type: Number,
      required: true
    },
    articleList: {
      type: Array,
      default: () => []
    }
  },

  setup(props) {
    const router = useRouter();

    const jumpDetailsPage = (aid) => {
      router.push(`/details/${aid}`);
    }

    return {
      jumpDetailsPage
    };
  }
};
</script>


