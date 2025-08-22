<template>
  <div class="back-menu-page">
    <div class="menu">
      <router-link to="/list">
        <i class="fa-solid fa-file"></i>
      </router-link>
      <i class="fa-solid fa-thumbs-up"></i>
      <i class="fa-solid fa-comment"></i>
      <i class="fa-solid fa-arrow-left" id="arrow" @click="ClickArrow"></i>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { showNav } from "@/components/UserPage.vue";

export const showList = ref(false);

export default {
  setup() {
    const router = useRouter();

    const ClickArrow = () => {
      router.push("/user");
      showNav.value = true;
    };

    const ClickList = () => {
      showList.value = true;
      router.push("/list");
    };

    return {
      showNav,
      ClickArrow,
      ClickList,
    };
  },
};
</script>

<style scoped>
.back-menu-page {
  height: 100%;
  display: flex;
  justify-content: start;
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
</style>
