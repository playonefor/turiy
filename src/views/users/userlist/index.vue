<template>
  <d2-container>
    <PageHeader slot="header" @submit="handleSubmit" @flush="refreshData" ref="header"> </PageHeader>
    <div>
      <d2-crud
        ref="d2Crud"
        :columns="columns"
        :rowHandle="rowHandle"
        edit-title="编辑用户"
        :editTemplate="editTemplate"
        :data="data"
        :options="options"
        :loading="loading"
        :edit-rules="editRules"
        :pagination="pagination"
        :form-options="formOptions"
        @pagination-current-change="paginationCurrentChange"
        @row-remove="handleRowRemove"
        @row-edit="handleRowEdit"
        @dialog-cancel="handleDialogCancel" />
    </div>
  </d2-container>
</template>

<script>
import { mapActions } from 'vuex'
import active from './components/active'
import staff from './components/staff'
import PageHeader from './components/PageHeader'
import dayjs from 'dayjs'
export default {
  components: {
    active,
    staff,
    PageHeader
  },
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
          width: '120',
          sortable: true,
          component: {
            name: staff
          }
        },
        {
          title: '状态',
          key: 'is_active',
          width: '90',
          sortable: true,
          component: {
            name: active
          }
        },
        {
          title: '最后登录时间',
          key: 'last_login',
          width: '180',
          sortable: true,
          formatter: this.formatDate
        }
      ],
      rowHandle: {
        columnHeader: '操作',
        edit: {
          icon: 'el-icon-edit',
          text: '编辑',
          size: 'mini'
        },
        remove: {
          icon: 'el-icon-delete',
          text: '删除',
          size: 'mini',
          type: 'danger',
          confirm: true
        },
        width: '200',
        fixed: 'right'
      },
      editTemplate: {
        username: {
          title: '用户名',
          component: {
            name: 'el-input'
          }
        },
        password: {
          title: '密码',
          value: '',
          component: {
            name: 'el-input'
          }
        },
        name: {
          title: '姓名',
          component: {
            name: 'el-input'
          }
        },
        email: {
          title: '邮箱',
          component: {
            name: 'el-input'
          }
        },
        mobile: {
          title: '电话',
          component: {
            name: 'el-input'
          }
        },
        wechat: {
          title: '微信',
          component: {
            name: 'el-input'
          }
        },
        is_staff: {
          title: '管理员',
          component: {
            name: 'el-switch'
          }
        },
        is_active: {
          title: '状态',
          component: {
            name: 'el-switch'
          }
        }
      },
      formOptions: {
        labelWidth: '80px',
        labelPosition: 'left',
        saveLoading: false,
        saveButtonType: 'primary',
        gutter: 20
      },
      data: [],
      loading: true,
      options: {
        border: true
      },
      pagination: {
        currentPage: 1,
        pageSize: 10,
        total: 0
      },
      editRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' }
        ],
        name: [
          { required: true, message: '请输入姓名', trigger: 'blur' }
        ],
        mobile: [
          { required: true, message: '请输入手机号', trigger: 'blur' }
        ],
        email: [
          { required: true, message: '请输入电子邮箱', trigger: 'blur' }
        ]
      }
    }
  },
  mounted () {
    this.fetchData(this.pagination.currentPage, this.pagination.pageSize)
  },
  methods: {
    ...mapActions('d2admin/account', [
      'GetAllUser',
      'DeleteUser',
      'UpdateUser'
    ]),
    paginationCurrentChange (currentPage) {
      this.pagination.currentPage = currentPage
      this.fetchData(this.pagination.currentPage, this.pagination.pageSize)
    },
    fetchData (page, pagesize) {
      this.loading = true
      // 获取子组件数据
      const fetchdata = this.$refs.header.form
      // fetchdata.is_active = (fetchdata.is_active === 'true')
      fetchdata.page = page
      fetchdata.page_size = pagesize
      this.GetAllUser(
        fetchdata
      ).then(res => {
        const resdata = []
        // 密码默认值
        for (var i = 0, len = res.results.length; i < len; i++) {
          res.results[i].password = ''
          resdata.push(res.results[i])
        }
        this.data = resdata
        this.pagination.total = res.count
        this.loading = false
      }).catch(err => {
        console.log('err', err)
        this.loading = false
      })
    },
    formatDate (row, column, cellValue, index) {
      if (cellValue) {
        var timestr = new Date(cellValue)
        return dayjs(timestr).format('YYYY年M月D日 HH:mm:ss', timestr)
      }
      return ''
    },
    handleRowRemove ({ index, row }, done) {
      this.DeleteUser(
        { 'id': row.id }
      ).then(res => {
        this.$message(
          {
            message: '删除成功',
            type: 'success'
          })
      })
      done()
    },
    handleRowEdit ({ index, row }, done) {
      this.formOptions.saveLoading = true
      const rowstr = row.password.replace(/\s+/g, '')
      console.log(row)
      if (!rowstr) {
        delete row.password
      }
      this.UpdateUser(row).then(res => {
        setTimeout(() => {
          this.$message({
            message: '编辑成功',
            type: 'success'
          })

          // done可以传入一个对象来修改提交的某个字段
          done({
            address: '我是通过done事件传入的数据！'
          })
          this.formOptions.saveLoading = false
        }, 400).catch(err => {
          this.loading = false
          console.log('err', err)
        })
      })
    },
    handleDialogCancel (done) {
      done()
    },
    handleSubmit (form) {
      this.loading = true
      this.GetAllUser({
        ...form
      })
        .then(res => {
          this.loading = false
          const resdata = []
          // 密码默认值
          for (var i = 0, len = res.results.length; i < len; i++) {
            res.results[i].password = ''
            resdata.push(res.results[i])
          }
          this.data = resdata
          this.pagination.total = res.count
        })
        .catch(err => {
          this.loading = false
          console.log('err', err)
        })
    },
    refreshData () {
      this.loading = true
      this.fetchData(this.pagination.currentPage, this.pagination.pageSize)
    }
  }
}
</script>
