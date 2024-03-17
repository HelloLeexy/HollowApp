<script setup>
import HomeAbove from './HomeAbove.vue';
import { CButtonGroup } from '@coreui/vue'
</script>

<template>


  <div style="height: 20px;"></div>
  <!-- 文章流 -->
  <HomeAbove />
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

</style>
