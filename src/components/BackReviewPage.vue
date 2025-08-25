<template>
  <div class="review-page">
    <div class="title">Customers Review</div>
    <div class="container">
      <div class="flame" v-for="(r, index) in backReview" :key="index">
        <div class="review">
          <div class="text">{{ r.name }}</div>
          <div class="star-flame">
            <div v-for="i in r.score" :key="i">
              <i class="fa-solid fa-star"></i>
            </div>
          </div>
          <div class="text">{{ r.date }}</div>
          <div class="text-de">{{ r.content }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  setup() {
    const backReview = ref([]);

    const GetReviewData = async () => {
      const response = await fetch("http://localhost:5000/api/getreview");
      const data = await response.json();

      backReview.value = data.data;
    };

    onMounted(async () => {
      await GetReviewData();
    });

    return {
      backReview,
      GetReviewData,
    };
  },
};
</script>

<style scoped>
.review-page {
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
.container {
  max-height: 92%;
  overflow-y: auto;
}
.flame {
  display: flex;
  justify-content: center;
  align-items: center;
}
.review {
  width: 95%;
  margin: 10px 0;
  display: grid;
  grid-template-columns: 10% 15% 15% 55%;
  gap: 10px;
  justify-content: space-between;
  align-items: center;
}
.text {
  font-size: 22px;
}
.star-flame {
  display: flex;
  justify-content: center;
  align-items: center;
}
i {
  color: #ff79bc;
}
.text-de {
  font-size: 18px;
  color: #adadad;
  text-align: left;
}
</style>
