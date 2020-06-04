<template>
  <div style="cursor: pointer">
    <el-input v-model="passwd" @input="handlerPassword" show-password></el-input>
  </div>
</template>
<script>
export default {
  props: {
    value: {
      type: String
    },
    // 本行的所有数据，此字段不需要额外配置
    scope: {
      default: null
    },
    // 通过 component 中 props 字段传过来的数据，此字段需要先在 component 中配置
    myProps: {
      default: null
    }
  },
  data () {
    return {
      passwd: ''
    }
  },
  methods: {
    handlerPassword () {
      this.$emit('input', this.passwd)
    }
  }
}
</script>
