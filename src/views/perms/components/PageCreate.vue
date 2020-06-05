<template>
  <d2-container>
    <el-card class="box-card">
     <div slot="header" class="clearfix">
       <span style="text-align: center;display:block;">新增权限</span>
    </div>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-row>
        <el-col :span="16">
        <el-form-item label="权限名称" prop="name">
          <el-input v-model="ruleForm.name"></el-input>
        </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="18">
        <el-form-item label="用户成员">
        <el-transfer
          filterable
          filter-placeholder="请输入用户名"
          :titles="['未属于', '属于']"
          v-model="ruleForm.users"
          :data="usersdata">
        </el-transfer>
        </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="18">
        <el-form-item label="用户组" prop="comment">
        <el-transfer
          filterable
          filter-placeholder="请输入用户组名称"
          :titles="['未属于', '属于']"
          v-model="ruleForm.groups"
          :data="groupsdata">
        </el-transfer>
        </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="18">
        <el-form-item label="应用" prop="comment">
        <el-transfer
          filterable
          filter-placeholder="请输入应用名称"
          :titles="['未属于', '属于']"
          v-model="ruleForm.apps"
          :data="appsdata">
        </el-transfer>
        </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="16">
        <el-form-item label="备注" prop="comment">
          <el-input type="textarea" v-model="ruleForm.comment"></el-input>
        </el-form-item>
        </el-col>
      </el-row>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
        <!-- <el-button @click="resetForm('ruleForm')">重置</el-button> -->
      </el-form-item>
    </el-form>
    </el-card>
  </d2-container>
</template>
<script>
import { mapActions } from 'vuex'

export default {
  data () {
    /**
    const generateData = _ => {
      const data = []
      const cities = ['上海', '北京', '广州', '深圳', '南京', '西安', '成都']
      const pinyin = ['shanghai', 'beijing', 'guangzhou', 'shenzhen', 'nanjing', 'xian', 'chengdu']
      cities.forEach((city, index) => {
        data.push({
          label: city,
          key: index,
          pinyin: pinyin[index]
        })
      })
      return data
    }
    */
    return {
      usersdata: [],
      appsdata: [],
      groupsdata: [],
      ruleForm: {
        name: '',
        comment: '',
        users: [],
        apps: [],
        tgroups: []
      },
      rules: {
        name: [
          { required: true, message: '请权限名称', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    ...mapActions('d2admin/perm', [
      'GetUsers',
      'GetApps',
      'GettGgroups',
      'CreatePerm'
    ]
    ),
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.CreatePerm(this.ruleForm).then(async res => {
            if (res) {
              this.$message.success('添加成功')
            } else {
              this.$notify.error({
                title: '错误',
                message: '添加错误'
              })
              console.log('err: ', res.error)
            }
          }).catch(err => {
            console.log('err:', err)
          })
        } else {
          this.$notify.error({
            title: '错误',
            message: '表单校验失败'
          })
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    getresrc () {
      this.GetApps().then(res => {
        const data = []
        res.forEach((app, index) => {
          data.push({
            label: app.name,
            id: app.id,
            key: app.id
          })
        })
        this.appsdata = data
      })

      this.GetUsers().then(res => {
        const data = []
        res.forEach((user, index) => {
          data.push({
            label: user.username,
            id: user.id,
            key: user.id
          })
        })
        this.usersdata = data
      })

      this.GettGgroups().then(res => {
        const data = []
        res.forEach((group, index) => {
          data.push({
            label: group.name,
            id: group.id,
            key: group.id
          })
        })
        this.groupsdata = data
      })
    }
  },
  mounted () {
    this.getresrc()
  }
}
</script>
