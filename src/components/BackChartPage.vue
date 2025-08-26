<template>
  <div class="chart-page">
    <div class="title">Data Analysis</div>
    <div class="container">
      <div class="flame">
        <div class="data-flame">
          <div class="sec-title">Products Sales</div>
          <canvas ref="productCanvas"></canvas>
        </div>
        <div class="data-flame">
          <div class="sec-title">Customers Evaluate</div>
          <canvas ref="starCanvas"></canvas>
        </div>
      </div>
      <div class="sale-data-flame">
        <div class="sec-title">Customers Evaluate</div>
        <canvas ref="saleCanvas"></canvas>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables); // 註冊 Chart.js

export default {
  name: "BackChartPage",
  setup() {
    const starCanvas = ref(null);
    const scoreData = ref(Array(5).fill(0));
    const productCanvas = ref(null);
    const productData = ref({
      "Product 1": 0,
      "Product 2": 0,
      "Product 3": 0,
      "Product 4": 0,
      "Product 5": 0,
      "Product 6": 0,
    });
    const saleData = ref(Array(12).fill(0));
    const saleCanvas = ref(null);

    const GetReviewScore = async () => {
      const response = await fetch("http://localhost:5000/api/getreview");
      const data = await response.json();

      const filterData = data.data.map((item) => item.score);

      for (let i = 0; i < filterData.length; i++) {
        scoreData.value[filterData[i] - 1] += 1;
      }
    };

    const GetProductData = async () => {
      const response = await fetch("http://localhost:5000/api/getbuy");
      const data = await response.json();

      const rawData = data.data;

      for (const item of rawData) {
        const name = item.product;
        const qty = parseInt(item.quantity);

        if (!productData.value[name]) {
          productData.value[name] = 0;
        }

        productData.value[name] += qty;
      }
    };

    const GetSaleData = async () => {
      const response = await fetch("http://localhost:5000/api/getbuy");
      const data = await response.json();

      const filterData = data.data.map((item) => item.date);

      for (let i = 0; i < filterData.length; i++) {
        const monthStr = filterData[i].split("-")[1];
        const monthNum = parseInt(monthStr);

        saleData.value[monthNum - 1] += 1;
      }
    };

    onMounted(async () => {
      await GetReviewScore();
      new Chart(starCanvas.value, {
        type: "bar",
        data: {
          labels: ["1", "2", "3", "4", "5"],
          datasets: [
            {
              label: "Stars",
              data: scoreData.value,
              backgroundColor: "#ffd9ec",
            },
          ],
        },
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true,
              ticks: {
                stepSize: 1, // 每格間距為 1，確保都是整數
              },
            },
          },
        },
      });

      await GetProductData();

      const labels = Object.keys(productData.value);
      const data = Object.values(productData.value);

      new Chart(productCanvas.value, {
        type: "bar",
        data: {
          labels: labels,
          datasets: [
            {
              label: "Products",
              data: data,
              borderColor: "#ff79bc",
              backgroundColor: "#ffd9ec",
            },
          ],
        },
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true,
              ticks: {
                stepSize: 1, // 每格間距為 1，確保都是整數
              },
            },
          },
        },
      });

      await GetSaleData();
      new Chart(saleCanvas.value, {
        type: "line",
        data: {
          labels: [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
          ],
          datasets: [
            {
              label: "Sales",
              data: saleData.value,
              backgroundColor: "#ffd9ec",
              borderColor: "#ff79bc",
            },
          ],
        },
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true,
              ticks: {
                stepSize: 1, // 每格間距為 1，確保都是整數
              },
            },
          },
        },
      });
    });

    return {
      starCanvas,
      scoreData,
      productCanvas,
      productData,
      saleData,
      saleCanvas,
      GetReviewScore,
      GetProductData,
      GetSaleData,
    };
  },
};
</script>

<style scoped>
.chart-page {
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
  width: 100%;
  height: calc(92% - 20px);
  padding: 20px;
  display: grid;
  grid-template-columns: 100%;
  grid-template-rows: 50% 50%;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.flame {
  /*width: 100%;
  height: 35%;*/
  margin-bottom: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.data-flame {
  width: 45%;
  margin: 0 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.sec-title {
  font-size: 20px;
}
.sale-data-flame {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.sale-data-flame .sec-title {
  margin-right: 20px;
}
</style>
