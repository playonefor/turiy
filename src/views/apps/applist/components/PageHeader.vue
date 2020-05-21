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
    <el-form-item label="组名" prop="name">
      <el-input
        v-model="form.name"
        placeholder="组名"
        style="width: 200px;"/>
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
  </el-col>
</el-row>
</template>

<script>

export default {
  data () {
    return {
      form: {
        name: ''
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
    }
  }
}
</script>
