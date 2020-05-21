import { GetAllGroup } from '@/api/groups'
export default {
  namespaced: true,
  actions: {
    /** 请求用户组列表
     */
    GetAllGroup (vm, data) {
      return GetAllGroup(data)
    }
  }
}
