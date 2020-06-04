import { GetAllPerm } from '@/api/perms'

export default {
  namespaced: true,
  /** 请求所有权限
   */
  actions: {
    GetAllPerm (vm, data) {
      return GetAllPerm(data)
    }
  }
}
