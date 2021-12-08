<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input  v-model="credentials.username" type="text" id="username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input @keyup.enter="login" v-model="credentials.password" type="password" id="password">
    </div>
    <div>
    </div>
    <button @click="login">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials:{
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: "http://127.0.0.1:8000/accounts/api-token-auth/",
        data: this.credentials
      }).then(res=>{
        console.log(res)
        localStorage.setItem("jwt", res.data.token)
        this.$emit('login')
        this.$router.push({name: 'TodoList'})
      }).catch(err=>{
        console.log(err)
      })
      
    }
  }
}
</script>
