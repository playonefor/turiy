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
      return this.value ? '是' : '否'
    },
    is_staff () {
      return this.scope.row.is_staff
    },
    id () {
      return this.scope.row.id
    },
    username () {
      return this.scope.row.username
    }
  },
  methods: {
    ...mapActions('d2admin/account', [
      'UpdateUser'
    ]),
    handleClick () {
      this.UpdateUser({
        id: this.id,
        is_staff: !this.is_staff,
        username: this.username
      })
      this.$emit('input', !this.value)
    }
  }
}
</script>
