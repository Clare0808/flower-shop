<template>
  <div class="user-page">
    <div class="title">
      <span style="color: #ff79bc">User</span>
      Information
    </div>
    <div class="container">
      <div class="img-flame">
        <img src="@/assets/user1.jpg" />
      </div>
      <div class="text-flame">
        <div class="info">
          <div class="info-title">Name</div>
          <div class="info-content">John Doe</div>
        </div>
        <div class="info">
          <div class="info-title">Birthday</div>
          <div class="info-content">2023/10/31</div>
        </div>
        <div class="info">
          <div class="info-title">Email</div>
          <div class="info-content">123456@gmail.com</div>
        </div>
        <div class="info">
          <div class="info-title">Number</div>
          <div class="info-content">0912345678</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserPage",
};
</script>

<style scoped>
.user-page {
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
  grid-template-columns: 35% 60%;
  grid-template-rows: 100%;
  gap: 20px;
  justify-content: center;
  align-items: center;
}
.img-flame {
  display: flex;
  justify-content: center;
  align-items: center;
}
img {
  width: 300px;
  height: 300px;
  box-shadow: 0px 0px 5px 3px #d0d0d0;
}
.info {
  position: relative;
  padding: 30px;
  padding-bottom: 10px;
  border-bottom: 1px solid #d0d0d0;
}
.info-title {
  position: absolute;
  top: 10px;
  left: 10px;
  color: #000000;
  font-size: 18px;
}
.info-content {
  color: #adadad;
  font-size: 22px;
  text-align: center;
  margin-top: 20px;
}
</style>
