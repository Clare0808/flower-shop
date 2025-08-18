<template>
  <div class="cart-page">
    <div class="title">
      Your
      <span style="color: #ff79bc">Cart</span>
    </div>
    <div class="container">
      <div class="flame" v-for="(c, index) in cartData" :key="index">
        <div class="items-flame">
          <img :src="c.img" />
          <div class="item-info">
            <div class="text-flame">
              <div class="item-name">{{ c.name }}</div>
              <div class="item-quan">x{{ c.quantity }}</div>
            </div>
            <div class="num-flame">
              <div class="item-price">${{ c.price }}</div>
              <div class="total-price">${{ c.total }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { userMail } from "@/components/LoginPage.vue";

export default {
  name: "CartPage",
  setup() {
    const cartData = ref([]);

    const GetCartData = async () => {
      const response = await fetch("http://localhost:5000/api/getcart");
      const data = await response.json();

      const filterData = data.data.filter(
        (item) => item.email === userMail.value
      );

      cartData.value = filterData;

      console.log(cartData.value);
    };

    onMounted(() => {
      GetCartData();
    });

    return {
      cartData,
      userMail,
      GetCartData,
    };
  },
};
</script>

<style scoped>
.cart-page {
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
.container {
  width: 90%;
  padding: 50px;
  display: grid;
  grid-template-columns: 48% 48%;
  grid-template-rows: repeat(4, 100px);
  gap: 20px;
  justify-content: center;
  align-items: center;
}
.flame {
  width: 100%;
}
.items-flame {
  width: 100%;
  box-shadow: 0px 0px 5px 3px #d0d0d0;
  display: flex;
  justify-content: start;
  align-items: center;
}
img {
  width: 100px;
  height: 100px;
}
.item-info {
  flex: 1;
  margin: 0 20px;
}
.text-flame {
  font-size: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.item-name {
  font-size: 25px;
  text-align: start;
}
.num-flame {
  font-size: 20px;
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.total-price {
  font-size: 25px;
  color: #ff79bc;
}
</style>
