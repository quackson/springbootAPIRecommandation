// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import router from './router'
import axios from 'axios'
import {Message} from 'element-ui'
import ECharts from "vue-echarts"
import "echarts"
import 'highlight.js/styles/default.css'

// Vue.config.productionTip = false;
Vue.use(ElementUI);
Vue.prototype.$http = axios
Vue.prototype.$url = 'http://127.0.0.1'
Vue.prototype.$message=Message
Vue.component('chart',ECharts)




new Vue({
	el: '#app',
	render: h => h(App),
	router
});
