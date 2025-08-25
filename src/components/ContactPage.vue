<template>
  <div class="contact">
    <div class="title">
      <span style="color: #ff79bc">Contact</span>
      Us
    </div>
    <div class="success" v-if="showSuccess">{{ successMsg }}</div>
    <div class="container">
      <div class="input-flame">
        <input
          class="input-name"
          type="text"
          placeholder="Name"
          v-model.trim="name"
        />
        <input type="text" placeholder="Email" v-model.trim="email" />
        <input type="number" placeholder="Number" v-model.trim="number" />
        <input
          class="input-msg"
          type="text"
          placeholder="Message"
          v-model.trim="msg"
        />
        <div class="btn" @click="SendComment">Send Message</div>
      </div>
      <img src="@/assets/contact.jpg" />
    </div>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  name: "ContactPage",
  setup() {
    const name = ref("");
    const email = ref("");
    const number = ref("");
    const msg = ref("");
    const commentDate = ref("");
    const showSuccess = ref(false);
    const successMsg = ref("");

    const SendComment = async () => {
      HandleDate();

      const response = await fetch("http://localhost:5000/api/sendcomment", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: name.value,
          email: email.value,
          number: number.value,
          date: commentDate.value,
          content: msg.value,
        }),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      successMsg.value = "Comment Send successfully!";
      showSuccess.value = true;

      name.value = "";
      email.value = "";
      number.value = "";
      msg.value = "";

      setTimeout(async () => {
        showSuccess.value = false;
      }, 2000);
    };

    const HandleDate = () => {
      const date = new Date();

      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const day = String(date.getDate()).padStart(2, "0");

      commentDate.value = `${year}-${month}-${day}`;
    };

    return {
      name,
      email,
      number,
      msg,
      showSuccess,
      successMsg,
      SendComment,
      HandleDate,
    };
  },
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
input:focus {
  outline: none;
  border: 1px solid #ff79bc;
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
