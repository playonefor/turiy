<template>
  <d2-container>
    <el-card>
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="用户组" name="first">
        <el-row :gutter="20">
          <el-col :span="8">
          <el-card style="font-size:5px">
              <el-divider></el-divider>
              <el-row>
                 <el-col :span="10"><div class="" style="font-weight:900;">组id:</div></el-col>
                 <el-col :span="14"><div class="">{{ gdata.id }}</div></el-col>
              </el-row>
              <el-divider></el-divider>
              <el-row>
                 <el-col :span="10"><div class="" style="font-weight:900;">组名称:</div></el-col>
                 <el-col :span="14"><div class="">{{ gdata.name }}</div></el-col>
              </el-row>
              <el-divider></el-divider>
              <el-row>
                 <el-col :span="10"><div class="" style="font-weight:900;">创建时间:</div></el-col>
                 <el-col :span="14"><div class="">{{ gdata.date_created }}</div></el-col>
              </el-row>
              <el-divider></el-divider>
              <el-row>
                 <el-col :span="10"><div class="" style="font-weight:900;">备注:</div></el-col>
                 <el-col :span="14"><div class="">{{ gdata.comment }}</div></el-col>
              </el-row>
              <el-divider></el-divider>
          </el-card>
          </el-col>
          <el-col :span="16">
          <el-card>
            <d2-crud
            :columns="columns"
            :data="userdata"
            :rowHandle="rowHandle"
            :pagination="pagination"
            :options="options"
            @pagination-current-change="paginationCurrentChange"
            />
            <el-input v-model="input" slot="header" placeholder="用户名" style="margin-bottom: 5px; width:200px;" @input="changeValue" prefix-icon="el-icon-search" size="small" clearable></el-input>
          </el-card>
          </el-col>
        </el-row>
      </el-tab-pane>
      <el-tab-pane label="授权应用" name="second">
        <el-row :gutter="20">
          <el-col :span="8">
          <el-card>
            授权应用
          </el-card>
          </el-col>
          <el-col :span="16">
          <el-card>
            <d2-crud
            :columns="columns"
            :data="userdata"
            :options="options"/>
          </el-card>
          </el-col>
        </el-row>
      </el-tab-pane>
    </el-tabs>
    </el-card>
  </d2-container>
</template>

<script>
import { mapActions } from 'vuex'
import dayjs from 'dayjs'

export default {
  props: ['groupid'],
  computed: {
    gid () {
      return this.groupid
    }
  },
  data () {
    return {
      activeName: 'first',
      input: '',
      gdata: {
      },
      columns: [
        {
          title: '用户名',
          key: 'username',
          width: '180'
        },
        {
          title: '姓名',
          key: 'name',
          width: '180'
        }
      ],
      userdata: [
      ],
      alluserdata: [
      ],
      options: {
        border: true
      },
      rowHandle: {
        columnHeader: '操作',
        custom: [
          {
            text: '退出',
            type: 'warning',
            size: 'mini',
            emit: 'custom-emit-1'
          }
        ],
        width: '200',
        fixed: 'right'
      },
      pagination: {
        currentPage: 1,
        pageSize: 10,
        total: 0
      }
    }
  },
  methods: {
    ...mapActions('d2admin/group', [
      'GetDetailGroup'
    ]),
    fetchData () {
      this.GetDetailGroup(
        { id: this.groupid }
      ).then(res => {
        res.date_created = dayjs(res.date_created).format('YYYY年M月D日 HH:mm:ss', res.date_created)
        this.gdata = res
        this.pagination.total = res.users.length
        this.userdata = res.users.slice(0, 10)
        this.alluserdata = res.users
      }).catch(err => {
        console.log('err', err)
      })
    },
    changeValue (val) {
      const users = []
      for (var i = 0, len = this.alluserdata.length; i < len; i++) {
        if ( this.alluserdata[i].username.indexOf(val) !== -1 ) {
          users.push(this.alluserdata[i])
        }
      }
      this.userdata = users
      this.pagination.total = this.userdata.length
    },
    handleClick (tab, event) {
      console.log(tab, event)
    },
    setCurrentPageData () {
      const begin = (this.pagination.currentPage - 1) * this.pagination.pageSize
      const end = this.pagination.currentPage * this.pagination.pageSize
      this.userdata = this.alluserdata.slice(
        begin,
        end
      )
    },
    paginationCurrentChange (currentPage) {
      this.pagination.currentPage = currentPage
      this.setCurrentPageData()
    }
  },
  mounted () {
    this.fetchData()
    this.setCurrentPageData()
  }
}
</script>
<style>
</style>
