<script setup>
import InfiniteArticle from './InfiniteArticle.vue';
import { CButtonGroup } from '@coreui/vue'
import { ref } from 'vue';

const selectedButton = ref('Latest');

const selectButton = (button) => {

  selectedButton.value = button;
};

</script>

<template src="./HomeMain.html" >
   
</template>

<style src="./HomeMain.css" scoped>


</style>
