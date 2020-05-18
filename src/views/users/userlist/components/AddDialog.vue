<template>
  <div :style="style.addDialog">
    <el-button icon="el-icon-plus" type="primary" size="mini" @click="dialogFormVisible = true">新增</el-button>
    <el-dialog title="新增用户" :visible.sync="dialogFormVisible">
      <el-form :model="userForm" :rules="rules" ref="ruleForm"  label-position="left">
        <el-form-item label="用户名" :label-width="formLabelWidth" prop="username">
          <el-input v-model="userForm.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" :label-width="formLabelWidth" prop="password">
          <el-input type="password" v-model="userForm.password"></el-input>
        </el-form-item>
        <el-form-item label="姓名" :label-width="formLabelWidth" prop="name">
          <el-input v-model="userForm.name"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" :label-width="formLabelWidth" prop="email">
          <el-input v-model="userForm.email"></el-input>
        </el-form-item>
        <el-form-item label="手机" :label-width="formLabelWidth" prop="mobile">
          <el-input v-model="userForm.mobile"></el-input>
        </el-form-item>
        <el-form-item label="微信" :label-width="formLabelWidth" prop="wechat">
          <el-input v-model="userForm.wechat"></el-input>
        </el-form-item>
        <el-form-item label="管理员" :label-width="formLabelWidth" prop="is_staff">
          <el-switch v-model="userForm.is_staff"></el-switch>
        </el-form-item>
        <el-form-item label="状态" :label-width="formLabelWidth" prop="is_active">
          <el-switch v-model="userForm.is_active"></el-switch>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="handleSubmit('ruleForm')">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  data () {
    return {
      style: {
        addDialog: {
          display: 'inline-block',
          marginRight: '10px'
        }
      },
      dialogFormVisible: false,
      userForm: {
        username: '',
        name: '',
        email: '',
        mobile: '',
        wechat: '',
        password: '',
        is_active: true,
        is_staff: true
      },
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ],
        name: [
          { required: true, message: '请输入姓名', trigger: 'blur' }
        ],
        email: [
          { required: true, message: '请输入邮箱', trigger: 'blur' },
          { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur'] }
        ],
        mobile: [
          { required: true, message: '请输入手机号', trigger: 'blur' }
        ]
      },
      props: { },
      formLabelWidth: '80px'
    }
  },
  computed: {},
  methods: {
    ...mapActions('d2admin/account', ['GetAllUser', 'CreateUser']),
    handleSubmit (formName) {
      this.$refs[formName].validate(valid => {
        if (!valid) {
          this.$notify.error({
            title: '错误',
            message: '表单校验失败'
          })
          return false
        }

        this.CreateUser({
          ...this.userForm
        }).then(async res => {
          if (res) {
            this.$message.success('添加成功！')
            this.dialogFormVisible = false
          } else {
            console.log(res)
            this.$notify.error({
              title: '错误',
              message: '添加错误'
            })
            // this.$message.error('添加失败！error:')
            console.log('err: ', res.error)
          }
        }).catch(err => {
          console.log('err: ', err)
        })
      })
    }
  }
}
</script>
