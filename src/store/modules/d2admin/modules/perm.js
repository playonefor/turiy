import { GetAllPerm, GetPerms, GetUsers, GetApps, GettGgroups, CreatePerm, GetPermOutUser, GetPermOutApp, GetPermOutGroup, GetPerm, UpdatePerm, DeletePerm } from '@/api/perms'

export default {
  namespaced: true,
  actions: {
    /** 请求所有权限
    */
    GetAllPerm (vm, data) {
      return GetAllPerm(data)
    },
    /** 请求权限列表
    */
    GetPerms (vm, data) {
      return GetPerms(data)
    },
    /** 请求权限列表
    */
    GetUsers (vm) {
      return GetUsers()
    },
    /** 请求权限列表
    */
    GetApps (vm) {
      return GetApps()
    },
    /** 请求权限列表
    */
    GettGgroups (vm) {
      return GettGgroups()
    },
    /** 创建权限
    */
    CreatePerm (vm, data) {
      return CreatePerm(data)
    },
    /** 请求权限以外的用户
    */
    GetPermOutUser (vm, data) {
      return GetPermOutUser(data)
    },
    /** 请求权限以外的应用
    */
    GetPermOutApp (vm, data) {
      return GetPermOutApp(data)
    },
    /** 请求权限以外的应用
    */
    GetPermOutGroup (vm, data) {
      return GetPermOutGroup(data)
    },
    /**  获取权限信息
    */
    GetPerm (vm, data) {
      return GetPerm(data)
    },
    /**  获取权限信息
    */
    UpdatePerm (vm, data) {
      return UpdatePerm(data)
    },
    DeletePerm (vm, data) {
      return DeletePerm(data)
    }
  }
}
