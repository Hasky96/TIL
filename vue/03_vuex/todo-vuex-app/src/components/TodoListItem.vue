<template>
  <div>
    <div>
        <span @click="updateTodoStatus(todo)">{{todo.title}}</span>
        <button @click="deleteTodo(todo)">Delete</button>
    </div>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
export default {
  name: 'TodoListItem',
  props:{
    todo: Object,
  },
  methods:{
    // deleteTodo(){
    //   this.$store.dispatch('deleteTodo', this.todo)
    // },
    // updateTodoStatus(){
    //   this.$store.dispatch('updateTodoStatus', this.todo)
    // }
    ...mapActions([
      'deleteTodo',
      'updateTodoStatus'
    ])
  }
}
</script>

<style>

</style>