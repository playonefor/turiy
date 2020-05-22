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

export { GetAllGroup, GetDetailGroup }
