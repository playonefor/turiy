import { GetAllPerm, GetPerms, GetUsers, GetApps, GettGgroups, CreatePerm } from '@/api/perms'

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
    }
  }
}
