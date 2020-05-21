import { uniqueId } from 'lodash'

/**
 * @description 给菜单数据补充上 path 字段
 * @description https://github.com/d2-projects/d2-admin/issues/209
 * @param {Array} menu 原始的菜单数据
 */
function supplementPath (menu) {
  return menu.map(e => ({
    ...e,
    path: e.path || uniqueId('d2-menu-empty-'),
    ...e.children ? {
      children: supplementPath(e.children)
    } : {}
  }))
}

export const menuHeader = supplementPath([
  { path: '/index', title: '首页', icon: 'home' },
  {
    title: '用户管理',
    icon: 'user-o',
    children: [
      // { path: '/page1', title: '页面 1' },
      // { path: '/page2', title: '页面 2' },
      // { path: '/page3', title: '页面 3' },
      { path: '/userlist', title: '用户列表', icon: 'user' },
      { path: '/usergroup', title: '用户组', icon: 'group' },
      { path: '/applist', title: '应用列表', icon: 'cubes' },
      { path: '/permgroup', title: '权限列表', icon: 'credit-card' }
    ]
  }
])

export const menuAside = supplementPath([
  { path: '/index', title: '首页', icon: 'home' },
  {
    title: '用户管理',
    icon: 'user-o',
    children: [
      // { path: '/page1', title: '页面 1' },
      // { path: '/page2', title: '页面 2' },
      // { path: '/page3', title: '页面 3' },
      { path: '/userlist', title: '用户列表', icon: 'user' },
      { path: '/usergroup', title: '用户组', icon: 'group' }
    ]
  },
  {
    title: '权限管理',
    icon: 'lock',
    children: [
      // { path: '/page1', title: '页面 1' },
      // { path: '/page2', title: '页面 2' },
      // { path: '/page3', title: '页面 3' },
      { path: '/permlist', title: '权限列表', icon: 'credit-card' }
    ]
  },
  {
    title: '应用管理',
    icon: 'cube',
    children: [
      // { path: '/page1', title: '页面 1' },
      // { path: '/page2', title: '页面 2' },
      // { path: '/page3', title: '页面 3' },
      { path: '/applist', title: '应用列表', icon: 'cubes' }
    ]
  }
])
