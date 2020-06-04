<template>
  <d2-container>
  <PageHeader slot="header" @submit="handleSubmit" @flush="refreshData" ref="header"> </PageHeader>
  <div>
    <d2-crud
      ref="d2Crud"
      :columns="columns"
      :rowHandle="rowHandle"
      edit-title="编辑用户组"
      :editTemplate="editTemplate"
      :edit-rules="editRules"
      :data="data"
      :options="options"
      :form-options="formOptions"
      :pagination="pagination"
      @pagination-current-change="paginationCurrentChange"
      @dialog-cancel="handleDialogCancel"
      @d2-data-change="handleDataChange"
      @row-edit="handleRowEdit"
      @row-remove="handleRowRemove"
      />
  </div>
  </d2-container>
</template>

<script>
import { mapActions } from 'vuex'
import PageHeader from './components/PageHeader'
import PageHrefDetail from './components/PageHrefDetail'
import users from './components/users'
import dayjs from 'dayjs'
export default {
  components: {
    PageHeader,
    PageHrefDetail,
    users
  },
  data () {
    return {
      columns: [
        {
          title: '名称',
          key: 'name',
          width: '200',
          sortable: true,
          component: {
            name: PageHrefDetail,
            props: {
              myProps: ''
            }
          }
        },
        {
          title: '创建时间',
          key: 'date_created',
          width: '200',
          formatter: this.formatDate
        },
        {
          title: '备注',
          key: 'comment',
          width: '220'
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
        name: {
          title: '用户组名',
          component: {
            name: 'el-input'
          }
        },
        users: {
          title: '用户成员',
          value: [],
          component: {
            name: users
          }
        },
        comment: {
          title: '备注',
          component: {
            name: 'el-input'
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
      editRules: {
        name: [
          { required: true, message: '请输入用户组名称', trigger: 'blur' }
        ]
      },
      data: [
      ],
      options: {
        border: true
      },
      loading: true,
      pagination: {
        currentPage: 1,
        pageSize: 10,
        total: 0
      }
    }
  },
  methods: {
    ...mapActions('d2admin/group', [
      'GetAllGroup',
      'DeleteGroup',
      'UpdateGroup'
    ]),
    paginationCurrentChange (currentPage) {
      this.pagination.currentPage = currentPage
      this.fetchData(this.pagination.currentPage, this.pagination.pageSize)
    },
    fetchData (page, pagesize) {
      this.loading = true
      // 获取子组件数据
      const fetchdata = this.$refs.header.form

      fetchdata.page = page
      fetchdata.page_size = pagesize

      this.GetAllGroup(
        fetchdata
      ).then(res => {
        this.data = res.results
        this.pagination.total = res.count
        this.loading = false
      }).catch(err => {
        console.log('err', err)
        this.loading = false
      }
      )
    },
    formatDate (row, column, cellValue, index) {
      if (cellValue) {
        var timestr = new Date(cellValue)
        return dayjs(timestr).format('YYYY年M月D日 HH:mm:ss', timestr)
      }
      return ''
    },
    refreshData (form) {
      this.fetchData(this.pagination.currentPage, this.pagination.pageSize)
    },
    handleSubmit (form) {
      this.loading = true
      this.GetAllGroup({
        ...form
      }).then(res => {
        this.loading = false
        this.data = res.results
        this.pagination.total = res.count
      }).catch(err => {
        this.loading = false
        console.log('err', err)
      })
    },
    handleDataChange (data) {
      console.log(data)
    },
    handleRowRemove ({ index, row }, done) {
      this.DeleteGroup({
        id: row.id
      }).then(res => {
        console.log(res)
        setTimeout(() => {
          console.log(index)
          console.log(row)
          this.$message({
            message: '删除成功',
            type: 'success'
          })
          done()
        }, 300)
      }).catch(
      )
    },
    handleRowEdit ({ index, row }, done) {
      console.log(row)
      this.formOptions.saveLoading = true
      this.UpdateGroup(row).then(res => {
        console.log(res)
        setTimeout(() => {
          this.$message({
            message: '编辑成功',
            type: 'success'
          })
          done()
          this.formOptions.saveLoading = false
        }, 300)
      }).catch(err => {
        this.$notify.error({
          title: '错误',
          message: err
        })
      }
      )
    },
    handleDialogCancel (done) {
      done()
    }
  },
  mounted () {
    this.loading = true
    this.fetchData(this.pagination.currentPage, this.pagination.pageSize)
    this.loading = false
  }
}
</script>
