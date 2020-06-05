import request from '@/plugin/axios'

// 获取所有权限
var GetAllPerm = function (data) {
  return request({
    url: '/api/v1/permisson/getall/',
    method: 'get',
    params: data
  })
}

// 获取所有用户
var GetUsers = function () {
  return request({
    url: '/api/v1/permisson/getusers/',
    method: 'get'
  })
}

// 获取所有应用
var GetApps = function () {
  return request({
    url: '/api/v1/permisson/getapps/',
    method: 'get'
  })
}

// 获取所有的用户组
var GettGgroups = function () {
  return request({
    url: '/api/v1/permisson/getgroups/',
    method: 'get'
  })
}

// 获取权限列表
var GetPerms = function (data) {
  return request({
    url: '/api/v1/permisson/',
    method: 'get',
    params: data
  })
}

// 创建权限
var CreatePerm = function (data) {
  return request({
    url: '/api/v1/permisson/',
    method: 'post',
    data: data
  })
}

export { GetAllPerm, GetPerms, GetUsers, GetApps, GettGgroups, CreatePerm }
