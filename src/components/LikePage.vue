<template>
  <div class="like-page">
    <div class="title">
      Your
      <span style="color: #ff79bc">Favorate</span>
    </div>
    <div class="container">
      <div class="flame" v-for="i in 6" :key="i">
        <img src="@/assets/product2.jpg" />
        <div class="item-flame">
          <div class="text-flame">
            <div class="name">Flower Pot</div>
            <div class="price">$15.99</div>
          </div>
          <i class="fa-solid fa-heart"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LikePage",
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
</style>
