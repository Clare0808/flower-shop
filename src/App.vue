<template>
  <nav>
    <div class="mark">
      <i class="fa-solid fa-seedling"></i>
      Flower
    </div>
    <div class="text-flame">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/products">Products</router-link>
      <router-link to="/review">Review</router-link>
      <router-link to="/contact">Contact</router-link>
    </div>
    <div class="icon-flame">
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
