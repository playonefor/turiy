import request from '@/plugin/axios'

var AccountLogin = function (data) {
  return request({
    url: '/api/auth/login/',
    method: 'post',
    data
  })
}

var GetAllUser = function (data){
  return request({
    url: '/api/v1/users/',
    method: 'get',
    data
  })
}

/*
var GetUser = function(data) {
  return request({
    url: '/services/app/User/Get',
    method: 'get',
    params: data
  })
}

var GetAllUser = function(data) {
  return request({
    url: '/services/app/User/GetLists',
    method: 'get',
    params: data
  })
}

var UserCreate = function(data) {
  return request({
    url: '/services/app/User/Create',
    method: 'post',
    data
  })
}

var UserUpdate = function(data) {
  return request({
    url: '/services/app/User/Update',
    method: 'put',
    data
  })
}
var UserDelete = function(data) {
  return request({
    url: '/services/app/User/Delete',
    method: 'delete',
    params: data
  })
}
*/
export { AccountLogin, GetAllUser }
