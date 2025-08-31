<template>
  <div class="about">
    <div class="title">
      About
      <span style="color: #ff79bc">Us</span>
    </div>
    <transition name="fade">
      <div class="container" v-if="showPage">
        <div class="img-flame">
          <img src="@/assets/about.jpg" />
          <div class="sec-title">Best Flower Sellers</div>
        </div>
        <div class="text-flame">
          <div class="third-title">Why Choose Us</div>
          <div class="description">
            Rose, Tulip, are native to Central Asia, Carnation, Known to
            symbolise love and deep fascination, Lily, Daisy, a great symbol of
            happiness, Camellia, symbolise love and affection... Rose, Tulip,
            are native to Central Asia, Carnation, Known to symbolise love and
            deep fascination, Lily, Daisy, a great symbol of happiness,
            Camellia, symbolise love and affection...
          </div>
          <div class="description">
            Rose, Tulip, are native to Central Asia, Carnation, Known to
            symbolise love and deep fascination, Lily, Daisy, a great symbol of
            happiness, Camellia, symbolise love and affection...
          </div>
          <div class="btn">Learn More</div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  name: "AboutView",
  setup() {
    const showPage = ref(false);

    onMounted(() => {
      showPage.value = true;
    });

    return {
      showPage,
    };
  },
};
</script>

<style scoped>
.about {
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
.container {
  width: 90%;
  padding: 50px;
  display: grid;
  grid-template-columns: 650px auto;
  grid-template-rows: 100%;
  gap: 20px;
  justify-content: center;
  align-items: center;
}
.img-flame {
  position: relative;
}
img {
  width: 100%;
}
.sec-title {
  width: 100%;
  font-size: 50px;
  font-weight: bold;
  padding: 5px;
  mix-blend-mode: screen;
  background-color: #ffffff;
  position: absolute;
  top: 40%;
}
.text-flame {
  width: 100%;
  height: 100%;
  text-align: start;
  padding-left: 20px;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: start;
}
.third-title {
  font-size: 40px;
  margin-bottom: 20px;
}
.description {
  margin-bottom: 10px;
  font-size: 20px;
  color: #adadad;
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
  margin-top: 10px;
  transition: all 0.3s ease;
}
.btn:hover {
  background-color: #ff79bc;
  cursor: pointer;
  transform: scale(1.1);
}

@media (max-width: 1115px) {
  .container {
    display: block;
  }
  .text-flame {
    padding-left: 0;
    margin-top: 20px;
  }
}
@media (max-width: 520px) {
  .container {
    padding: 20px;
  }
  .sec-title {
    font-size: 40px;
  }
  .third-title {
    font-size: 30px;
  }
  .description {
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
  transform: translateY(40px);
}
.fade-enter-to,
.fade-leave-from {
  opacity: 1;
  transform: translateY(0);
}
</style>
