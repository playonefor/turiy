<template>
  <d2-container>
  <div>

    <d2-crud
      ref="d2Crud"
      :columns="columns"
      :rowHandle="rowHandle"
      :data="data"
      :options="options"
      :pagination="pagination"
      @pagination-current-change="paginationCurrentChange"
      />
  </div>
  </d2-container>
</template>

<script>
import { mapActions } from 'vuex'
import dayjs from 'dayjs'
export default {
  data () {
    return {
      columns: [
        {
          title: '名称',
          key: 'name',
          width: '200',
          sortable: true
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
      'GetAllGroup'
    ]),
    paginationCurrentChange (currentPage) {
      this.pagination.currentPage = currentPage
      this.fetchData(this.pagination.currentPage, this.pagination.pageSize)
    },
    fetchData (page, pagesize) {
      this.loading = true
      this.GetAllGroup({
        page: page,
        page_size: pagesize
      }).then(res => {
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
    }
  },
  mounted () {
    this.fetchData()
  }
}
</script>
