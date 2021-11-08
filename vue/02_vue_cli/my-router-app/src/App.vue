<template>
  <div id="app">
    <div id="nav">
      <!-- router-link aTag 이지만 원래 역할 차단되어 있음 -->
      <router-link :to="{name:'Home'}">Home</router-link> |
      <router-link :to="{name:'About'}">About</router-link> |
      <router-link :to="{name:'TheLotto', params: { lottoNum : 6}}">TheLotto</router-link>
      
    </div>
    <!-- 라우터의 내용을 위치 -->
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
