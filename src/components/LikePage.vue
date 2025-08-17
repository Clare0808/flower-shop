<template>
  <div class="like-page">
    <div class="title">
      Your
      <span style="color: #ff79bc">Favorate</span>
    </div>
    <div class="success" v-if="showSuccess">{{ successMsg }}</div>
    <div class="container">
      <div class="flame" v-for="(p, index) in likeData" :key="index">
        <img :src="p.image" />
        <div class="item-flame">
          <div class="text-flame">
            <div class="name">{{ p.product }}</div>
            <div class="price">{{ p.price }}</div>
          </div>
          <i class="fa-solid fa-heart" @click="RemoveLike(p.product)"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { userMail } from "@/components/LoginPage.vue";

export default {
  name: "LikePage",
  setup() {
    const likeData = ref([]);
    const showSuccess = ref(false);
    const successMsg = ref("");

    const GetLikeData = async () => {
      const response = await fetch("http://localhost:5000/api/getlike");
      const data = await response.json();

      const filterData = data.data.filter(
        (item) => item.email === userMail.value
      );

      likeData.value = filterData;
    };

    const RemoveLike = async (product) => {
      const response = await fetch("http://localhost:5000/api/delete", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ product }),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      GetLikeData();

      successMsg.value = "Remove successfully !";
      showSuccess.value = true;

      setTimeout(() => {
        showSuccess.value = false;
      }, 2000);
    };

    onMounted(() => {
      GetLikeData();
    });

    return {
      userMail,
      likeData,
      showSuccess,
      successMsg,
      GetLikeData,
      RemoveLike,
    };
  },
};
</script>

<style scoped>
.like-page {
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
.success {
  position: fixed;
  right: 5%;
  top: 80px;
  z-index: 2;
  background-color: #a6ffa6;
  color: #00db00;
  padding: 20px;
  text-align: center;
  font-size: 18px;
}
.container {
  width: 85%;
  padding: 50px;
  display: grid;
  grid-template-columns: repeat(3, 30%);
  grid-template-rows: repeat(2, 450px);
  gap: 20px;
  justify-content: center;
  align-items: center;
}
.flame {
  box-shadow: 0px 0px 5px 3px #d0d0d0;
}
img {
  width: 100%;
}
.item-flame {
  margin: 20px 0;
  text-align: start;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.text-flame {
  padding-left: 20px;
}
.name {
  font-size: 25px;
  margin-bottom: 10px;
}
.price,
i {
  font-size: 20px;
  color: #ff79bc;
}
i {
  padding-right: 20px;
}
i:hover {
  color: #ffd9ec;
}
</style>
