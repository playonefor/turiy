import { GetAllGroup, GetDetailGroup } from '@/api/groups'
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
    }
  }
}
