<template>
  <div>
    <input 
    type="text"
    v-model.trim="todoTitle"
    @keyup.enter="createTodo" 
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
export default {
  name: "TodoForm",
  data : function (){
    return {
      todoTitle: null,
    }
  },
  methods:{
    createTodo(){
      console.log("todo CREATED! by createTodo method at TodoForm.vue ")
      const todoItem = {
        title: this.todoTitle,
        isCompleted: false,
        date : new Date().getTime(),
      }
      // mutation handler 호출 (commit)
      // this.$store.commit(/*mutations name*/'CREATE_TODO', /*payload:전송되는 데이터*/todoItem)

      //validation
      if(todoItem.title){
        // action handler 호출 (dispatch)
        this.$store.dispatch('createTodo', todoItem)
        this.todoTitle = null
      }
    }
  }
}
</script>

<style>

</style>