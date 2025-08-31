<template>
  <div class="contact">
    <div class="title">
      <span style="color: #ff79bc">Contact</span>
      Us
    </div>
    <transition name="slide">
      <div class="error" v-if="showError">{{ errorMsg }}</div>
    </transition>
    <transition name="slide">
      <div class="success" v-if="showSuccess">{{ successMsg }}</div>
    </transition>
    <transition name="fade">
      <div class="container" v-if="showPage">
        <div class="input-flame">
          <textarea
            class="input-name"
            type="text"
            placeholder="Name"
            v-model.trim="name"
          ></textarea>
          <textarea
            type="text"
            placeholder="Email"
            v-model.trim="email"
          ></textarea>
          <textarea
            type="text"
            placeholder="Number"
            v-model.trim="number"
          ></textarea>
          <textarea
            class="input-msg"
            type="text"
            placeholder="Message"
            v-model.trim="msg"
          ></textarea>
          <div class="btn" @click="SendComment">Send Message</div>
        </div>
        <img src="@/assets/contact.jpg" />
      </div>
    </transition>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { userMail } from "@/components/LoginPage.vue";

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
    const showError = ref(false);
    const errorMsg = ref("");
    const showPage = ref(false);

    const SendComment = async () => {
      EmptyInput();

      if (!showError.value) {
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
      }
    };

    const HandleDate = () => {
      const date = new Date();

      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const day = String(date.getDate()).padStart(2, "0");

      commentDate.value = `${year}-${month}-${day}`;
    };

    const AutoInputInfo = async () => {
      const response = await fetch("http://localhost:5000/api/info");
      const data = await response.json();

      const filterData = data.data.find(
        (item) => item.email === userMail.value
      );

      name.value = filterData.name;
      email.value = filterData.email;

      if (filterData.number !== "None") {
        number.value = filterData.number;
      } else {
        number.value = "";
      }
    };

    const EmptyInput = () => {
      if (name.value === "") {
        errorMsg.value = "Name is required !";
        showError.value = true;
      } else if (email.value === "") {
        errorMsg.value = "Email is required !";
        showError.value = true;
      } else if (number.value === "") {
        errorMsg.value = "Number is required !";
        showError.value = true;
      } else if (msg.value === "") {
        errorMsg.value = "Please enter your message !";
        showError.value = true;
      } else {
        showError.value = false;
      }

      setTimeout(() => {
        showError.value = false;
      }, 2000);
    };

    onMounted(() => {
      AutoInputInfo();
      showPage.value = true;
    });

    return {
      userMail,
      name,
      email,
      number,
      msg,
      showSuccess,
      successMsg,
      showError,
      errorMsg,
      showPage,
      SendComment,
      HandleDate,
      AutoInputInfo,
      EmptyInput,
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
.error {
  position: absolute;
  right: 5%;
  top: 80px;
  background-color: #ffb5b5;
  color: #ff2d2d;
  padding: 20px;
  text-align: center;
  font-size: 18px;
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
textarea {
  width: 85%;
  height: 15px;
  padding: 10px;
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
  margin-bottom: 20px;
  height: 100px;
}
textarea:focus {
  outline: none;
  border: 1px solid #ff79bc;
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
  transition: all 0.3s ease;
}
.btn:hover {
  background-color: #ff79bc;
  cursor: pointer;
  transform: scale(1.1);
}
img {
  width: 100%;
  border-radius: 20px;
}

@media (max-width: 1000px) {
  .container {
    width: 75%;
    display: flex;
    flex-direction: column;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: all 1s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(20px);
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
