import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
// import test from '@/components/test'
// import rate from '@/components/rate'
import ElementUI from 'element-ui'

Vue.use(Router)

export default new Router({
  /*routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ]*/
  routes: [
        {
            path: '/',
            redirect: '/firstpage'
        },
        
        {
            path: '/',
            component: () => import(/* webpackChunkName: "home" */ '../components/common/Home.vue'),
            meta: { title: '自述文件' },
            children: [
                {
                    path: '/dashboard',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/page/Dashboard.vue'),
                    meta: { title: '综合页面' }
                },
                {
                    path: '/codepage',
                    name: 'codepage',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/page/codepage.vue'),
                    meta: { title: '代码阅读页面' }
                },
                {
                    path: '/mappage',
                    name: 'mappage',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/page/mapPage.vue'),
                    meta: { title: '代码阅读页面' }
                },
				{
                  path: '/case',
				  name:'case',
                  component: () => import(/* webpackChunkName: "case" */ '../components/page/case.vue'),
                  meta: {title: '使用场景'}
                },
				{
                  path: '/help',
                  component: () => import(/* webpackChunkName: "search" */ '../components/page/PaperPage.vue'),
                  meta: {title: '帮助'}
                }
            ]
        },

        {
            path: '/firstpage',
            component: () => import(/* webpackChunkName: "firstpage" */ '../components/page/zhou_firstpage.vue'),
            meta: { title: '首页' }
        },
        {
            path: '/secondpage',
            component: () => import(/* webpackChunkName: "firstpage" */ '../components/page/zhou_secondpage.vue'),
            meta: { title: '首页' }
        },
        {
            path: '/hello',
            component: () => import(/* webpackChunkName: "login" */ '../components/HelloWorld.vue'),
            meta: { title: '测试' }
        }
        
    ]
})
