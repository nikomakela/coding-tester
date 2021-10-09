import Home from './pages/Home.vue'
import About from './pages/About.vue'

export const assignmentsAvailable = ['fibonacci', 'sananmuunnos']

const assignmentsPaths = assignmentsAvailable.map((ass) => {
  return { path: `/${ass}`, component: Home }
})

export default [
  { path: '/', component: Home },
  { path: '/about', component: About },
].concat(assignmentsPaths)
