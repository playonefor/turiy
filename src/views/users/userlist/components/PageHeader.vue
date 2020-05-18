<template>
  <el-form
    :inline="true"
    :model="form"
    ref="form"
    size="mini"
    style="margin-bottom: -10px;margin-top:10px;">

    <el-form-item label="用户名" prop="username">
      <el-input
        v-model="form.username"
        placeholder="用户名"
        style="width: 100px;"/>
    </el-form-item>

    <el-form-item label="状态" prop="type">
      <el-select
        v-model="form.type"
        placeholder="状态选择"
        style="width: 100px;">
        <el-option label="启用" value="true"/>
        <el-option label="禁用" value="false"/>
      </el-select>
    </el-form-item>

    <el-form-item label="手机" prop="mobile">
      <el-input
        v-model="form.mobile"
        placeholder="手机"
        style="width: 120px;"/>
    </el-form-item>

    <el-form-item label="邮箱" prop="email">
      <el-input
        v-model="form.email"
        placeholder="邮箱"
        style="width: 120px;"/>
    </el-form-item>

    <el-form-item>
      <el-button
        type="primary"
        @click="handleFormSubmit">
        <d2-icon name="search"/>
        查询
      </el-button>
    </el-form-item>

    <el-form-item>
      <el-button
        @click="handleFormReset">
        <d2-icon name="refresh"/>
        重置
      </el-button>
    </el-form-item>

  </el-form>
</template>

<script>
export default {
  data () {
    return {
      form: {
        type: 'true',
        username: '',
        mobile: '',
        email: ''
      }
    }
  },
  methods: {
    handleFormSubmit () {
      this.$refs.form.validate((valid) => {
        if (valid) {
          this.$emit('submit', this.form)
        } else {
          this.$notify.error({
            title: '错误',
            message: '表单校验失败'
          })
          return false
        }
      })
    },
    handleFormReset () {
      this.$refs.form.resetFields()
    }
  }
}
</script>
