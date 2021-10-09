import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import routes from './routes'
import './assets/styles/tailwind.css' // Tailwind init
import './assets/styles/main.scss' // Custom global styles
import App from './App.vue'

const router = createRouter({
  history: createWebHistory(),
  routes,
})

createApp(App).use(router).mount('#app')
