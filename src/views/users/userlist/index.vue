<template>
  <d2-container>
    <template slot="header">用户管理</template>
    <div>
      <d2-crud :columns="columns" :data="data" :options="options"/>
    </div>
    <template slot="footer">用户管理</template>
  </d2-container>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  mounted () {
    this.fetchData()
  },
  methods: {
    ...mapActions('d2admin/account', [
      'GetAllUser'
    ]),
    fetchData () {
      this.loading = true
      this.GetAllUser().then(res => {
        this.data = res
        this.loading = false
      }).catch(err => {
        console.log('err', err)
        this.loading = false
      })
    }
  },
  loading: true,
  data () {
    return {
      columns: [
        {
          title: '用户名',
          key: 'username',
          width: '120',
          sortable: true
        },
        {
          title: '名字',
          key: 'name',
          width: '120'
        },
        {
          title: 'Email',
          key: 'email',
          width: '180'
        },
        {
          title: '手机',
          key: 'mobile',
          width: '160'
        },
        {
          title: '微信',
          key: 'wehchat',
          width: '120'
        },
        {
          title: '是否管理员',
          key: 'is_staff',
          width: '120'
        },
        {
          title: '状态',
          key: 'is_active',
          width: '90'
        },
        {
          title: '操作',
          key: 'operation',
          fixed: 'right'
        }
      ],
      data: [],
      options: {
        border: true
      }
    }
  }
}
</script>
