<template>
  <d2-container>
    <el-divider></el-divider>
    <el-row :gutter="20">
      <el-col :span="8">
        <div>
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>权限列表</span>
              <el-button style="float: right; padding: 3px 0" type="primary" plain>创建权限</el-button>
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
      <el-col :span="16"><div class="grid-content bg-purple"></div></el-col>
    </el-row>
  </d2-container>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'permlist',
  data () {
    return {
      filterText: '',
      treedata: [{
        id: 1,
        label: '权限1',
        icon: 'el-icon-bank-card',
        children: [{
          label: '应用1',
          icon: 'el-icon-s-order'
        }]
      }, {
        label: '权限2',
        icon: 'el-icon-bank-card',
        children: [{
          label: '应用2',
          icon: 'el-icon-s-order'
        }]
      }],
      defaultProps: {
        children: 'children',
        label: 'label'
      }
    }
  },
  methods: {
    // vuex
    ...mapActions('d2admin/perm', [
      'GetAllPerm'
    ]),
    // node节点点击事件
    handleNodeClick (data) {
      console.log(data)
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
    }
  },
  watch: {
    filterText (val) {
      this.$refs.tree.filter(val)
    }
  },
  mounted () {
    this.getallPerms()
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
