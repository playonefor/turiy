import request from '@/plugin/axios'

// 获取用户组
var GetAllGroup = function (data) {
  return request({
    url: '/api/v1/groups/',
    method: 'get',
    params: data
  })
}

export { GetAllGroup }
