<template>
  <div class="product">
    <div class="title">
      Least
      <span style="color: #ff79bc">Product</span>
    </div>
    <transition name="slide">
      <div class="success" v-if="showSuccess">{{ successMsg }}</div>
    </transition>
    <transition name="fade">
      <div class="container" v-if="showPage">
        <div class="pro-flame" v-for="(p, index) in productsData" :key="index">
          <div class="img-flame">
            <img :src="p.img" @click="ShowFunction(index)" />
            <div class="function">
              <i
                class="fa-solid fa-heart"
                :class="{ liked: p.like }"
                @click="SendLikeData(index)"
              ></i>
              <div class="add" @click="ShowBuyPage(index)">Add To Cart</div>
              <i class="fa-solid fa-share"></i>
            </div>
          </div>
          <div class="name">{{ p.name }}</div>
          <div class="price">${{ p.price }}</div>
        </div>
      </div>
    </transition>

    <transition name="fade">
      <BuyPage class="buy-page" v-if="showBuy" />
    </transition>
  </div>
</template>

<script>
import { ref, onMounted, watch } from "vue";
import { userMail } from "@/components/LoginPage.vue";
import BuyPage from "@/components/BuyPage.vue";
import { showBuySuccess } from "@/components/BuyPage.vue";

export const showBuy = ref(false);
export const buyData = ref({});

export default {
  name: "ProductPage",
  components: {
    BuyPage,
  },
  setup() {
    const productsData = ref([
      {
        id: 1,
        name: "Product 1",
        price: 15.99,
        img: require("@/assets/product1.jpg"),
        like: false,
      },
      {
        id: 2,
        name: "Product 2",
        price: 12.99,
        img: require("@/assets/product2.jpg"),
        like: false,
      },
      {
        id: 3,
        name: "Product 3",
        price: 9.99,
        img: require("@/assets/product3.jpg"),
        like: false,
      },
      {
        id: 4,
        name: "Product 4",
        price: 19.99,
        img: require("@/assets/product4.jpg"),
        like: false,
      },
      {
        id: 5,
        name: "Product 5",
        price: 25.99,
        img: require("@/assets/product5.jpg"),
        like: false,
      },
      {
        id: 6,
        name: "Product 6",
        price: 8.99,
        img: require("@/assets/product6.jpg"),
        like: false,
      },
    ]);
    const hover = ref(false);
    const successMsg = ref("");
    const showSuccess = ref(false);
    const showPage = ref(false);

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
      const response = await fetch("http://localhost:5000/api/getlike");
      const data = await response.json();

      const booleanData = data.data.some(
        (item) =>
          item.email === userMail.value &&
          item.product === productsData.value[index].name
      );

      const filterData = data.data.find(
        (item) =>
          item.email === userMail.value &&
          item.product === productsData.value[index].name
      );

      //const filterProductData = productsData.value.map((item) => item.name);

      if (booleanData) {
        const response = await fetch("http://localhost:5000/api/delete", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ product: filterData.product }),
        });

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        successMsg.value = "Remove from favorate !";
        showSuccess.value = true;

        productsData.value[index].like = false;

        setTimeout(() => {
          showSuccess.value = false;
        }, 2000);
      } else {
        const userResponse = await fetch(
          "http://localhost:5000/api/storelike",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              email: userMail.value,
              product: productsData.value[index].name,
              price: productsData.value[index].price,
              image: productsData.value[index].img,
            }),
          }
        );

        if (!userResponse.ok) {
          throw new Error("Network response was not ok");
        }

        successMsg.value = "Put in favorate !";
        showSuccess.value = true;

        productsData.value[index].like = true;

        setTimeout(() => {
          showSuccess.value = false;
        }, 2000);
      }
    };

    const HandleLike = async () => {
      const response = await fetch("http://localhost:5000/api/getlike");
      const data = await response.json();

      const filterData = data.data.filter(
        (item) => item.email === userMail.value
      );

      const filterProductData = productsData.value.map((item) => item.name);

      for (let i = 0; i < filterData.length; i++) {
        if (filterProductData.includes(filterData[i].product)) {
          const markProduct = productsData.value.find(
            (item) => item.name === filterData[i].product
          );

          markProduct.like = true;
        }
      }
    };

    const ShowBuyPage = (index) => {
      showBuy.value = true;

      buyData.value = productsData.value[index];
    };

    watch(showBuy);
    watch(showBuySuccess, () => {
      successMsg.value = "Add in cart successfully !";
      showSuccess.value = true;

      showBuySuccess.value = false;

      setTimeout(() => {
        showSuccess.value = false;
      }, 2000);
    });

    onMounted(() => {
      HandleLike();
      showPage.value = true;
    });

    return {
      userMail,
      showBuySuccess,
      productsData,
      hover,
      successMsg,
      showSuccess,
      showBuy,
      showPage,
      ShowFunction,
      SendLikeData,
      HandleLike,
      ShowBuyPage,
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
  position: relative;
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
i:active {
  color: #000000;
}
i.liked {
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

.buy-page {
  width: 50%;
  position: fixed;
  top: 15%;
  z-index: 2;
}

@media (max-width: 1050px) {
  .container {
    grid-template-columns: repeat(2, 45%);
    grid-template-rows: repeat(3, 450px);
    gap: 20px;
  }
}
@media (max-width: 650px) {
  .container {
    grid-template-columns: 80%;
    grid-template-rows: repeat(6, 500px);
    gap: 20px;
  }
  .buy-page {
    width: 70%;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: all 1s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(100px);
}
.fade-enter-to,
.fade-leave-from {
  opacity: 1;
  transform: translateY(0);
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.6s ease;
}
.slide-enter-from,
.slide-leave-to {
  opacity: 0;
  transform: translateX(20px);
}
.slide-enter-to,
.slide-leave-from {
  opacity: 1;
  transform: translateX(0);
}
</style>
