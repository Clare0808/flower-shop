<template>
  <div class="back-page">
    <div class="menu">
      <router-link to="/backlist">
        <i class="fa-solid fa-file"></i>
      </router-link>
      <router-link to="/backreview">
        <i class="fa-solid fa-thumbs-up"></i>
      </router-link>
      <router-link to="/backcomment">
        <i class="fa-solid fa-comment"></i>
      </router-link>
      <i class="fa-solid fa-arrow-left" id="arrow" @click="ClickArrow"></i>
    </div>
    <div class="son-page">
      <router-view />
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import { showNav } from "@/components/UserPage.vue";

export default {
  name: "BackPage",
  setup() {
    const router = useRouter();

    const ClickArrow = () => {
      router.push("/user");

      showNav.value = true;
      localStorage.setItem("showNav", showNav.value);
    };

    return {
      showNav,
      ClickArrow,
    };
  },
};
</script>

<style scoped>
.back-page {
  background-color: #ffd9ec;
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.menu {
  width: 50px;
  height: 85%;
  background-color: #ffffff;
  border-radius: 10px;
  margin-left: 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
}
i {
  color: #ffd9ec;
  font-size: 22px;
  margin: 10px 0;
}
i:hover {
  color: #ff79bc;
}
#arrow {
  position: absolute;
  bottom: 20px;
}
.son-page {
  width: 100%;
  height: 95%;
  margin: 0 30px;
}
</style>
