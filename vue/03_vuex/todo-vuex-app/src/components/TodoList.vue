<template>
  <div>
    <todo-list-item
      v-for="todo in todos"
      :key="todo.date"
      :todo="todo"
      :class="{'is_completed': todo.isCompleted}"
    ></todo-list-item>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'
import {mapState} from 'vuex'
export default {
  name : 'TodoList',
  components:{
    TodoListItem,
  },
  // computed: {
  //   todos: function(){
  //     return this.$store.state.todos
  //   }
  // }
  // computed: mapState([
  //   'todos',
  // ]),
  computed: {
    ...mapState([
    'todos',
    ])
  }
}
</script>
<style>
.is_completed{  
  text-decoration: line-through;
}
</style>