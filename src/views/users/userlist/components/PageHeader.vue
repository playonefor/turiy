<template>
  <el-row :gutter="20">
  <el-form
    :inline="true"
    :model="form"
    ref="form"
    size="mini"
    style="margin-bottom: -10px;margin-top:10px;"
    >

    <el-col :span="20">
    <el-form-item label="用户名" prop="username">
      <el-input
        v-model="form.username"
        placeholder="用户名"
        style="width: 100px;"/>
    </el-form-item>

    <el-form-item label="状态" prop="is_active">
      <el-select
        v-model="form.is_active"
        placeholder="状态选择"
        style="width: 100px;">
        <el-option label="状态选择" value=""/>
        <el-option label="启用" value="1"/>
        <el-option label="禁用" value="0"/>
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
    </el-col>
  </el-form>

  <el-col :span="4">
    <el-button
      type="success"
      @click="refreshData"
      style="float: right;"
      size="mini"
      >
      <d2-icon name="refresh"/>
        刷新
    </el-button>
    <AddDialog style="float: right;"/>
  </el-col>
</el-row>
</template>

<script>
import AddDialog from './AddDialog'

export default {
  components: {
    AddDialog
  },
  data () {
    return {
      form: {
        is_active: '',
        username: '',
        mobile: '',
        email: ''
      }
    }
  },
  methods: {
    handleFormSubmit () {
      this.$emit('submit', this.form)
      // 前端验证
      /*
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
      */
    },
    handleFormReset () {
      this.$refs.form.resetFields()
    },
    refreshData () {
      this.$emit('flush', this.form)
    },
    handleAddDialog () {
      AddDialog.dialogFormVisible = false
      console.log(AddDialog)
      AddDialog.dialogFormVisible = true
    }
  }
}
</script>
