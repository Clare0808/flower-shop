<template>
  <div class="product">
    <div class="title">
      Least
      <span style="color: #ff79bc">Product</span>
    </div>
    <div class="success" v-if="showSuccess">{{ successMsg }}</div>
    <div class="container">
      <div class="pro-flame" v-for="(p, index) in productsData" :key="index">
        <div class="img-flame">
          <img :src="p.img" @click="ShowFunction(index)" />
          <div class="function">
            <i class="fa-solid fa-heart" @click="SendLikeData(index)"></i>
            <div class="add">Add To Cart</div>
            <i class="fa-solid fa-share"></i>
          </div>
        </div>
        <div class="name">{{ p.name }}</div>
        <div class="price">${{ p.price }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { userMail } from "@/components/LoginPage.vue";

export default {
  name: "ProductPage",
  setup() {
    const productsData = [
      {
        id: 1,
        name: "Product 1",
        price: 15.99,
        img: require("@/assets/product1.jpg"),
      },
      {
        id: 2,
        name: "Product 2",
        price: 12.99,
        img: require("@/assets/product2.jpg"),
      },
      {
        id: 3,
        name: "Product 3",
        price: 9.99,
        img: require("@/assets/product3.jpg"),
      },
      {
        id: 4,
        name: "Product 4",
        price: 19.99,
        img: require("@/assets/product4.jpg"),
      },
      {
        id: 5,
        name: "Product 5",
        price: 25.99,
        img: require("@/assets/product5.jpg"),
      },
      {
        id: 6,
        name: "Product 6",
        price: 8.99,
        img: require("@/assets/product6.jpg"),
      },
    ];
    const hover = ref(false);
    const successMsg = ref("");
    const showSuccess = ref(false);

    const ShowFunction = (index) => {
      hover.value = !hover.value;

      const functions = document.querySelectorAll(".function");

      functions.forEach((f, i) => {
        if (hover.value && i === index) {
          f.style.display = "flex";
        } else {
          f.style.display = "none";
        }
      });
    };

    const SendLikeData = async (index) => {
      const userResponse = await fetch("http://localhost:5000/api/storelike", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: userMail.value,
          product: productsData[index].name,
          price: productsData[index].price,
          image: productsData[index].img,
        }),
      });

      if (!userResponse.ok) {
        throw new Error("Network response was not ok");
      }

      successMsg.value = "Put in favorate !";
      showSuccess.value = true;

      setTimeout(() => {
        showSuccess.value = false;
      }, 2000);
    };

    return {
      userMail,
      productsData,
      hover,
      successMsg,
      showSuccess,
      ShowFunction,
      SendLikeData,
    };
  },
};
</script>

<style scoped>
.product {
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
  position: absolute;
  right: 5%;
  top: 80px;
  background-color: #a6ffa6;
  color: #00db00;
  padding: 20px;
  text-align: center;
  font-size: 18px;
}
.container {
  width: 90%;
  padding: 35px;
  display: grid;
  grid-template-columns: repeat(3, 30%);
  grid-template-rows: repeat(2, 450px);
  justify-content: center;
  align-items: center;
}
.img-flame {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
img {
  max-width: 90%;
  box-shadow: 0px 0px 5px 3px #d0d0d0;
  cursor: pointer;
}
.function {
  width: 90%;
  background-color: #ff79bc;
  color: #ffffff;
  padding: 5px 0;
  font-size: 25px;
  cursor: pointer;
  display: none;
  justify-content: space-between;
  align-items: center;
  position: absolute;
  bottom: 0;
}
i {
  margin: 0 20px;
}
i:hover {
  color: #000000;
}
.add:hover {
  color: #000000;
}
.name {
  font-size: 25px;
  margin: 10px 0;
}
.price {
  color: #ff79bc;
  font-size: 25px;
}
</style>
