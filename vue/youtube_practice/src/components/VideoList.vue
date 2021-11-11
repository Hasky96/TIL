<template>
  <div>
    <ul>
      <video-list-item
        v-for="video in videos" :key="video.id.videoId"
      >
      </video-list-item>
    </ul>
  </div>
</template>

<script>
import VideoListItem from "./VideoListItem.vue"

export default {
  name: "VideoList",
  components:{
    VideoListItem,
  },
  props:{
    videos: Array,
  }
}
</script>

<style>

</style>