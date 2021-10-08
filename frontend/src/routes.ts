import Home from './pages/Home.vue'
import About from './pages/About.vue'

// 2. Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
export default [
  { path: '/', component: Home },
  { path: '/about', component: About },
]
