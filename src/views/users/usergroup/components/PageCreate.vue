<template>
  <d2-container>
    <el-card>
       <div slot="header" class="clearfix">
         <span style="text-align: center;display:block;">新增用户组</span>
      </div>
      <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-row>
          <el-col :span="16">
          <el-form-item label="用户组名称" prop="name">
            <el-input v-model="ruleForm.name"></el-input>
          </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="16">
          <el-form-item label="用户组成员" prop="users">
           <el-select v-model="ruleForm.users" multiple filterable placeholder="请选择" style="width:100%">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
           </el-select>
          </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="16">
          <el-form-item label="备注信息" prop="comment">
            <el-input type="textarea" v-model="ruleForm.comment"></el-input>
          </el-form-item>
          </el-col>
        </el-row>
        <el-form-item>
          <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
          <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </d2-container>
</template>
<script>
import { mapActions } from 'vuex'
export default {
  data () {
    return {
      ruleForm: {
        name: '',
        users: [],
        comment: ''
      },
      options: [],
      rules: {
        name: [
          { required: true, message: '请输入用户组名称', trigger: 'blur' },
          { min: 3, max: 10, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    ...mapActions('d2admin/account', ['GetAllUser']),
    ...mapActions('d2admin/group', ['CreateGroup']),
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          console.log(this.ruleForm)
          this.CreateGroup(this.ruleForm).then(async res => {
            console.log(res)
            if (res) {
              this.$message.success('添加成功！')
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
    getusers () {
      this.GetAllUser().then(res => {
        for (var i = 0, len = res.results.length; i < len; i++) {
          const userlist = {
            value: res.results[i].id,
            label: res.results[i].username
          }
          this.options.push(userlist)
        }
      }
      ).catch(err => {
        console.log(err)
        return false
      })
    }
  },
  mounted () {
    this.getusers()
  }
}
</script>
