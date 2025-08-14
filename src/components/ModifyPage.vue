<template>
  <div class="modify-page">
    <div class="title">
      <span style="color: #ff79bc">Modify</span>
      Information
    </div>
    <div class="success" v-if="showSuccess">{{ successMsg }}</div>
    <div class="container">
      <div class="flame">
        <div class="info-title">Original {{ modifyData.title }}</div>
        <div class="info-content">{{ modifyData.content }}</div>
      </div>
      <div class="new-flame">
        <div class="info-title">New {{ modifyData.title }}</div>
        <input :type="modifyData.type" v-model.trim="inputInfo" />
      </div>
    </div>
    <div class="btn-flame">
      <div class="no-btn" @click="ClickBtn">Cancel</div>
      <div class="yes-btn" @click="ClickCheckBtn">
        Modify
        <i class="fa-solid fa-check"></i>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch } from "vue";
import { penClick, modifyData } from "@/components/UserPage.vue";
import { userMail } from "@/components/LoginPage.vue";
import { useRouter } from "vue-router";

export default {
  setup() {
    const inputInfo = ref("");
    const router = useRouter();
    const showSuccess = ref(false);
    const successMsg = ref("");

    const ClickBtn = () => {
      penClick.value = false;
    };

    const ClickCheckBtn = async () => {
      modifyData.value.content = inputInfo.value;

      const responseUser = await fetch("http://localhost:5000/api/modify", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: userMail.value,
          title: modifyData.value.title.toLowerCase(),
          value: modifyData.value.content,
        }),
      });

      if (modifyData.value.title === "name") {
        const responseLogin = await fetch(
          "http://localhost:5000/api/login/modify",
          {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              email: userMail.value,
              title: modifyData.value.title.toLowerCase(),
              value: modifyData.value.content,
            }),
          }
        );

        const result = await responseLogin.json();
        console.log("更新結果：", result);
      }

      const result = await responseUser.json();
      console.log("User更新結果：", result);

      successMsg.value = "Modify SuccessFully !";
      showSuccess.value = true;

      setTimeout(() => {
        router.go(0);
        showSuccess.value = false;
        penClick.value = false;
      }, 1000);
    };

    watch(modifyData);

    return {
      penClick,
      modifyData,
      userMail,
      inputInfo,
      showSuccess,
      successMsg,
      ClickBtn,
      ClickCheckBtn,
    };
  },
};
</script>

<style scoped>
.modify-page {
  background-color: #ffffff;
  box-shadow: 0px 0px 5px 3px #d0d0d0;
  padding: 30px;
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
  position: absolute;
  bottom: 30px;
  left: 5%;
  background-color: #a6ffa6;
  color: #00db00;
  padding: 20px;
  text-align: center;
  font-size: 18px;
}
.container {
  width: 90%;
}
.flame {
  margin: 20px 0;
  border-bottom: 1px solid #adadad;
}
.new-flame {
  margin: 20px 0;
}
.info-title {
  font-size: 18px;
  text-align: left;
}
.info-content {
  font-size: 22px;
  color: #adadad;
  margin-top: 20px;
  margin-bottom: 10px;
}
input {
  width: 100%;
  padding-top: 20px;
  padding-bottom: 10px;
  text-align: center;
  font-size: 22px;
  color: #adadad;
  border: none;
  border-bottom: 1px solid #adadad;
}
input:focus {
  outline: none;
  border-bottom: 2px solid #ff79bc;
}
.btn-flame {
  width: 90%;
  display: flex;
  justify-content: end;
  align-items: center;
}
.yes-btn,
.no-btn {
  background-color: #000000;
  color: #ffffff;
  width: 100px;
  height: 25px;
  line-height: 25px;
  padding: 5px;
  border-radius: 10px;
}
.yes-btn:hover {
  cursor: pointer;
  background-color: #ff79bc;
}
.no-btn {
  background-color: #ffd9ec;
  color: #ff79bc;
  margin-right: 20px;
}
.no-btn:hover {
  cursor: pointer;
  background-color: #ff79bc;
  color: #ffffff;
}
</style>
