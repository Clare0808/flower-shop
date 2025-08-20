<template>
  <div class="review">
    <div class="title">
      Customer's
      <span style="color: #ff79bc">Review</span>
    </div>
    <div class="flame">
      <div class="review-flame" v-for="(r, index) in reviewData" :key="index">
        <div class="star-flame">
          <div v-for="i in r.score" :key="i">
            <i class="fa-solid fa-star"></i>
          </div>
        </div>
        <div class="content">{{ r.content }}</div>
        <div class="user-info">
          <img :src="r.img" />
          <div class="text-flame">
            <div class="name">{{ r.name }}</div>
            <div class="date">{{ r.date }}</div>
          </div>
        </div>
      </div>
    </div>
    <div class="btn" @click="ShowWritePage">+</div>

    <WriteReviewPage class="write-page" v-if="showWrite" />
  </div>
</template>

<script>
import { ref, watch, onMounted } from "vue";
import WriteReviewPage from "@/components/WriteReviewPage.vue";
import { userMail, userImage } from "@/components/LoginPage.vue";

export const showWrite = ref(false);

export default {
  name: "ReviewPage",
  components: {
    WriteReviewPage,
  },
  setup() {
    const reviewData = ref([]);

    const ShowWritePage = () => {
      showWrite.value = true;
    };

    const GetReviewData = async () => {
      const response = await fetch("http://localhost:5000/api/getreview");
      const data = await response.json();

      reviewData.value = data.data;
      console.log(reviewData.value);
    };

    watch(showWrite);
    watch(reviewData);

    onMounted(() => {
      GetReviewData();
    });

    return {
      userImage,
      userMail,
      reviewData,
      showWrite,
      ShowWritePage,
      GetReviewData,
    };
  },
};
</script>

<style scoped>
.review {
  margin-top: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.title {
  font-size: 30px;
  background-color: #ffd9ec;
  width: 90%;
  padding: 2px;
}
.flame {
  width: 90%;
  padding: 50px;
  display: grid;
  grid-template-columns: repeat(3, 30%);
  gap: 20px;
  justify-content: center;
  align-items: center;
}
.review-flame {
  padding: 20px;
  box-shadow: 0px 0px 5px 3px #d0d0d0;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: start;
}
.star-flame {
  display: flex;
  justify-content: center;
  align-items: start;
}
i {
  color: #ff79bc;
  font-size: 20px;
}
.content {
  color: #adadad;
  text-align: start;
  margin: 20px 0;
}
.user-info {
  display: flex;
  justify-content: center;
  align-items: center;
}
img {
  width: 50px;
  border-radius: 50%;
}
.text-flame {
  text-align: start;
  color: #adadad;
  margin-left: 20px;
}
.name {
  color: #000000;
  font-size: 25px;
}
.btn {
  background-color: #ffd9ec;
  color: #ff79bc;
  font-size: 50px;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  position: fixed;
  bottom: 20px;
  right: 20px;
}
.btn:hover {
  background-color: #ff79bc;
  color: #ffffff;
  cursor: pointer;
}

.write-page {
  width: 40%;
  position: fixed;
  top: 25%;
  z-index: 2;
}
</style>
