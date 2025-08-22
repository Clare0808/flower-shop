import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProductPage from "@/components/ProductPage.vue";
import ReviewPage from "@/components/ReviewPage.vue";
import ContactPage from "@/components/ContactPage.vue";
import UserPage from "@/components/UserPage.vue";
import CartPage from "@/components/CartPage.vue";
import LikePage from "@/components/LikePage.vue";
import LoginPage from "@/components/LoginPage.vue";
import BackPage from "@/components/BackPage.vue";
import ListPage from "@/components/ListPage.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/products",
    name: "ProductPage",
    component: ProductPage,
  },
  {
    path: "/review",
    name: "ReviewPage",
    component: ReviewPage,
  },
  {
    path: "/contact",
    name: "ContactPage",
    component: ContactPage,
  },
  {
    path: "/user",
    name: "UserPage",
    component: UserPage,
  },
  {
    path: "/cart",
    name: "CartPage",
    component: CartPage,
  },
  {
    path: "/like",
    name: "LikePage",
    component: LikePage,
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/back",
    name: "BackPage",
    component: BackPage,
    children: [
      {
        path: "/list",
        name: "ListPage",
        component: ListPage,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
