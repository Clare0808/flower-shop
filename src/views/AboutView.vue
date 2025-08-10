<template>
  <div class="about">
    <div class="title">
      About
      <span style="color: #ff79bc">Us</span>
    </div>
    <div class="container">
      <div class="img-flame">
        <img src="@/assets/about.jpg" />
        <div class="sec-title">Best Flower Sellers</div>
      </div>
      <div class="text-flame">
        <div class="third-title">Why Choose Us</div>
        <div class="description">
          Rose, Tulip, are native to Central Asia, Carnation, Known to symbolise
          love and deep fascination, Lily, Daisy, a great symbol of happiness,
          Camellia, symbolise love and affection... Rose, Tulip, are native to
          Central Asia, Carnation, Known to symbolise love and deep fascination,
          Lily, Daisy, a great symbol of happiness, Camellia, symbolise love and
          affection...
        </div>
        <div class="description">
          Rose, Tulip, are native to Central Asia, Carnation, Known to symbolise
          love and deep fascination, Lily, Daisy, a great symbol of happiness,
          Camellia, symbolise love and affection...
        </div>
        <div class="btn">Learn More</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AboutView",
};
</script>

<style scoped>
.about {
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
  display: flex;
  justify-content: center;
  align-items: center;
}
.img-flame {
  position: relative;
}
img {
  width: 650px;
}
.sec-title {
  width: 100%;
  font-size: 50px;
  font-weight: bold;
  padding: 5px;
  mix-blend-mode: screen;
  background-color: #ffffff;
  position: absolute;
  top: 40%;
}
.text-flame {
  text-align: start;
  padding-left: 20px;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: start;
}
.third-title {
  font-size: 40px;
  margin-bottom: 20px;
}
.description {
  margin-bottom: 10px;
  font-size: 20px;
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
  margin-top: 10px;
}
.btn:hover {
  background-color: #ff79bc;
  cursor: pointer;
}
</style>
