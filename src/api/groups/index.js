import request from '@/plugin/axios'

// 获取用户组
var GetAllGroup = function (data) {
  return request({
    url: '/api/v1/groups/',
    method: 'get',
    params: data
  })
}

// 获取用户详情页
var GetDetailGroup = function (data) {
  return request({
    url: '/api/v1/groups/' + data.id + '/',
    method: 'get'
  })
}

// 删除用户组成员
var DeleteUserGroup = function (data) {
  return request({
    url: '/api/v1/groups/' + data.gid + '/delete_user_group/',
    method: 'put',
    data: data
  })
}

// 获取用户组外人员
var GetGroupOutSideUser = function (data) {
  return request({
    url: '/api/v1/groups/' + data.id + '/group_outside_user/',
    method: 'get'
  })
}

// 添加用户到用户组
var AddUsertoGroup = function (data) {
  return request({
    url: '/api/v1/groups/' + data.id + '/add_userto_group/',
    method: 'post',
    data: data
  })
}

// 获取用户组里权限应用列表
var GetUserPermApps = function (data) {
  return request({
    url: '/api/v1/groups/' + data.id + '/get_group_permapp/',
    method: 'get'
  })
}

// 删除用户组
var DeleteGroup = function (data) {
  return request({
    url: '/api/v1/groups/' + data.id + '/',
    method: 'delete'
  })
}

// 创建用户组
var CreateGroup = function (data) {
  return request({
    url: '/api/v1/groups/',
    method: 'post',
    data: data
  })
}

// 更新用户组
var UpdateGroup = function (data) {
  console.log(data)
  return request({
    url: '/api/v1/groups/' + data.id + '/',
    method: 'put',
    data: data
  })
}

export { GetAllGroup, GetDetailGroup, DeleteUserGroup, GetGroupOutSideUser, AddUsertoGroup, GetUserPermApps, DeleteGroup, CreateGroup, UpdateGroup }
