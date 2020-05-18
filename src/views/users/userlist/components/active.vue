<template>
  <div style="cursor: pointer">
    <el-tag :type="type" @click.native="handleClick">{{ text }}</el-tag>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  props: {
    value: {
      type: Boolean,
      require: true
    },
    scope: {
      default: null
    },
    // 通过 component 中 props 字段传过来的数据，此字段需要先在 component 中配置
    myProps: {
      default: null
    }
  },
  computed: {
    type () {
      return this.value ? 'success' : 'danger'
    },
    text () {
      return this.value ? '启用' : '禁用'
    },
    is_active () {
      return this.scope.row.is_active
    },
    id () {
      return this.scope.row.id
    },
    username () {
      return this.scope.row.username
    }
  },
  mounted () {
  },
  methods: {
    ...mapActions('d2admin/account', [
      'UpdateUser'
    ]),
    handleClick () {
      this.UpdateUser({
        id: this.id,
        is_active: !this.is_active,
        username: this.username
      })
      console.log(this.id)
      console.log(this.is_active)
      this.$emit('input', !this.value)
    }
  }
}
</script>
