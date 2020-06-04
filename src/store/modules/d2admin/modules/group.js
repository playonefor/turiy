import { GetAllGroup, GetDetailGroup, DeleteUserGroup, GetGroupOutSideUser, AddUsertoGroup, GetUserPermApps, DeleteGroup, CreateGroup, UpdateGroup } from '@/api/groups'
export default {
  namespaced: true,
  actions: {
    /** 请求用户组列表
     */
    GetAllGroup (vm, data) {
      return GetAllGroup(data)
    },
    /** 请求用户详情
     */
    GetDetailGroup (vm, data) {
      return GetDetailGroup(data)
    },
    /** 删除用户组用户
     */
    DeleteUserGroup (vm, data) {
      return DeleteUserGroup(data)
    },
    /** 获取用户组之外用户
     */
    GetGroupOutSideUser (vm, data) {
      return GetGroupOutSideUser(data)
    },
    /** 获取用户组之外用户
     */
    AddUsertoGroup (vm, data) {
      return AddUsertoGroup(data)
    },
    /* 获取用户组权限应用列表
     */
    GetUserPermApps (vm, data) {
      return GetUserPermApps(data)
    },
    /* 获取用户组权限应用列表
     */
    DeleteGroup (vm, data) {
      return DeleteGroup(data)
    },
    /* 获取用户组权限应用列表
     */
    CreateGroup (vm, data) {
      return CreateGroup(data)
    },
    /* 获取用户组权限应用列表
     */
    UpdateGroup (vm, data) {
      return UpdateGroup(data)
    }
  }
}
