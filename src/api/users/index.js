import request from '@/plugin/axios'

// 登录
var AccountLogin = function (data) {
  return request({
    url: '/api/auth/login/',
    method: 'post',
    data
  })
}

// 用户列表
var GetAllUser = function (data) {
  return request({
    url: '/api/v1/users/',
    method: 'get',
    params: data
  })
}

// 创建用户
var CreateUser = function (data) {
  return request({
    url: '/api/v1/users/',
    method: 'post',
    data
  })
}

// 删除用户
var DeleteUser = function (data) {
  return request({
    url: '/api/v1/users/' + data.id + '/',
    method: 'delete'
  })
}

// 更新用户
var UpdateUser = function (data) {
  return request({
    url: '/api/v1/users/' + data.id + '/',
    method: 'put',
    data
  })
}

export { AccountLogin, GetAllUser, CreateUser, DeleteUser, UpdateUser }
