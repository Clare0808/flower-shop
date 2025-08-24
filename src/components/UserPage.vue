<template>
  <div class="user-page">
    <div class="title">
      <span style="color: #ff79bc">User</span>
      Information
    </div>
    <div class="container">
      <div class="img-flame">
        <img :src="userImage" />
        <i class="fa-solid fa-pencil" id="img-pen" @click="TriggleFileInput">
          <input
            type="file"
            accept="image/*"
            @change="UploadImage"
            ref="fileInput"
            style="display: none"
          />
        </i>
      </div>
      <div class="text-flame">
        <div v-for="(d, index) in userData" :key="index">
          <div class="info">
            <div class="info-title">{{ d.title }}</div>
            <div class="detail-info">
              <div class="info-content">{{ d.content }}</div>
              <i
                class="fa-solid fa-pencil"
                id="pen"
                v-if="d.title !== 'Email'"
                @click="ModifyInfo(index)"
              ></i>
            </div>
          </div>
        </div>
      </div>
      <div class="btn-flame">
        <div class="manage-btn" @click="ClickManage">Manage</div>
        <div class="btn" @click="ClickBtn">
          Logout
          <i class="fa-solid fa-arrow-right-from-bracket"></i>
        </div>
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
export const userImage = ref("");
export const showNav = ref(true);

export default {
  name: "UserPage",
  components: {
    ModifyPage,
  },
  setup() {
    const router = useRouter();
    const userData = ref([]);
    const fileInput = ref(null);
    const userImage = ref("");

    const ClickBtn = () => {
      loginStatus.value = false;

      localStorage.removeItem("userMail");
      localStorage.removeItem("userName");

      router.push("/login");
    };

    const ClickManage = () => {
      router.push("/back");

      showNav.value = false;
      localStorage.setItem("showNav", showNav.value);
    };

    const ModifyInfo = (index) => {
      penClick.value = true;

      modifyData.value = {
        index: index,
        type: userData.value[index].type,
        title: userData.value[index].title,
        content: userData.value[index].content,
      };
    };

    const GetUserInfo = async () => {
      const response = await fetch("http://localhost:5000/api/info");
      const data = await response.json();
      console.log(data);

      const filterData = data.data.find(
        (item) => item.email === userMail.value
      );

      userData.value = [
        {
          id: 1,
          type: "text",
          title: "Name",
          content: filterData.name,
        },
        {
          id: 2,
          type: "date",
          title: "Birthday",
          content: filterData.birthday,
        },
        {
          id: 3,
          type: "text",
          title: "Email",
          content: filterData.email,
        },
        {
          id: 4,
          type: "number",
          title: "Number",
          content: filterData.number,
        },
      ];

      userImage.value = `/assets/users/${filterData.img}`;
    };

    const UploadImage = async (event) => {
      const file = event.target.files[0];

      const reader = new FileReader();
      reader.onload = () => {
        userImage.value = reader.result;
      };
      reader.readAsDataURL(file);

      const formData = new FormData();
      formData.append("image", file);
      formData.append("title", userMail.value);

      const response = await fetch("http://localhost:5000/api/upload", {
        method: "POST",
        body: formData,
      });

      const result = await response.json(); // ✅ 解析 JSON
      console.log("re", result.newName);

      const responseModify = await fetch("http://localhost:5000/api/modify", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: userMail.value,
          title: "img",
          value: result.newName,
        }),
      });

      const resultM = await responseModify.json();
      console.log("m", resultM);

      userImage.value = `/assets/users/${result.newName}`;
    };

    const TriggleFileInput = () => {
      fileInput.value.click();
    };

    watch(penClick);
    watch(modifyData, async (newValue) => {
      userData.value[newValue.index].content = newValue.content;
    });

    /*const HandleImage = computed(() => {
      try {
        return require(`@/assets/users/${userMail.value}.jpg`);
      } catch (e) {
        return require("@/assets/users/user.jpg");
      }
    });*/

    onMounted(async () => {
      userMail.value = localStorage.getItem("userMail");
      userName.value = localStorage.getItem("userName");

      await GetUserInfo();
    });

    return {
      userMail,
      userName,
      loginStatus,
      penClick,
      modifyData,
      userData,
      userImage,
      fileInput,
      ClickBtn,
      ClickManage,
      ModifyInfo,
      GetUserInfo,
      UploadImage,
      TriggleFileInput,
      // HandleImage,
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
  position: relative;
}
img {
  width: 80%;
  box-shadow: 0px 0px 5px 3px #d0d0d0;
}
#img-pen {
  width: 30px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  background-color: #ffffff;
  border-radius: 50%;
  position: absolute;
  bottom: 3%;
  right: 13%;
  z-index: 2;
}
#img-pen:hover {
  color: #ffffff;
  background-color: #ff79bc;
  cursor: pointer;
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
.btn-flame {
  display: flex;
  justify-content: center;
  position: absolute;
  right: 70px;
  bottom: -15px;
}
.manage-btn {
  width: 100px;
  height: 25px;
  background-color: #ffd9ec;
  color: #ff79bc;
  text-align: center;
  line-height: 25px;
  padding: 5px;
  border-radius: 10px;
  margin: 0 20px;
}
.manage-btn:hover {
  background-color: #ff79bc;
  color: #ffffff;
  cursor: pointer;
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

.modify-page {
  width: 40%;
  position: absolute;
  top: 25%;
  z-index: 2;
}
</style>
