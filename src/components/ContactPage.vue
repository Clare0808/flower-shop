<template>
  <div class="contact">
    <div class="title">
      <span style="color: #ff79bc">Contact</span>
      Us
    </div>
    <div class="container">
      <div class="input-flame">
        <input class="input-name" type="text" placeholder="Name" />
        <input type="text" placeholder="Email" />
        <input type="number" placeholder="Number" />
        <input class="input-msg" type="text" placeholder="Message" />
        <div class="btn">Send Message</div>
      </div>
      <img src="@/assets/contact.jpg" />
    </div>
  </div>
</template>

<script>
export default {
  name: "ContactPage",
};
</script>

<style scoped>
.contact {
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
.input-flame {
  width: 100%;
  height: 100%;
  box-shadow: 0px 0px 5px 3px #d0d0d0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
input {
  width: 90%;
  height: 25px;
  border: 1px solid #adadad;
  border-radius: 10px;
  margin: 10px 10px;
}
.input-name {
  margin-top: 20px;
}
.input-msg {
  height: 100px;
  margin-bottom: 20px;
}
.btn {
  width: 150px;
  height: 25px;
  padding: 5px;
  margin-bottom: 20px;
  color: #ffffff;
  background-color: #000000;
  border-radius: 10px;
  text-align: center;
  line-height: 25px;
}
.btn:hover {
  background-color: #ff79bc;
  cursor: pointer;
}
img {
  width: 100%;
  border-radius: 20px;
}
</style>
