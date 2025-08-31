<template>
  <nav v-if="showNav">
    <div class="mark">
      <i
        class="fa-solid fa-bars"
        id="menu"
        v-if="loginStatus"
        @click="ClickMenu"
      ></i>
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
  <transition name="slide">
    <div class="mobile-flame" v-if="showMenu">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/products">Products</router-link>
      <router-link to="/review">Review</router-link>
      <router-link to="/contact">Contact</router-link>
    </div>
  </transition>
  <router-view />
</template>

<script>
import { ref, onMounted, computed, watch } from "vue";
import { useRoute } from "vue-router";
import { userMail, userName, loginStatus } from "@/components/LoginPage.vue";
import { showNav } from "@/components/UserPage.vue";

export default {
  setup() {
    const route = useRoute();
    const isBackPage = computed(() => route.path.includes("back"));
    const showMenu = ref(false);

    const ClickMenu = () => {
      showMenu.value = !showMenu.value;
    };

    watch(isBackPage, (newValue) => {
      if (newValue) {
        showNav.value = false;
      } else {
        showNav.value = true;
      }
    });

    watch(route, () => {
      showMenu.value = false;
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
      showMenu,
      ClickMenu,
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
  transition: all 0.3s ease;
}
nav a:hover {
  color: #ff79bc;
}
nav a:focus {
  color: #ff79bc;
}
.mark i {
  color: #79ff79;
  margin-right: 5px;
}
.mark {
  font-size: 30px;
  font-weight: bold;
  display: flex;
  justify-content: center;
  align-items: center;
}
.text-flame a {
  color: #adadad;
  margin: 0 10px;
}
.icon-flame a {
  color: #000000;
  margin: 0 5px;
}
#menu {
  display: none;
  margin-right: 20px;
  font-size: 20px;
  color: #000000;
  cursor: pointer;
  transition: all 0.6s ease;
}
#menu:hover {
  color: #ffffff;
  background-color: #ff79bc;
  border-radius: 50%;
  padding: 5px;
  transform: rotate(180deg);
}
.mobile-flame {
  background-color: #ffd9ec;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
  z-index: 2;
}
.mobile-flame a {
  width: 90%;
  height: 25px;
  color: #adadad;
  font-size: 18px;
  line-height: 25px;
  text-align: left;
  text-decoration: none;
  background-color: #ffffff;
  border: 1px solid #adadad;
  border-radius: 10px;
  margin: 5px 0;
  padding: 5px;
}
.mobile-flame a:hover {
  border-color: #ff79bc;
}

@media (max-width: 750px) {
  #menu {
    display: block;
  }
  .text-flame {
    display: none;
  }
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.6s ease;
}
.slide-enter-from,
.slide-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}
.slide-enter-to,
.slide-leave-from {
  opacity: 1;
  transform: translateY(0);
}
</style>
