import request from '@/plugin/axios'

// 获取权限列表
var GetAllPerm = function (data) {
  return request({
    url: '/api/v1/permisson/getall/',
    method: 'get',
    params: data
  })
}

export { GetAllPerm }
