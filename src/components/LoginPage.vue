<template>
  <div class="login-page">
    <div class="title">Login</div>
    <div class="error" v-if="showError">{{ errorMsg }}</div>
    <div class="success" v-if="showSuccess">{{ successMsg }}</div>
    <div class="container" v-if="showLogin">
      <div class="flame">
        <div class="input-title">Email</div>
        <input type="text" v-model.trim="email" />
      </div>
      <div class="flame">
        <div class="input-title">Password</div>
        <input type="password" v-model.trim="password" />
      </div>
      <div class="btn-flame">
        <div class="login-btn" @click="HandleLogin">Login</div>
        <div class="sign-in-btn" @click="ShowSignInPage">Sing in</div>
      </div>
    </div>
    <div class="container" v-if="showSignIn">
      <div class="flame">
        <div class="input-title">Nmae</div>
        <input type="text" v-model.trim="name" />
      </div>
      <div class="flame">
        <div class="input-title">Email</div>
        <input type="text" v-model.trim="email" />
      </div>
      <div class="flame">
        <div class="input-title">Password</div>
        <input type="password" v-model.trim="password" />
      </div>
      <div class="flame">
        <div class="input-title">Confirm Password</div>
        <input type="password" v-model.trim="conPassword" />
      </div>
      <div class="btn-flame">
        <div class="login-btn" @click="HandleSignIn">Sign in</div>
        <div class="sign-in-btn" @click="ShowLoginPage">Login</div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";

export const userMail = ref("");
export const userName = ref("");
export const userImage = ref("");
export const loginStatus = ref(false);

export default {
  name: "LoginPage",
  setup() {
    const showLogin = ref(true);
    const showSignIn = ref(false);
    const name = ref("");
    const email = ref("");
    const password = ref("");
    const conPassword = ref("");
    const errorMsg = ref("");
    const showError = ref(false);
    const successMsg = ref("");
    const showSuccess = ref(false);
    const router = useRouter();

    const ShowLoginPage = () => {
      showLogin.value = true;
      showSignIn.value = false;

      showError.value = false;
      showSuccess.value = false;

      CleanInput();
    };

    const ShowSignInPage = () => {
      showLogin.value = false;
      showSignIn.value = true;

      showError.value = false;
      showSuccess.value = false;

      CleanInput();
    };

    const HandleSignIn = async () => {
      ValidInput("signin");

      await EmailCheck();

      if (!showError.value) {
        const signInResponse = await fetch("http://localhost:5000/api/signin", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            name: name.value,
            email: email.value,
            password: password.value,
          }),
        });

        if (!signInResponse.ok) {
          throw new Error("Network response was not ok");
        }

        const userResponse = await fetch("http://localhost:5000/api/user", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            name: name.value,
            email: email.value,
            birthday: "None",
            number: "None",
            img: "user.jpg",
          }),
        });

        if (!userResponse.ok) {
          throw new Error("Network response was not ok");
        }

        successMsg.value = "Sign in successful!";
        showSuccess.value = true;

        CleanInput();

        setTimeout(() => {
          ShowLoginPage();
        }, 1000);
      }
    };

    const HandleLogin = async () => {
      ValidInput("login");

      if (!showError.value) {
        const response = await fetch("http://localhost:5000/api/login");
        const data = await response.json();

        const filterData = data.data.find((item) => item.email === email.value);

        if (filterData) {
          if (filterData.password === password.value) {
            successMsg.value = "Login successful !";
            showSuccess.value = true;

            userMail.value = localStorage.setItem("userMail", filterData.email);
            userName.value = localStorage.setItem("userName", filterData.name);

            userMail.value = filterData.email;
            userName.value = filterData.name;

            loginStatus.value = true;

            CleanInput();

            setTimeout(() => {
              showSuccess.value = false;
              router.push("/");
            }, 1000);
          } else {
            errorMsg.value = "Email or password is incorrect !";
            showError.value = true;
          }
        } else {
          errorMsg.value = "Email not found !";
          showError.value = true;
        }
      }
    };

    const ValidInput = (type) => {
      if (type === "signin") {
        if (name.value === "") {
          errorMsg.value = "Name is required !";
          showError.value = true;
        } else if (email.value === "") {
          errorMsg.value = "Email is required !";
          showError.value = true;
        } else if (password.value === "") {
          errorMsg.value = "Password is required !";
          showError.value = true;
        } else if (conPassword.value === "") {
          errorMsg.value = "Please enter password again !";
          showError.value = true;
        } else if (password.value !== conPassword.value) {
          errorMsg.value = "Password does not match !";
          showError.value = true;
        } else {
          showError.value = false;
        }
      } else if (type === "login") {
        if (email.value === "") {
          errorMsg.value = "Please enter email !";
          showError.value = true;
        } else if (password.value === "") {
          errorMsg.value = "Please enter password !";
          showError.value = true;
        } else {
          showError.value = false;
        }
      }
    };

    const EmailCheck = async () => {
      const response = await fetch("http://localhost:5000/api/login");
      const data = await response.json();

      const filterEmail = data.data.map((item) => item.email);

      if (filterEmail.includes(email.value)) {
        errorMsg.value = "Email already exists !";
        showError.value = true;
      } else {
        showError.value = false;
      }
    };

    const CleanInput = () => {
      name.value = "";
      email.value = "";
      password.value = "";
      conPassword.value = "";
    };

    return {
      showLogin,
      showSignIn,
      name,
      email,
      password,
      conPassword,
      errorMsg,
      showError,
      successMsg,
      showSuccess,
      ShowLoginPage,
      ShowSignInPage,
      HandleSignIn,
      HandleLogin,
      ValidInput,
      EmailCheck,
      CleanInput,
    };
  },
};
</script>

<style scoped>
.login-page {
  margin-top: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
}
.title {
  font-size: 30px;
  background-color: #ffd9ec;
  width: 90%;
  padding: 2px;
}
.error {
  position: absolute;
  right: 5%;
  top: 80px;
  background-color: #ffb5b5;
  color: #ff2d2d;
  padding: 20px;
  text-align: center;
  font-size: 18px;
}
.success {
  position: absolute;
  right: 5%;
  top: 80px;
  background-color: #a6ffa6;
  color: #00db00;
  padding: 20px;
  text-align: center;
  font-size: 18px;
}
.container {
  width: 35%;
  margin-top: 50px;
  padding: 20px;
  box-shadow: 0px 0px 5px 3px #d0d0d0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.flame {
  width: 100%;
  margin: 10px 0;
}
.input-title {
  text-align: left;
  color: #adadad;
  font-size: 20px;
}
input {
  width: 100%;
  height: 25px;
  border-radius: 10px;
  border: 1px solid #adadad;
}
input:focus {
  outline: none;
  border: 1px solid #ff79bc;
}
.btn-flame {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}
.login-btn {
  width: 100px;
  height: 25px;
  background-color: #000000;
  color: #ffffff;
  text-align: center;
  line-height: 25px;
  padding: 5px;
  border-radius: 10px;
  margin: 0 20px;
}
.login-btn:hover {
  background-color: #ff79bc;
  cursor: pointer;
}
.sign-in-btn {
  width: 100px;
  height: 25px;
  background-color: #ffd9ec;
  color: #ff79bc;
  text-align: center;
  line-height: 25px;
  padding: 5px;
  border-radius: 10px;
  margin: 0 20px;
}
.sign-in-btn:hover {
  background-color: #ff79bc;
  color: #ffffff;
  cursor: pointer;
}
</style>
