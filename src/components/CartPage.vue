<template>
  <div class="cart-page">
    <div class="title">
      Your
      <span style="color: #ff79bc">Cart</span>
    </div>
    <div class="container">
      <div class="flame" v-for="i in 8" :key="i">
        <div class="items-flame">
          <img src="@/assets/product1.jpg" />
          <div class="item-info">
            <div class="text-flame">
              <div class="item-name">Flowers Pot</div>
              <div class="item-quan">x3</div>
            </div>
            <div class="num-flame">
              <div class="item-price">$15.99</div>
              <div class="total-price">$47.97</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CartPage",
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
