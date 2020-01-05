import Vue from 'vue'
import Router from 'vue-router'
import GameMode from './components/GameMode.vue'
import Classic from './components/Classic.vue'
import Categories from './components/Categories.vue'
import AddCard from './components/AddCard.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/game',
      name: 'Game',
      component: GameMode
    },
    {
      path: '/classic',
      name: 'Classic',
      component: Classic,
      props: true
    },
    {
      path: '/categories',
      name: 'Categories',
      component: Categories
    },
    {
      path: '/addcard',
      name: 'AddCard',
      component: AddCard
    }
  ]
})
