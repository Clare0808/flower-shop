<template>
  <div class="comment-page">
    <div class="title">Customers Review</div>
    <div class="container">
      <div class="flame" v-for="i in 10" :key="i">
        <div class="comment">
          <div class="text">User 1</div>
          <div class="text">2023/08/08</div>
          <div class="text">1223456@gmail.com</div>
          <div class="text">0912345678</div>
          <div class="text-de">
            Rose, Tulip, are native to Central Asia, Carnation, Known to
            symbolise love and deep fascination, Lily, Daisy, a great symbol of
            happiness, Camellia, symbolise love and affection...
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.comment-page {
  height: calc(100% - 40px);
  background-color: #ffffff;
  border-radius: 10px;
  padding: 20px;
}
.title {
  font-size: 30px;
  color: #ff79bc;
  padding-bottom: 10px;
  margin-bottom: 10px;
  border-bottom: 2px solid #ff79bc;
}
.container {
  max-height: 92%;
  overflow-y: auto;
}
.flame {
  display: flex;
  justify-content: center;
  align-items: center;
}
.comment {
  width: 95%;
  margin: 10px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.text {
  font-size: 20px;
}
.text-de {
  font-size: 18px;
  color: #adadad;
  text-align: left;
  width: 40%;
}
</style>
