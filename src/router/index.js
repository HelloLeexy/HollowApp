import { h, resolveComponent } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'

import DefaultLayout from '@/layouts/DefaultLayout'

// 提取出的 Login 路由配置

const routes = [
  {
    path: '/',
    name: 'Home',
    component: DefaultLayout,
    redirect: '/Login',

    children: [
      {
        path: '/dashboard',
        name: 'Dashboard',
        component: () => import('@/views/Home/index.vue'),
      },
      {
        path: '/follow',
        name: 'follow',
        component: () => import('@/views/Follow/index.vue'),
      },
      {
        path: '/post',
        name: 'post',
        component: () => import('@/views/Theme/index.vue'),
      },
      {
        path: '/account',
        name: 'account',
        component: () => import('@/views/Account/index.vue'),
      },
      {
        path: '/contact',
        name: 'contact',
        component: () => import('@/views/Theme/Typography.vue'),
      },
    ],
  },
  {
    path: '/Login',
    name: 'Login',
    component: () => import('@/views/pages/Login.vue'),
  },
  {
    path: '/info',
    name: 'info',
    component: () => import('@/views/pages/index.vue'),
  },
  {
    path: '/createAccount',
    name: 'createAccount',
    component: () => import('@/views/pages/create-account.vue'),
  },
  {
    path: '/selectCourse',
    name: 'selectCourse',
    component: () => import('@/views/pages/select-Course.vue'),
  },
  {
    path: '/itgroup-dashboard',
    name: 'itgroup-dashboard',
    component: () => import('@/views/Admin/index.vue'),
  },
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes,
  scrollBehavior() {
    // always scroll to top
    return { top: 0 }
  },
})

export default router
