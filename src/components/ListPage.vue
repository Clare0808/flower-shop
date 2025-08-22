<template>
  <div class="list-page">
    <div class="title">Products List</div>
    <div class="flame">
      <div class="list">
        <img src="@/assets/product1.jpg" />
        <div class="text">User 1</div>
        <div class="text">Product 1</div>
        <div class="text">x3</div>
        <div class="text">$12.99</div>
        <div class="total">$37.99</div>
      </div>
    </div>
  </div>
</template>

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
.flame {
  display: flex;
  justify-content: center;
  align-items: center;
}
.list {
  width: 95%;
  margin: 10px 0;
  display: flex;
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
.total {
  font-size: 24px;
  color: #ff79bc;
}
</style>
