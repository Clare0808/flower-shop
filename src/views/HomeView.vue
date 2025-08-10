<template>
  <div class="home">
    <div class="container">
      <div class="title">Fresh Flowers</div>
      <div class="sec-title">Natural & Beautiful Flowers</div>
      <div class="description">
        Rose, Tulip, are native to Central Asia, Carnation, Known to symbolise
        love and deep fascination, Lily, Daisy, a great symbol of happiness,
        Camellia, symbolise love and affection...
      </div>
      <div class="btn">Shop Now</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style scoped>
.home {
  width: 100%;
  height: 100%;
  background-image: url("@/assets/background.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: right bottom;
  position: absolute;
  top: 0;
  left: 0;
}
.container {
  padding-top: 200px;
  padding-left: 100px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
}
.title {
  font-size: 50px;
  font-weight: bold;
  margin-bottom: 10px;
}
.sec-title {
  font-size: 35px;
  color: #ff79bc;
  margin-bottom: 10px;
}
.description {
  width: 450px;
  font-size: 20px;
  text-align: start;
  margin-bottom: 20px;
}
.btn {
  width: 100px;
  height: 25px;
  background-color: #000000;
  color: #ffffff;
  text-align: center;
  line-height: 25px;
  padding: 5px;
  border-radius: 10px;
}
.btn:hover {
  background-color: #ff79bc;
  cursor: pointer;
}
</style>
