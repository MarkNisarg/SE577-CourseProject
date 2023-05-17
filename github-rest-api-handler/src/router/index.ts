import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../pages/HomePage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../pages/AboutPage.vue')
    },
    {
      path: '/repositories',
      name: 'repositories',
      component: () => import('../pages/RepositoriesPage.vue')
    },
    {
      path: '/pull',
      name: 'requests',
      component: () => import('../pages/PullRequestsPage.vue')
    },
  ]
})

export default router
