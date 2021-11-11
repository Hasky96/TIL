<template>
  <div>
    <input type="text" @keyup.enter="getSearchText">
  </div>
</template>

<script>
export default {
  name: "TheSearchBar",
  methods: {
    getSearchText(event){
      // console.log(event.target.value)
      this.$emit("get-search-text", event.target.value)
    }
  }
}
</script>

<style>

</style>