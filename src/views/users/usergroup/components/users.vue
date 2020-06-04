<template>
  <div style="cursor: pointer">
      <el-select v-model="users" value-key="value" @change="handleruser" multiple filterable placeholder="请选择" style="width:100%">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
      </el-select>
  </div>
</template>
<script>
import { mapActions } from 'vuex'
export default {
  props: {
    value: {
      type: Array
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
      users: [],
      options: []
    }
  },
  methods: {
    ...mapActions('d2admin/account', ['GetAllUser']),
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
    },
    getcurrusers () {
      if (this.users) {
        for (var i = 0, len = this.value.length; i < len; i++) {
          if (typeof this.value[i] === 'object') {
            this.users.push(this.value[i].id)
          } else {
            this.users.push(this.value[i])
          }
        }
      }
    },
    handleruser () {
      if (this.users) {
        this.$emit('input', this.users)
      }
    }
  },
  mounted () {
    this.getusers()
    this.getcurrusers()
    this.handleruser()
  }
}

</script>
