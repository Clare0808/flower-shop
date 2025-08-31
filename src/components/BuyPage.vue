<template>
  <div class="buy-page">
    <div class="title">
      <span style="color: #ff79bc">Buy</span>
      Product
    </div>
    <div class="container">
      <div class="img-flame">
        <img :src="buyData.img" />
      </div>
      <div class="flame">
        <div class="sec-title">Product</div>
        <div class="content">{{ buyData.name }}</div>
      </div>
      <div class="flame">
        <div class="sec-title">Price</div>
        <div class="content">${{ buyData.price }}</div>
      </div>
      <div class="flame">
        <div class="sec-title">Quantity</div>
        <div class="num-flame">
          <div class="btn" @click="ChangeQuantity(-1)">-</div>
          <div class="content">{{ counter }}</div>
          <div class="btn" @click="ChangeQuantity(1)">+</div>
        </div>
      </div>
      <div class="flame">
        <div class="sec-title">Total</div>
        <div class="content-total">${{ total }}</div>
      </div>
      <div class="btn-flame">
        <div class="no-btn" @click="CloseBuyPage">Cancel</div>
        <div class="send" @click="SendBuy">Add to card</div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { showBuy, buyData } from "@/components/ProductPage.vue";
import { userMail } from "@/components/LoginPage.vue";

export const showBuySuccess = ref(false);

export default {
  setup() {
    const counter = ref(1);
    const total = ref(buyData.value.price);

    const CloseBuyPage = () => {
      showBuy.value = false;
    };

    const ChangeQuantity = (num) => {
      counter.value += num;

      if (counter.value <= 1) {
        counter.value = 1;

        total.value = buyData.value.price;
      }

      total.value = counter.value * buyData.value.price;
    };

    const SendBuy = async () => {
      const response = await fetch("http://localhost:5000/api/storecart", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: userMail.value,
          name: buyData.value.name,
          price: buyData.value.price,
          img: buyData.value.img,
          quantity: counter.value,
          total: total.value,
        }),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      CloseBuyPage();

      showBuySuccess.value = true;
    };

    return {
      showBuy,
      buyData,
      userMail,
      counter,
      total,
      CloseBuyPage,
      ChangeQuantity,
      SendBuy,
    };
  },
};
</script>

<style scoped>
.buy-page {
  background-color: #ffffff;
  box-shadow: 0px 0px 5px 3px #d0d0d0;
  padding: 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
}
.title {
  font-size: 30px;
  background-color: #ffd9ec;
  width: 100%;
  padding: 2px;
}
.container {
  width: calc(100% - 40px);
  padding: 20px;
  max-height: 400px;
  overflow-y: auto;
  flex: 1;
}
.img-flame {
  width: 100%;
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
img {
  width: 60%;
  box-shadow: 0px 0px 5px 3px #d0d0d0;
}
.flame {
  width: 100%;
  margin-top: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.sec-title {
  font-size: 18px;
  color: #000000;
  text-align: left;
}
.num-flame {
  display: flex;
  justify-content: center;
  align-items: center;
}
.content {
  font-size: 22px;
  color: #adadad;
}
.num-flame .content {
  font-size: 22px;
  color: #adadad;
  margin: 0 10px;
}
.btn {
  color: #adadad;
  font-size: 22px;
  border: 1px solid #adadad;
  width: 20px;
  height: 20px;
  line-height: 20px;
  transition: all 0.3s ease;
}
.btn:hover {
  cursor: pointer;
  background-color: #ff79bc;
  color: #ffffff;
  transform: scale(1.3);
}
.content-total {
  font-size: 22px;
  color: #ff79bc;
}
.btn-flame {
  margin-top: 40px;
  display: flex;
  justify-content: center;
}
.no-btn,
.send {
  width: 100px;
  height: 25px;
  background-color: #000000;
  color: #ffffff;
  text-align: center;
  line-height: 25px;
  padding: 5px;
  border-radius: 10px;
  transition: all 0.3s ease;
}
.send:hover {
  background-color: #ff79bc;
  cursor: pointer;
  transform: scale(1.1);
}
.no-btn {
  background-color: #ffd9ec;
  color: #ff79bc;
  margin-right: 20px;
}
.no-btn:hover {
  cursor: pointer;
  background-color: #ff79bc;
  color: #ffffff;
  transform: scale(1.1);
}
</style>
