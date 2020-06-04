<template>
  <div style="cursor: pointer">
    <el-link @click="handleClick" type="primary">{{ text }}</el-link>
  </div>
</template>
<script>
export default {
  props: {
    astr: {
      type: String,
      require: true
    },
    scope: {
      default: null
    },
    myProps: {
      default: null
    }
  },
  computed: {
    text () {
      return this.scope.row.name
    }
  },
  mounted () {
  },
  methods: {
    handleClick () {
      const groupid = this.scope.row.id
      this.$router.push(
        {
          name: 'groupdetail',
          params: { groupid }
        }
      )
    }
  }
}
</script>
