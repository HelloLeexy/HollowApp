<script setup>
import InfiniteArticle from './InfiniteArticle.vue';
import HomeAbove from './HomeAbove.vue';
import { CButtonGroup } from '@coreui/vue'
</script>

<template>
  <div style="height: 20px;"></div>
  <!-- 文章流 -->
  <HomeAbove />
  <div style="height: 15px;"></div>

  <CButtonGroup role="group" aria-label="Basic example" class="custom-button-group">
    <CButton class="custom-button" variant="outline-secondary">My Posts</CButton>
    <!-- <CButton class="custom-button" variant="outline-secondary">Recommend</CButton>
    <CButton class="custom-button" variant="outline-secondary">Your attention</CButton> -->
  </CButtonGroup>

  <div style="height: 20px;"></div>
  <!-- 文章流 -->
  <InfiniteArticle />
  <div style="height: 15px;"></div>
</template>

<style scoped>

  .custom-button-group .btn {
    position: relative;
  }

  .custom-button-group .btn:not(:last-child)::after {
    content: '';
    position: absolute;
    top: 50%;
    right: 0;
    transform: translateY(-50%);
    height: 100%;
    width: 1px;
    background-color: white; /* 白色竖线的颜色 */
    margin-left: 8px; /* 调整竖线与按钮之间的距离 */
  }

  .custom-button-group {
  display: flex;
}

.custom-button {
  position: relative;
  background-color: #778899; /* 浅灰色背景 */
  color: #333; /* 字体颜色 */
  transition: color 0.3s; /* 添加过渡效果 */
  width: 10px; /* 设置按钮宽度 */
  text-align: center; /* 文字居中 */
}

.custom-button:active {
  color: #5bc0de; /* 按下按钮时的浅蓝色字体 */
}
</style>
