import './styles/tailwind.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueTailwind from 'vue-tailwind'
import CircularCountDownTimer from 'vue-circular-count-down-timer'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VueTailwind)
Vue.use(CircularCountDownTimer)

new Vue({
  render: h => h(App)
}).$mount('#app')
