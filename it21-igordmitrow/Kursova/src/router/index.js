import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../components/HomeComponent.vue'
// import PlaylistView from '../components/PlaylistComponent.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/:position?',
      name: 'home',
      component: HomeView
    },
    {
      path: '/playlist',
      name: 'playlist',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../components/PlaylistComponent.vue')
    },
    {
      path: '/search',
      name: 'search',
      component: () => import('../components/SearchComponent.vue')
    }
  ]
})

export default router
