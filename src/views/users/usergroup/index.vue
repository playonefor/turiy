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
export default {
  data () {
    return {
      columns: [
        {
          title: '日期',
          key: 'date',
          width: '180',
          sortable: true
        },
        {
          title: '姓名',
          key: 'name',
          width: '180'
        },
        {
          title: '地址',
          key: 'address',
          fixed: 'right'
        }
      ],
      data: [
        {
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        },
        {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄'
        },
        {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄'
        },
        {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄'
        }
      ],
      options: {
        border: true
      }
    }
  }
}
</script>
