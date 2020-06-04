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
          <el-card>
            <el-divider></el-divider>
            <el-row>
            <el-col :span="16">
            <el-select v-model="value1" multiple filterable placeholder="请选择">
              <el-option
                v-for="item in selectoptions"
                :key="item.id"
                :label="item.username"
                :value="item.id">
              </el-option>
            </el-select>
            </el-col>
            <el-col :span="8">
            <el-button type="primary" @click="addUsertoGroup">添加到用户组</el-button>
            </el-col>
            </el-row>
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
            @row-remove="handleRowRemove"
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
            <el-tree :data="treedata" @node-click="handleNodeClick" highlight-current :render-content="renderContent">
            </el-tree>
          </el-card>
          </el-col>
          <el-col :span="16">
          <el-card>
            <d2-crud
            :columns="appcolumns"
            :data="appdata"
            :pagination="apppagination"
            @pagination-current-change="apppaginationCurrentChange"
            :options="options"/>
            <el-input v-model="input" slot="header" placeholder="应用名称" style="margin-bottom: 5px; width:200px;" @input="appchangeValue" prefix-icon="el-icon-search" size="small" clearable></el-input>
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
      appcolumns: [
        {
          title: '权限名称',
          key: 'permname',
          width: '180'
        },
        {
          title: '应用名称',
          key: 'appname',
          width: '180'
        },
        {
          title: '环境',
          key: 'envcode',
          width: '180'
        }
      ],
      treedata: [
        {
          label: '所有环境',
          icon: 'el-icon-copy-document',
          id: '5'
        },
        {
          label: '开发环境',
          icon: 'el-icon-copy-document',
          id: '0'
        },
        {
          label: '测试环境',
          icon: 'el-icon-copy-document',
          id: '1'
        },
        {
          label: 'Beta环境',
          icon: 'el-icon-copy-document',
          id: '2'
        },
        {
          label: '生产环境',
          icon: 'el-icon-copy-document',
          id: '3'
        }],
      defaultProps: {
        children: 'children',
        label: 'label'
      },
      userdata: [
      ],
      appdata: [],
      alluserdata: [],
      allappdata: [],
      options: {
        border: true
      },
      selectoptions: [],
      value1: [],
      rowHandle: {
        columnHeader: '操作',
        remove: {
          icon: 'el-icon-right',
          size: 'small',
          type: 'info',
          text: '退出',
          confirmTitle: '是否退出',
          confirmText: '是否退出用户组?',
          fixed: 'right',
          confirm: true
        },
        width: '200',
        fixed: 'right'
      },
      pagination: {
        currentPage: 1,
        pageSize: 10,
        total: 0
      },
      apppagination: {
        currentPage: 1,
        pageSize: 10,
        total: 0
      },
      sectionappdata: []
    }
  },
  methods: {
    ...mapActions('d2admin/group', [
      'GetDetailGroup',
      'DeleteUserGroup',
      'GetGroupOutSideUser',
      'AddUsertoGroup',
      'GetUserPermApps'
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
    // 监听input标签内容
    changeValue (val) {
      const users = []
      for (var i = 0, len = this.alluserdata.length; i < len; i++) {
        if (this.alluserdata[i].username.indexOf(val) !== -1) {
          users.push(this.alluserdata[i])
        }
      }
      this.userdata = users
      this.pagination.total = this.userdata.length
    },
    appchangeValue (val) {
      const apps = []
      for (var i = 0, len = this.sectionappdata.length; i < len; i++) {
        if (this.sectionappdata[i].appname.indexOf(val) !== -1) {
          apps.push(this.sectionappdata[i])
        }
      }
      this.appdata = apps
      this.apppagination.total = this.appdata.length
    },
    handleClick (tab, event) {
      console.log(tab, event)
    },
    // 数据前端分页
    setCurrentPageData () {
      const begin = (this.pagination.currentPage - 1) * this.pagination.pageSize
      const end = this.pagination.currentPage * this.pagination.pageSize
      this.userdata = this.alluserdata.slice(
        begin,
        end
      )
    },
    appsetCurrentPageData () {
      const begin = (this.apppagination.currentPage - 1) * this.apppagination.pageSize
      const end = this.apppagination.currentPage * this.apppagination.pageSize
      this.appdata = this.sectionappdata.slice(
        begin,
        end
      )
    },
    paginationCurrentChange (currentPage) {
      this.pagination.currentPage = currentPage
      this.setCurrentPageData()
    },
    apppaginationCurrentChange (currentPage) {
      this.apppagination.currentPage = currentPage
      this.appsetCurrentPageData()
    },
    handleRowRemove ({ index, row }, done) {
      this.DeleteUserGroup({
        gid: this.gid,
        id: row.id
      }).then(
        setTimeout(() => {
          this.$message({
            message: '退出成功',
            type: 'success'
          })
          done()
        }, 300))
    },
    getGroupOutSideUser () {
      this.GetGroupOutSideUser({
        id: this.gid
      }).then(res => {
        this.selectoptions = res
      }).catch(err => {
        console.log('err:', err)
      })
    },
    addUsertoGroup () {
      this.AddUsertoGroup({
        id: this.gid,
        users: this.value1
      }).then(res => {
        for (var i = 0, len = res.length; i < len; i++) {
          this.userdata.unshift(res[i])
        }
      }).catch(err => {
        this.$notify('err', err.detail)
        console.log('err', err.detail)
      })
    },
    handleNodeClick (data) {
      if (data.id === '5') {
        this.sectionappdata = this.allappdata
        this.apppagination.total = this.sectionappdata.length
        this.appdata = this.sectionappdata.slice(0, 10)
        return
      }
      this.sectionappdata = this.allappdata.filter(app =>
        app.env === data.id
      )
      this.apppagination.total = this.sectionappdata.length
      this.appdata = this.sectionappdata.slice(0, 10)
    },
    renderContent (h, { node, data, store }) {
      return (
        <span>
          <i class={data.icon}></i>
          <span> {node.label}</span>
        </span>
      )
    },
    loadappdata () {
      this.GetUserPermApps(
        { id: this.gid }
      ).then(res => {
        const datas = []
        for (var i = 0, permslen = res.perms.length; i < permslen; i++) {
          for (var j = 0, applen = res.perms[i].apps.length; j < applen; j++) {
            const permappobj = {}
            permappobj.permname = res.perms[i].name
            permappobj.appname = res.perms[i].apps[j].name
            permappobj.env = res.perms[i].apps[j].env
            permappobj.envcode = res.perms[i].apps[j].envcode
            datas.push(permappobj)
          }
        }
        this.allappdata = datas
      }).catch(res => {
        console.log('err', res.details)
      })
    }
  },
  mounted () {
    this.fetchData()
    this.setCurrentPageData()
    this.getGroupOutSideUser()
    this.loadappdata()
  }
}
</script>
<style>
</style>
