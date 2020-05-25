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

export { GetAllGroup, GetDetailGroup, DeleteUserGroup, GetGroupOutSideUser, AddUsertoGroup, GetUserPermApps }
