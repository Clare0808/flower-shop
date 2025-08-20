<template>
  <div class="write-page">
    <div class="title">
      Write
      <span style="color: #ff79bc">Review</span>
    </div>
    <div class="error" v-if="showError">{{ errorMsg }}</div>
    <div class="success" v-if="showSuccess">{{ successMsg }}</div>
    <div class="container">
      <div class="flame">
        <div class="sec-title">Give us some star !</div>
        <div class="i-flame">
          <div v-for="i in 5" :key="i">
            <i
              class="fa-solid fa-star"
              @click="HandleStarNum(i)"
              @mouseenter="HandleStarNum(i)"
              :class="{ iClick: star[i - 1] }"
            ></i>
          </div>
        </div>
      </div>
      <div class="flame">
        <div class="sec-title">Write down your review.</div>
        <textarea type="text" v-model.trim="content"></textarea>
      </div>
      <div class="btn-flame">
        <div class="no-btn" @click="ClosePage">Cancel</div>
        <div class="yes-btn" @click="SendReview">Submit</div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { showWrite } from "@/components/ReviewPage.vue";
import { userName } from "@/components/LoginPage.vue";
import { userImage } from "@/components/UserPage.vue";

export default {
  name: "CartPage",
  setup() {
    const content = ref("");
    const starNum = ref(0);
    const reviewDate = ref("");
    const star = ref(Array(5).fill(false));
    const errorMsg = ref("");
    const showError = ref(false);
    const router = useRouter();
    const showSuccess = ref(false);
    const successMsg = ref("");

    const ClosePage = () => {
      showWrite.value = false;
      console.log(userImage.value);
    };

    const HandleStarNum = (index) => {
      starNum.value = index;

      HandleStarLight(index);
    };

    const HandleStarLight = (index) => {
      for (let i = 0; i < 5; i++) {
        star.value[i] = false;
      }

      for (let i = 0; i < index; i++) {
        star.value[i] = true;
      }
    };

    const HandleDate = () => {
      const date = new Date();

      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const day = String(date.getDate()).padStart(2, "0");

      reviewDate.value = `${year}-${month}-${day}`;
    };

    const SendReview = async () => {
      HandleDate();

      CheckContent();

      if (!showError.value) {
        const response = await fetch("http://localhost:5000/api/storereview", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            name: userName.value,
            img: userImage.value,
            date: reviewDate.value,
            score: starNum.value,
            content: content.value,
          }),
        });

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        successMsg.value = "Add review successfully !";
        showSuccess.value = true;

        setTimeout(() => {
          ClosePage();
          router.go(0);
        }, 1000);
      }
    };

    const CheckContent = () => {
      if (starNum.value === 0) {
        errorMsg.value = "Please give us some star !";
        showError.value = true;
      } else if (content.value === "") {
        errorMsg.value = "Please write something !";
        showError.value = true;
      } else {
        showError.value = false;
      }

      setTimeout(() => {
        showError.value = false;
      }, 2000);
    };

    return {
      userName,
      userImage,
      showWrite,
      content,
      starNum,
      reviewDate,
      star,
      errorMsg,
      showError,
      showSuccess,
      successMsg,
      ClosePage,
      HandleStarNum,
      HandleStarLight,
      HandleDate,
      SendReview,
      CheckContent,
    };
  },
};
</script>

<style scoped>
.write-page {
  background-color: #ffffff;
  box-shadow: 0px 0px 5px 3px #d0d0d0;
  padding: 30px;
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
  position: absolute;
  right: 5%;
  top: 80px;
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
  width: 100%;
  margin-top: 20px;
}
.sec-title {
  font-size: 18px;
  color: #000000;
  text-align: left;
}
.i-flame {
  margin-top: 10px;
  display: flex;
  justify-content: start;
  align-items: center;
}
i {
  color: #ffd9ec;
  font-size: 22px;
  margin-right: 20px;
}
i:hover {
  color: #ff79bc;
  cursor: pointer;
}
.iClick {
  color: #ff79bc;
  cursor: pointer;
}
textarea {
  width: calc(100% - 20px);
  margin-top: 10px;
  height: 150px;
  padding: 10px;
  border-radius: 10px;
  border: 1px solid #adadad;
}
textarea:focus {
  outline: none;
  border: 1px solid #ff79bc;
}
.btn-flame {
  margin-top: 30px;
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
