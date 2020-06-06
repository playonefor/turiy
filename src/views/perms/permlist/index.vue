<template>
  <d2-container>
    <el-divider></el-divider>
    <el-row :gutter="20">
      <el-col :span="8">
        <div>
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>权限列表</span>
              <el-button style="float: right; padding: 3px 0" type="primary" @click="handlerPushuri" plain>创建权限</el-button>
            </div>
            <div style="width:60%;">
              <el-input
                placeholder="输入关键字进行过滤"
                v-model="filterText">
              </el-input>
            </div>
            <el-divider></el-divider>
            <el-tree
              :data="treedata"
              :props="defaultProps"
              @node-click="handleNodeClick"
              :render-content="renderContent"
              :filter-node-method="filterNode"
              highlight-current
              ref="tree"></el-tree>
          </el-card>
        </div>
      </el-col>
      <el-col :span="16">
      <el-card>
          <el-divider></el-divider>
          <el-table
            border
            :data="tableData"
            style="width: 100%">
            <el-table-column type="expand">
              <template slot-scope="props">
                <el-form label-position="left" inline>
                  <el-form-item label="权限名称">
                    <span>{{ props.row.name }}</span>
                  </el-form-item>
                  <el-form-item label="创建时间">
                    <span>{{ props.row.date_created }}</span>
                  </el-form-item>
                  <el-form-item label="备注">
                    <span>{{ props.row.comment }}</span>
                  </el-form-item>
                  <el-form-item label="用户组">
                    <span>{{ props.row.tgroups }}</span>
                  </el-form-item>
                  <el-form-item label="用户">
                    <span>{{ props.row.users }}</span>
                  </el-form-item>
                  <el-form-item label="应用">
                    <span>{{ props.row.apps }}</span>
                  </el-form-item>
                </el-form>
              </template>
            </el-table-column>
            <el-table-column
              label="权限名称"
              prop="name">
            </el-table-column>
            <el-table-column
              label="创建时间"
              prop="date_created">
            </el-table-column>
            <el-table-column
              label="备注"
              prop="comment">
            </el-table-column>
            <el-table-column
              label="操作">
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                <el-button
                  size="mini"
                  type="danger"
                  @click="handleDelete(scope.$index, scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>

          <el-divider></el-divider>

          <template>
          <div class="block">
            <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page="pageCurrent"
              :page-sizes="[5, 10, 20, 50, 100]"
              :page-size="pageSize"
              layout="total, sizes, prev, pager, next, jumper"
              :total="pagetotal">
            </el-pagination>
          </div>
          </template>
      </el-card>
      </el-col>
    </el-row>
  </d2-container>
</template>

<script>
import { mapActions } from 'vuex'
import dayjs from 'dayjs'

export default {
  name: 'permlist',
  data () {
    return {
      pagetotal: 0,
      pageCurrent: 1,
      pageSize: 5,
      filterText: '',
      tableData: [],
      treedata: [],
      defaultProps: {
        children: 'children',
        label: 'label'
      }
    }
  },
  methods: {
    // vuex
    ...mapActions('d2admin/perm', [
      'GetAllPerm',
      'GetPerms',
      'DeletePerm'
    ]),
    // node节点点击事件
    handleNodeClick (data) {
      if (data.children) {
        this.getpageperms(this.pageSize, this.pageCurrent, data.id)
        return true
      }
      return false
    },
    // 图标更改的方法事件
    renderContent (h, { node, data, store }) {
      return (
        <span>
          <i class={data.icon}></i>
          <span> {node.label}</span>
        </span>
      )
    },
    handleSizeChange (val) {
      this.pageSize = val
      this.getpageperms(this.pageSize, 1)
    },
    handleCurrentChange (val) {
      this.pageCurrent = val
      this.getpageperms(this.pageSize, this.pageCurrent)
    },
    getpageperms (pageSize, pageCurrent, id) {
      this.GetPerms({
        page_size: pageSize,
        page: pageCurrent,
        id: id
      }).then(res => {
        for (var i = 0, len = res.results.length; i < len; i++) {
          const datestr = dayjs(res.results[i].date_created).format('YYYY年M月D日 HH:mm:ss', res.results[i].date_created)
          const users = res.results[i].users.map(function (i) { return i.name })
          const apps = res.results[i].apps.map(function (i) { return i.name })
          const tgroups = res.results[i].tgroups.map(function (i) { return i.name })
          res.results[i].users = users.join(',')
          res.results[i].apps = apps.join(',')
          res.results[i].tgroups = tgroups.join(',')
          res.results[i].date_created = datestr
        }
        this.pagetotal = res.count
        this.tableData = res.results
      }).catch(err => {
        console.log(err)
      })
    },
    getallPerms () {
      this.GetAllPerm().then(res => {
        const treedata = []
        for (var i = 0, len = res.length; i < len; i++) {
          const firstnode = {
            name: res[i].name,
            id: res[i].id,
            label: res[i].name,
            icon: 'el-icon-bank-card',
            children: []
          }
          for (var j = 0, jlen = res[i].apps.length; j < jlen; j++) {
            const secondnode = {
              name: res[i].apps[j].name,
              id: res[i].apps[j].id,
              label: res[i].apps[j].name,
              icon: 'el-icon-s-order'
            }
            firstnode.children.push(secondnode)
          }
          treedata.push(firstnode)
        }
        this.treedata = treedata
      }
      ).catch(err => {
        console.log(err)
      }
      )
    },
    filterNode (value, data) {
      if (!value) return true
      return data.label.indexOf(value) !== -1
    },
    handlerPushuri () {
      this.$router.push(
        {
          name: 'createperm'
        }
      )
    },
    handleEdit (index, row) {
      this.$router.push(
        {
          name: 'permedit',
          params: { id: row.id }
        })
    },
    handleDelete (index, row, done) {
      this.$confirm('确认删除？', '删除', {
        type: 'warning'
      })
        .then(_ => {
          this.DeletePerm({
            id: row.id
          }).then(res => {
            this.treedata.splice(this.treedata[this.treedata.findIndex(obj => obj.id === row.id)], 1)
            this.tableData.splice(this.tableData[this.tableData.findIndex(obj => obj.id === row.id)], 1)
            this.$message.success('删除成功')
          }).catch(err => {
            this.$notify.error({
              title: '错误',
              message: '删除失败!'
            })
            console.log('err:', err)
          })
        })
        .catch(_ => {})
    }
  },
  watch: {
    filterText (val) {
      this.$refs.tree.filter(val)
    }
  },
  mounted () {
    this.getallPerms()
    this.getpageperms(this.pageSize, this.pageCurrent)
  }
}
</script>

<style>
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
