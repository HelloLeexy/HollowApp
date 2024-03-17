<script  setup>
// 文章流组件
import ArticleCardFull from '@/components/article/ArticleCardFull.vue';
import { ref, onMounted } from 'vue';

const articleList = ref([]);

onMounted(() => {
  // 从后端获取数据
  // getIndexTime().then(res => {
  //   articleList.value = res.data.page.list;
  //   console.log('首页返回数据',articleList.value);
  // });

  // 模拟的数据流
  articleList.value = [{
    aid: 1,
    author:"Natalia Chrom",
    createTime:"2023-05-29 23:57:19",
    description:"How to install the compiler in IT class?",
    likeCount:1,
    pageView:24,
    status:true,
    tags:[],
    title:"Install compiler",
    type:"IT",
    uavator:"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fss2.meipian.me%2Fusers%2F50268721%2F748a1a83123240b099d96223d436d6bd.jpeg%3Fmeipian-raw%2Fbucket%2Fivwen%2Fkey%2FdXNlcnMvNTAyNjg3MjEvNzQ4YTFhODMxMjMyNDBiMDk5ZDk2MjIzZDQzNmQ2YmQuanBlZw%3D%3D%2Fsign%2Fd25a20fb972dbce6cf04e6cff260073d.jpg&refer=http%3A%2F%2Fss2.meipian.me&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1711481574&t=6e26d1ea4e1955a0953135f4e50a8205",
    updateTime:"2023-06-02 11:53:17"
  }, {
    aid: 2,
    author:"快乐星球",
    createTime:"2023-05-29T23:57:19",
    description:"axios获取请求",
    likeCount:6,
    pageView:34,
    status:true,
    tags:[],
    title:"axios获取请求",
    type:"axios",
    uavator:"https://img0.baidu.com/it/u=1091210682,206783907&fm=253&app=138&size=w931&n=0&f=JPEG&fmt=auto?sec=1684602000&t=1813754cb45a25a646263c4b3a711514",
    updateTime:"2023-06-02T11:53:17"
  },{
    aid: 3,
    author:"Natalia Chrom",
    createTime:"2023-05-29 23:57:19",
    description:"How to install the compiler in IT class?",
    likeCount:1,
    pageView:24,
    status:true,
    tags:[],
    title:"Install compiler",
    type:"IT",
    uavator:"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fss2.meipian.me%2Fusers%2F50268721%2F748a1a83123240b099d96223d436d6bd.jpeg%3Fmeipian-raw%2Fbucket%2Fivwen%2Fkey%2FdXNlcnMvNTAyNjg3MjEvNzQ4YTFhODMxMjMyNDBiMDk5ZDk2MjIzZDQzNmQ2YmQuanBlZw%3D%3D%2Fsign%2Fd25a20fb972dbce6cf04e6cff260073d.jpg&refer=http%3A%2F%2Fss2.meipian.me&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1711481574&t=6e26d1ea4e1955a0953135f4e50a8205",
    updateTime:"2023-06-02 11:53:17"
  }]
});

</script>

<template>
  <div>
    <ArticleCardFull :articleList="articleList" />
  </div>
</template>
