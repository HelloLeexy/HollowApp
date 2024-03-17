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

<template>

  <div class="container">

    <CFormFloating>
    <CFormTextarea
      id="floatingTextarea"
      floatingLabel="Search"
      placeholder="Leave a comment here"
    ></CFormTextarea>
  </CFormFloating>
    <br>
    <CListGroup>
      <CListGroupItem class="d-flex justify-content-between align-items-center">Internet Technology<CBadge color="primary" shape="rounded-pill">14</CBadge></CListGroupItem>
      <CListGroupItem class="d-flex justify-content-between align-items-center">Information Visualization<CBadge color="primary" shape="rounded-pill">2</CBadge></CListGroupItem>
      <CListGroupItem class="d-flex justify-content-between align-items-center">Human-Computer Interaction<CBadge color="primary" shape="rounded-pill">1</CBadge></CListGroupItem>
    </CListGroup>

    <br>
    <el-badge value="hot" class="item">
      <div class="section-header">
        <el-text>Hot topics</el-text>
      </div>
    </el-badge>
    <el-card class="card" shadow="never">
      <ArticleCardMini :articleList="articleList" />
    </el-card>

    <br>
    <el-badge value="hot" class="item">
      <div class="section-header">
        <el-text>Active users</el-text>
      </div>
    </el-badge>
    <el-card class="card" shadow="never">
      <ArticleCardMini :articleList="userList" />
    </el-card>
  </div>



</template>

<style scoped>
.container {
  margin-top: 18px;
}

.section {
  margin-bottom: 10px;
}

.section-header {
  margin-bottom: 10px;
}

.card {
  shadow: never;
}

.tag {
  /* Add any specific styling for the tags */
}

.input {
  /* Add any specific styling for the input */
}

.item {
  margin-bottom: 10px;
}
</style>

