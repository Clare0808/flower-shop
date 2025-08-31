<template>
  <div class="home">
    <transition name="fade">
      <div class="container" v-if="showPage">
        <div class="title">Fresh Flowers</div>
        <div class="sec-title">Natural & Beautiful Flowers</div>
        <div class="description">
          Rose, Tulip, are native to Central Asia, Carnation, Known to symbolise
          love and deep fascination, Lily, Daisy, a great symbol of happiness,
          Camellia, symbolise love and affection...
        </div>
        <div class="btn" @click="ClickBtn">Shop Now</div>
      </div>
    </transition>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "HomeView",
  setup() {
    const router = useRouter();
    const showPage = ref(false);

    const ClickBtn = () => {
      router.push("/products");
    };

    onMounted(() => {
      showPage.value = true;
    });

    return {
      showPage,
      ClickBtn,
    };
  },
};
</script>

<style scoped>
.home {
  width: 100%;
  height: 100%;
  background-image: url("@/assets/background.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: right bottom;
  position: absolute;
  top: 0;
  left: 0;
}
.container {
  padding-top: 200px;
  padding-left: 100px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
}
.title {
  font-size: 50px;
  font-weight: bold;
  margin-bottom: 10px;
}
.sec-title {
  font-size: 35px;
  color: #ff79bc;
  margin-bottom: 10px;
}
.description {
  width: 450px;
  font-size: 20px;
  text-align: start;
  margin-bottom: 20px;
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
  transition: all 0.3s ease;
}
.btn:hover {
  background-color: #ff79bc;
  cursor: pointer;
  transform: scale(1.1);
}

@media (max-width: 625px) {
  .container {
    padding-top: 150px;
    padding-left: 50px;
  }
  .title {
    font-size: 40px;
  }
  .sec-title {
    font-size: 25px;
  }
  .description {
    width: 300px;
    font-size: 15px;
  }
  .btn {
    width: 80px;
    height: 20px;
    line-height: 20px;
    font-size: 15px;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: all 1s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(100px);
}
.fade-enter-to,
.fade-leave-from {
  opacity: 1;
  transform: translateY(0);
}
</style>
