<!-- 展示分类与搜索框 -->
<script setup>
import ArticleCardMini from '@/components/account/ArticleCardHot.vue';
import { ref, onMounted } from 'vue';
import { CListGroup } from '@coreui/vue'
//import { useRouter } from 'vue-router';
//const router = useRouter();




const articleList = ref([])
const userList = ref([])
// 加载热点文章数据
onMounted(() => {
    // 获取数据
    // getIndexHot().then(res => {
    //     articleList.value = res.data.page.list;
    // });
    // getTypes().then(res => {
    //     console.log('全部分类', res);
    //     types.value = res.data
    // })

    // 模拟的数据
    articleList.value = [{
        title: 'Course View:Whats your favorit...'
    },
    {
        title: 'Are you ready for the valentines...'
    },
    {
        title: 'Any one know about Internet Tech..'
    },
    ]

      userList.value = [{
        title: 'Natilia Chrom'
    },
    {
        title: 'Alex Moors'
    },
    {
        title: 'John Beer'
    },
    ]

});

</script>

<template src="./HomeRight.html" >
</template>

<style src="./HomeRight.css" scoped>

</style>

