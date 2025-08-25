<template>
  <div class="cart-page">
    <div class="title">
      Your
      <span style="color: #ff79bc">Cart</span>
    </div>
    <div class="success" v-if="showSuccess">{{ successMsg }}</div>
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
          <div class="buy-flame">
            <div class="buy-btn" @click="SendBuy(index)">Buy</div>
            <div class="delete" @click="DeleteCart(index)">Delete</div>
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
    const showSuccess = ref(false);
    const successMsg = ref("");

    const GetCartData = async () => {
      const response = await fetch("http://localhost:5000/api/getcart");
      const data = await response.json();

      const filterData = data.data.filter(
        (item) => item.email === userMail.value
      );

      cartData.value = filterData;

      console.log(cartData.value);
    };

    const SendBuy = async (index) => {
      const response = await fetch("http://localhost:5000/api/storebuy", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: userMail.value,
          product: cartData.value[index].name,
          price: cartData.value[index].price,
          img: cartData.value[index].img,
          quantity: cartData.value[index].quantity,
          total: cartData.value[index].total,
        }),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      successMsg.value = "Buy successfully!";
      showSuccess.value = true;

      setTimeout(async () => {
        showSuccess.value = false;
        await DeleteCart(index);
      }, 2000);
    };

    const DeleteCart = async (index) => {
      const response = await fetch("http://localhost:5000/api/deletecart", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: cartData.value[index].name,
          quantity: cartData.value[index].quantity,
        }),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      GetCartData();

      successMsg.value = "Delete successfully!";
      showSuccess.value = true;

      setTimeout(() => {
        showSuccess.value = false;
      }, 2000);
    };

    onMounted(() => {
      GetCartData();
    });

    return {
      cartData,
      userMail,
      showSuccess,
      successMsg,
      GetCartData,
      SendBuy,
      DeleteCart,
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
  position: relative;
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
.buy-flame {
  margin-right: 20px;
}
.buy-btn {
  width: 100px;
  height: 25px;
  background-color: #000000;
  color: #ffffff;
  text-align: center;
  line-height: 25px;
  padding: 5px;
  border-radius: 10px;
  margin: 10px 0;
}
.buy-btn:hover {
  background-color: #ff79bc;
  color: #ffffff;
  cursor: pointer;
}
.delete {
  width: 100px;
  height: 25px;
  background-color: #ffd9ec;
  color: #ff79bc;
  text-align: center;
  line-height: 25px;
  padding: 5px;
  border-radius: 10px;
  margin: 10px 0;
}
.delete:hover {
  color: #ffffff;
  background-color: #ff79bc;
  cursor: pointer;
}
</style>
