<template>
  <div id="app">
    <h1>Youtube API Study</h1>
    <the-search-bar
      @get-search-text="searchVideos"
    >
    </the-search-bar>
    <video-list
      :videos="videos"
    >
    </video-list>
  </div>
</template>

<script>
import axios from "axios"
import TheSearchBar from './components/TheSearchBar.vue'
import VideoList from './components/VideoList.vue'

const API_URL = "https://www.googleapis.com/youtube/v3/search"


export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
  },
  data:function(){
    return {
      videos: null,
    }
  },
  methods:{
    searchVideos(searchText) {
      // console.log(this.searchText)
      const params = {
        part : "snippet",
        q: searchText,
        type: "video",
        key: "AIzaSyDu2bC5h3-VtKO1Ttct26O_sAlhyFet6sQ",
      }
      axios({
        method: "get",
        url : API_URL,
        params
      }).then(res=>{
        console.log(res)
        this.videos = res.data.items
      }).catch(error=>{
        console.log(error)
      })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

