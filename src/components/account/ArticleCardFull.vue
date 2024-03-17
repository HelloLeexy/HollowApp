<template>
  <div class="body" v-for="article in articleList" :key="article.poster" @click="jumpDetailsPage(article.poster)">
    <div class="row">
      <div style="width: 100%;">
        {{ article.poster }}
        <span>{{ article.publish_date }}</span>
        <span style="margin-right: 10px;"> classification </span>
        <el-tag class="tag">{{ article.classification }}</el-tag>
      </div>
    </div>
    <div style="height: 10px;"></div>
              <!-- <img src="@/assets/icons/dianzan.png" alt="Your Icon" class="scaled-icon">  -->
    <div class="box-card">
      <div class="row">
        <div style="flex: 1;">
          <div class="title">{{ article.title }}</div>
          <div style="margin-top: 10px;" class="text">{{ article.content }}</div>
          <div style="height: 15px;"></div>

          <div class="icon-container">
            <div class="icon-wrapper">
              <img src="@/assets/icons/dianzan.png" alt="Your Icon" class="scaled-icon">
              <div class="icon">{{ article.likes }}</div>
            </div>
            <div class="icon-wrapper">
              <img src="@/assets/icons/yanjing.png" alt="Your Icon" class="scaled-icon">
              <div class="icon">{{ article.views_count }}</div>
            </div>
            <div class="icon-wrapper">
              <img src="@/assets/icons/pinglun.png" alt="Your Icon" class="scaled-icon">
              <div class="icon">30</div>
            </div>
          </div>
        </div>



        <div style="flex: 0 0 8rem;">
          <div>
            <img :src="article.coverImg" style="height: 120px; border-radius: 7px;" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

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

<style scoped>
.icon-container {
  display: flex;
}

.icon-wrapper {
  display: flex;
  align-items: center; /* Align items vertically in the center */
  margin-right: 20px; /* Add some margin between the icon and text for spacing */
}

.scaled-icon {
  width: 20px; /* Set the width of the icon as needed */
  height: 20px; /* Set the height of the icon as needed */
  margin-right: 5px; /* Adjust the margin as needed */
  margin-bottom: -5px;
}

.icon {
  display: inline-block;
}


.row {
  display: flex;
  align-items: center; /* 垂直居中 */
}



.body {
  margin-top: 10px;
  margin-bottom: 5px;
}

.title {
  font-size: 14px;
  font-weight: bolder;
}

.text {
  font-size: 14px;
}

.tag {
  margin-right: 5px;
}



.box-card {
  width: 100%;
  margin-left: 0%;
  border-radius: 6px;
  border: 2px solid #ccc;
  padding: 15px;
  box-shadow: 10px 10px 10px rgba(0, 0, 0, 0.1);
}
</style>
