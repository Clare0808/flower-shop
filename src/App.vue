<template>
  <nav v-if="showNav">
    <div class="mark">
      <i class="fa-solid fa-seedling"></i>
      Flower
    </div>
    <div class="text-flame" v-if="loginStatus">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/products">Products</router-link>
      <router-link to="/review">Review</router-link>
      <router-link to="/contact">Contact</router-link>
    </div>
    <div class="icon-flame" v-if="loginStatus">
      <router-link to="/like">
        <i class="fa-solid fa-heart"></i>
      </router-link>
      <router-link to="/cart">
        <i class="fa-solid fa-cart-shopping"></i>
      </router-link>
      <router-link to="/user">
        <i class="fa-solid fa-user"></i>
      </router-link>
    </div>
  </nav>
  <router-view />
</template>

<script>
import { onMounted, computed, watch } from "vue";
import { useRoute } from "vue-router";
import { userMail, userName, loginStatus } from "@/components/LoginPage.vue";
import { showNav } from "@/components/UserPage.vue";

export default {
  setup() {
    const route = useRoute();

    const isBackPage = computed(() => route.path.includes("back"));

    watch(isBackPage, (newValue) => {
      if (newValue) {
        showNav.value = false;
      } else {
        showNav.value = true;
      }
    });

    onMounted(() => {
      const storeMail = localStorage.getItem("userMail");
      const storeName = localStorage.getItem("userName");

      if (storeMail && storeName) {
        userMail.value = storeMail;
        userName.value = storeName;

        loginStatus.value = true;
      } else {
        loginStatus.value = false;
      }
    });

    return {
      userMail,
      userName,
      loginStatus,
      showNav,
    };
  },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body {
  margin: 0;
  padding: 0;
  width: 100vw;
  height: 100vh;
  overflow-x: hidden;
}
nav {
  background-color: #ffffff;
  padding: 10px 20px;
  box-shadow: 5px 5px 5px 5px #0005;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  z-index: 2;
}
nav a {
  text-decoration: none;
  font-size: 20px;
}
nav a:hover {
  color: #ff79bc;
}
nav a:focus {
  color: #ff79bc;
}
.mark i {
  color: #79ff79;
}
.mark {
  font-size: 30px;
  font-weight: bold;
}
.text-flame a {
  color: #adadad;
  margin: 0 10px;
}
.icon-flame a {
  color: #000000;
  margin: 0 5px;
}
</style>
