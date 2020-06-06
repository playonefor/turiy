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

// 查看权限以外的用户
var GetPermOutUser = function (data) {
  return request({
    url: '/api/v1/permisson/' + data.id + '/getusers_out/',
    method: 'get'
  })
}

// 查看权限以外的用户组
var GetPermOutGroup = function (data) {
  return request({
    url: '/api/v1/permisson/' + data.id + '/getgroups_out/',
    method: 'get'
  })
}

// 查看权限以外的应用
var GetPermOutApp = function (data) {
  return request({
    url: '/api/v1/permisson/' + data.id + '/getapps_out/',
    method: 'get'
  })
}

// 查看权限信息
var GetPerm = function (data) {
  return request({
    url: '/api/v1/permisson/' + data.id + '/',
    method: 'get'
  })
}

// 更新权限
var UpdatePerm = function (data) {
  return request({
    url: '/api/v1/permisson/' + data.id + '/',
    method: 'put',
    data: data
  })
}
// 删除权限
var DeletePerm = function (data) {
  return request({
    url: '/api/v1/permisson/' + data.id + '/',
    method: 'delete'
  })
}

export { GetAllPerm, GetPerms, GetUsers, GetApps, GettGgroups, CreatePerm, GetPermOutUser, GetPermOutApp, GetPermOutGroup, GetPerm, UpdatePerm, DeletePerm }
