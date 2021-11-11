import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)
// components 를 공유하기 위함. => 목적에 따라 component가 local data를 가질 수 있음
export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    todos: []
  },
  mutations: {// => state 조작하는 역할 => 1번째 인자로 state / 상수값처럼 대문자로만듬(style-guide) / commit으로 호출됨
    // mutation handler 첫번째 인자는 항상 state
    CREATE_TODO: function(state, todoItem){// component 에서 commit일어남
      console.log("   mutations.CREATE_TODO RUN!...")
      state.todos.push(todoItem)
      console.log(`    PUSHED!`)
    },
    DELETE_TODO: function(state, todoItem){// component 에서 delete일어남
      console.log("   mutations.DELETE_TODO RUN!...")
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
      console.log(`    DELETED!`)
    },
    UPDATE_TODO_STATUS: function(state, todoItem){// component 에서 delete일어남
      console.log("   mutations.UPDATE_TODO_STATUS RUN!...")
      state.todos = state.todos.map(todo=>{
        if (todo === todoItem){
          return {
            ...todo, // javascript spread syntax
            isCompleted : !todo.isCompleted
          }
        }else{
          return todo
        }
      })
      console.log(`    UPDATED!`)
    },
  },
  actions: { // state변경 외 모든 동작을 수행 
    // 첫번째 인자로  context(commit, dispatch, getters, state, ...etc 포함)를 받음 // dispatch로 호출됨
    createTodo : function({commit, state}, todoItem){
      console.log(" actions.createTodo RUN!...")
      // mutations CREATE_TODO 호출 (commit)
      console.log(state)
      commit("CREATE_TODO", todoItem)
    },
    deleteTodo : function({commit}, todoItem){
      console.log(" actions.deleteTodo RUN!...")
      commit("DELETE_TODO", todoItem)
    },
    updateTodoStatus : function({commit}, todoItem){
      console.log(" actions.updateTodoStatus RUN!...")
      commit("UPDATE_TODO_STATUS", todoItem)
    }
  },
  getters: {
    completedTodosCount: function(state){
      return state.todos.filter(todo=>{
        return todo.isCompleted==true
      }).length
    },
    uncompletedTodosCount: function(state){
      return state.todos.filter(todo=>{
        return todo.isCompleted==false
      }).length
    },
    allTodosCount: function(state){
      return state.todos.length
    }
  },
  modules: {

  }
})

