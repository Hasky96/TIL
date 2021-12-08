<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input  v-model="credentials.username" type="text" id="username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input v-model="credentials.password" type="password" id="password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input @keyup.enter="signup" v-model="credentials.passwordConfirmation" type="password" id="passwordConfirmation">
    </div>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials:{
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
      .then(()=>{
        this.$router.push({name: 'Login'})
      }).catch(err=>{
        console.log(err)
      })
    
    }
  }
}
</script>
