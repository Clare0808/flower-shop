<template>
  <div class="list-page">
    <div class="title">Products List</div>
    <div class="empty" v-if="listData.length === 0">Nothing here.</div>
    <div class="container">
      <div class="flame" v-for="(l, index) in listData" :key="index">
        <div class="list">
          <img :src="l.img" />
          <div class="text">{{ l.email }}</div>
          <div class="text">{{ l.date }}</div>
          <div class="text">{{ l.product }}</div>
          <div class="text">x{{ l.quantity }}</div>
          <div class="text-p">${{ l.price }}</div>
          <div class="total">${{ l.total }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  setup() {
    const listData = ref([]);

    const GetListData = async () => {
      const response = await fetch("http://localhost:5000/api/getbuy");
      const data = await response.json();

      listData.value = data.data;
      console.log(listData.value);
    };

    onMounted(() => {
      GetListData();
    });

    return {
      listData,
      GetListData,
    };
  },
};
</script>

<style scoped>
.list-page {
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
.list {
  width: 95%;
  margin: 10px 0;
  display: grid;
  grid-template-columns: 8% 30% 15% 15% 5% 8% 10%;
  gap: 10px;
  justify-content: space-between;
  align-items: center;
}
img {
  width: 80px;
  height: 80px;
}
.text {
  font-size: 24px;
}
.text-p {
  width: 10%;
  font-size: 24px;
}
.total {
  font-size: 24px;
  color: #ff79bc;
}
</style>
