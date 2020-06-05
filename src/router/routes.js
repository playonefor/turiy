import layoutHeaderAside from '@/layout/header-aside'

// 由于懒加载页面太多的话会造成webpack热更新太慢，所以开发环境不使用懒加载，只有生产环境使用懒加载
const _import = require('@/libs/util.import.' + process.env.NODE_ENV)

/**
 * 在主框架内显示
 */
const frameIn = [
  {
    path: '/',
    redirect: { name: 'index' },
    component: layoutHeaderAside,
    children: [
      // 首页
      {
        path: 'index',
        name: 'index',
        meta: {
          auth: true
        },
        component: _import('system/index')
      },
      {
        path: 'userlist',
        name: 'userlist',
        meta: {
          title: '用户列表',
          auth: true
        },
        component: _import('users/userlist')
      },
      {
        path: 'usergroup',
        name: 'usergroup',
        meta: {
          title: '用户组',
          auth: true
        },
        component: _import('users/usergroup')
      },
      {
        path: 'usergroup/groupdetail/:groupid',
        name: 'groupdetail',
        meta: {
          title: '用户组详情',
          auth: true
        },
        props: true,
        component: _import('users/usergroup/components/PageDetail')
      },
      {
        path: 'usergroup/creategroup',
        name: 'creategroup',
        meta: {
          title: '新增用户组',
          auth: true
        },
        component: _import('users/usergroup/components/PageCreate')
      },
      {
        path: 'permlist',
        name: 'permslist',
        meta: {
          title: '权限列表',
          auth: true
        },
        component: _import('perms/permlist')
      },
      {
        path: 'permlist/permcreate',
        name: 'createperm',
        meta: {
          title: '新增权限',
          auth: true
        },
        component: _import('perms/components/PageCreate')
      },
      {
        path: 'perms/update/:id',
        name: 'permedit',
        meta: {
          title: '权限编辑',
          auth: true
        },
        props: true,
        component: _import('perms/components/PageUpdate.vue')
      },
      {
        path: 'applist',
        name: 'applist',
        meta: {
          title: '应用列表',
          auth: true
        },
        component: _import('apps/applist')
      },
      // 系统 前端日志
      /**
      {
        path: 'log',
        name: 'log',
        meta: {
          title: '前端日志',
          auth: true
        },
        component: _import('system/log')
      },
      */
      // 刷新页面 必须保留
      {
        path: 'refresh',
        name: 'refresh',
        hidden: true,
        component: _import('system/function/refresh')
      },
      // 页面重定向 必须保留
      {
        path: 'redirect/:route*',
        name: 'redirect',
        hidden: true,
        component: _import('system/function/redirect')
      }
    ]
  }
]

/**
 * 在主框架之外显示
 */
const frameOut = [
  // 登录
  {
    path: '/login',
    name: 'login',
    component: _import('system/login')
  }
]

/**
 * 错误页面
 */
const errorPage = [
  {
    path: '*',
    name: '404',
    component: _import('system/error/404')
  }
]

// 导出需要显示菜单的
export const frameInRoutes = frameIn

// 重新组织后导出
export default [
  ...frameIn,
  ...frameOut,
  ...errorPage
]
