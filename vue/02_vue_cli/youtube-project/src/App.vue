<template>
  <div id="app">
    <h1>My first Youtube Project</h1>
    <header>
      <the-search-bar @input-change="onInputChange"></the-search-bar>
    </header>
    <video-detail :video="selectedVideo"></video-detail>
    <section>
      <video-list :videos="videos" @select-video="onVideoSelect"></video-list>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
// @/ => src
// import TheSearchBar from 'src/components/TheSearchBar'
import TheSearchBar from '@/components/TheSearchBar'
import VideoList from "@/components/VideoList.vue"
import VideoDetail from "@/components/VideoDetail.vue"
const API_KEY = "AIzaSyDu2bC5h3-VtKO1Ttct26O_sAlhyFet6sQ"
const API_URL = "https://www.googleapis.com/youtube/v3/search"

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  data: function
    VideoListItem(){
    return {
      inputValue: null,
      videos: [],
      selectedVideo: null,
    }
  },
  methods:{
    onInputChange: function(inputValue){
      //검색어 저장
      this.inputValue = inputValue
      
      const params = {
        key : API_KEY,
        part: 'snippet',
        // 검색어
        q: this.inputValue,
        type: "video",
      }

      axios({
        method:'get',
        url: API_URL,
        params,
      }).then(res=>{
        console.log(res)
        //응답 저장
        this.videos=res.data.items
        }).catch(err=>{
          console.log(err)
          })
    },
    onVideoSelect: function(video){
      this.selectedVideo=video
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
