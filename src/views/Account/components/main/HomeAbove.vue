<script setup>
import UserCardFull from '@/components/account/UserCardFull.vue';
import axios from 'axios';
import { ref, onMounted, toRefs } from 'vue';
import { useStore } from 'vuex';

const store = useStore();
const { getUserID } = toRefs(store.getters);

const userList = ref([]);

onMounted(async () => {
  try {
    // 发起 POST 请求获取用户数据
    const userID = getUserID.value;
    const response = await axios.post('http://localhost:8000/api/get_user/', { userID: userID });
    
    const users = response.data.users;

    if (users.length > 0) {
      const user = users[0];
      const imgSrc = await requireImage(user.img);
      
      // 将后端返回的数据赋值给 userList
      userList.value.push({
        ...user,
        imgSrc: imgSrc,
      });
    }
  } catch (error) {
    console.error('Error fetching users:', error);
  }
});

async function requireImage(img) {
  // 动态导入图片
  const relativePath = `../../../../assets/head/${img}`;
  // 动态导入图片，使用相对路径
  const imageModule = await import(relativePath);
  return imageModule.default;
}
</script>

<template src="./HomeAbove.html" >

</template>
