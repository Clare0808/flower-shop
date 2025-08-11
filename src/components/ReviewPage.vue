<template>
  <div class="review">
    <div class="title">
      Customer's
      <span style="color: #ff79bc">Review</span>
    </div>
    <div class="flame">
      <div class="review-flame" v-for="(r, index) in reviewData" :key="index">
        <div class="star-flame">
          <div v-for="i in r.rating" :key="i">
            <i class="fa-solid fa-star"></i>
          </div>
        </div>
        <div class="content">{{ r.content }}</div>
        <div class="user-info">
          <img :src="r.img" />
          <div class="text-flame">
            <div class="name">{{ r.name }}</div>
            <div class="date">{{ r.date }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewPage",
  setup() {
    const reviewData = [
      {
        id: 1,
        name: "John Doe",
        date: "2023-10-01",
        content:
          "Rose, Tulip, are native to Central Asia, Carnation, Known to symbolise love and deep fascination, Lily, Daisy, a great symbol of happiness, Camellia, symbolise love and affection...Rose, Tulip, are native to Central Asia, Carnation, Known to symbolise love and deep fascination, Lily, Daisy, a great symbol of happiness, Camellia, symbolise love and affection...",
        img: require("@/assets/user1.jpg"),
        rating: 5,
      },
      {
        id: 2,
        name: "John Doe",
        date: "2023-10-01",
        content:
          "Rose, Tulip, are native to Central Asia, Carnation, Known to symbolise love and deep fascination, Lily, Daisy, a great symbol of happiness, Camellia, symbolise love and affection...Rose, Tulip, are native to Central Asia, Carnation, Known to symbolise love and deep fascination, Lily, Daisy, a great symbol of happiness, Camellia, symbolise love and affection...",
        img: require("@/assets/user2.jpg"),
        rating: 3,
      },
      {
        id: 3,
        name: "John Doe",
        date: "2023-10-01",
        content:
          "Rose, Tulip, are native to Central Asia, Carnation, Known to symbolise love and deep fascination, Lily, Daisy, a great symbol of happiness, Camellia, symbolise love and affection...Rose, Tulip, are native to Central Asia, Carnation, Known to symbolise love and deep fascination, Lily, Daisy, a great symbol of happiness, Camellia, symbolise love and affection...",
        img: require("@/assets/user3.jpg"),
        rating: 4,
      },
    ];

    return {
      reviewData,
    };
  },
};
</script>

<style scoped>
.review {
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
.flame {
  width: 90%;
  padding: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.review-flame {
  width: 35%;
  margin: 0 20px;
  padding: 20px;
  box-shadow: 0px 0px 5px 3px #d0d0d0;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: start;
}
.star-flame {
  display: flex;
  justify-content: center;
  align-items: start;
}
i {
  color: #ff79bc;
  font-size: 20px;
}
.content {
  color: #adadad;
  text-align: start;
  margin: 20px 0;
}
.user-info {
  display: flex;
  justify-content: center;
  align-items: center;
}
img {
  width: 50px;
  border-radius: 50%;
}
.text-flame {
  text-align: start;
  color: #adadad;
  margin-left: 20px;
}
.name {
  color: #000000;
  font-size: 25px;
}
</style>
