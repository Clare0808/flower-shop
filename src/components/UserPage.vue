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
        <div v-for="(d, index) in data" :key="index">
          <div class="info">
            <div class="info-title">{{ d.title }}</div>
            <div class="detail-info">
              <div class="info-content">{{ d.content }}</div>
              <i
                class="fa-solid fa-pencil"
                id="pen"
                @click="ModifyInfo(index)"
              ></i>
            </div>
          </div>
        </div>
      </div>
      <div class="btn" @click="ClickBtn">
        Logout
        <i class="fa-solid fa-arrow-right-from-bracket"></i>
      </div>
    </div>

    <ModifyPage class="modify-page" v-if="penClick" />
  </div>
</template>

<script>
import { ref, onMounted, watch } from "vue";
import { useRouter } from "vue-router";
import { userMail, userName, loginStatus } from "@/components/LoginPage.vue";
import ModifyPage from "@/components/ModifyPage.vue";

export const penClick = ref(false);
export const modifyData = ref({});

export default {
  name: "UserPage",
  components: {
    ModifyPage,
  },
  setup() {
    const router = useRouter();
    const data = ref([
      {
        id: 1,
        type: "text",
        title: "Name",
        content: userName.value,
      },
      {
        id: 2,
        type: "date",
        title: "Birthday",
        content: "None",
      },
      {
        id: 3,
        type: "text",
        title: "Email",
        content: userMail.value,
      },
      {
        id: 4,
        type: "number",
        title: "Number",
        content: "None",
      },
    ]);

    const ClickBtn = () => {
      loginStatus.value = false;

      localStorage.removeItem("userMail");
      localStorage.removeItem("userName");

      router.push("/login");
    };

    const ModifyInfo = (index) => {
      penClick.value = true;

      modifyData.value = {
        index: index,
        type: data.value[index].type,
        title: data.value[index].title,
        content: data.value[index].content,
      };
    };

    watch(penClick);
    watch(modifyData, (newValue) => {
      data.value[newValue.index].content = newValue.content;
    });

    onMounted(() => {
      userMail.value = localStorage.getItem("userMail");
      userName.value = localStorage.getItem("userName");
    });

    return {
      userMail,
      userName,
      loginStatus,
      penClick,
      modifyData,
      data,
      ClickBtn,
      ModifyInfo,
    };
  },
};
</script>

<style scoped>
.user-page {
  margin-top: 50px;
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
.container {
  width: 90%;
  padding: 50px;
  display: grid;
  grid-template-columns: 35% 60%;
  grid-template-rows: 100%;
  gap: 20px;
  justify-content: center;
  align-items: center;
  position: relative;
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
.detail-info {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  color: #adadad;
}
#pen {
  position: absolute;
  bottom: 5px;
  right: 0;
}
#pen:hover {
  color: #ff79bc;
  cursor: pointer;
}
.info-content {
  font-size: 22px;
  text-align: center;
  margin-top: 20px;
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
  position: absolute;
  right: 70px;
  bottom: -15px;
}
.btn:hover {
  background-color: #ff79bc;
  cursor: pointer;
}

.modify-page {
  width: 40%;
  position: absolute;
  top: 25%;
  z-index: 2;
}
</style>
