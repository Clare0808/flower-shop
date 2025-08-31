<template>
  <div class="comment-page">
    <div class="title">Customers Review</div>
    <div class="empty" v-if="commentData.length === 0">Nothing here.</div>
    <div class="container">
      <div class="flame" v-for="(c, index) in commentData" :key="index">
        <div class="comment">
          <div class="text">{{ c.name }}</div>
          <div class="text">{{ c.date }}</div>
          <div class="text">{{ c.email }}</div>
          <div class="text">{{ c.number }}</div>
          <div class="text-de">{{ c.content }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  setup() {
    const commentData = ref([]);

    const GetCommentData = async () => {
      const response = await fetch("http://localhost:5000/api/getcomment");
      const data = await response.json();

      commentData.value = data.data;
    };

    onMounted(() => {
      GetCommentData();
    });

    return {
      commentData,
      GetCommentData,
    };
  },
};
</script>

<style scoped>
.comment-page {
  height: calc(100% - 40px);
  background-color: #ffffff;
  border-radius: 10px;
  padding: 20px;
}
.title {
  font-size: 30px;
  color: #ff79bc;
  padding-bottom: 10px;
  margin-bottom: 10px;
  border-bottom: 2px solid #ff79bc;
}
.empty {
  color: #adadad;
  font-size: 24px;
  margin-top: 50px;
}
.container {
  max-height: 92%;
  overflow-y: auto;
}
.flame {
  display: flex;
  justify-content: center;
  align-items: center;
}
.comment {
  width: 95%;
  margin: 10px 0;
  text-align: left;
  display: grid;
  grid-template-columns: 10% 15% 25% 15% 30%;
  gap: 10px;
  justify-content: space-between;
  align-items: center;
}
.text {
  font-size: 20px;
}
.text-de {
  font-size: 18px;
  color: #adadad;
  text-align: left;
}
</style>
