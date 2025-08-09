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
      <router-link to="/buyCar">
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
}
nav {
  padding: 10px 20px;
  box-shadow: 0 2px 2px 2px #d0d0d0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
nav a {
  text-decoration: none;
}
.mark i {
  color: #79ff79;
}
.mark {
  font-size: 30px;
  font-weight: bold;
}
.text-flame a {
  color: #d0d0d0;
  margin: 0 10px;
}
.icon-flame a {
  color: #000000;
  margin: 0 5px;
}
</style>
