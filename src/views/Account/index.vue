<!-- MyComponent.vue -->
<template src="./MyComponent.html"></template>

<style src="./MyComponent.css" scoped></style>

<script setup>
// 例如，使用 "HomeMain" 而不是 "homeMain"
import HomeMain from './components/main/HomeMain.vue';
//import HomeRight from './components/right/HomeRight.vue';
import RightComponent from '@/components/template/right_component.vue';
</script>