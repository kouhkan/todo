<template>
  <div id="app">

      <form @submit.prevent="submitForm">
          <div class="form-group row">
              <input type="text" class="form-control col-4 mx-auto" placeholder="Title" v-model="todo.title">
              <input type="text" class="form-control col-8 " placeholder="Description" v-model="todo.description">
          </div>
          <div class="form-group row">
              <input type="datetime-local" class="form-control col-9 " placeholder="Datetime" v-model="todo.do_date">
              <select class="form-control col-3 " v-model="todo.status">
                  <option value="w" selected>Working on</option>
                  <option value="d">Done</option>
                  <option value="c">Cancel</option>
              </select>
          </div>
          <div class="form-group row">
              <input type="submit" value="Submit" class="btn btn-success btn-block">
          </div>
      </form>


    <table class="table table-striped table-hover">
      <thead>
        <th>Title</th>
        <th>Description</th>
        <th>Do Date</th>
        <th>Status</th>
        <th>Remove</th>
      </thead>
      <tbody>
       <tr v-for="todo in todo_list" :key="todo.id" @dblclick="$data.todo=todo">
          <td>{{ todo.title }}</td>
          <td>{{ todo.description }}</td>
          <td>{{ todo.do_date }}</td>
          <td>{{ todo.status }}</td>
           <td>
               <button class="btn btn-outline-danger btn-sm mx-1" @click="deleteTodo">&times;</button>
           </td>
       </tr>
      </tbody>
    </table>

  </div>
</template>

<script>

export default {
  name: 'App',
      data(){
        return {
        todo: {},
        todo_list: []
        }
      },
     async created(){
        await this.getTodos();
    },

    methods: {

      submitForm(){
          if (this.todo.id === undefined){
              this.createTodo();
          } else {
              this.editTodo();
          }
      },

      async getTodos(){
            var response = await fetch('http://localhost:8000/api/todos/');
            this.todo_list = await response.json();
      },

      async createTodo(){
          await this.getTodos();

         await fetch('http://localhost:8000/api/todos/', {
              method: 'post',
              headers: {
                  'Content-Type': 'application/json'
              },
              body: JSON.stringify(this.todo)
          });
          // this.todo_list.push(await response.json());
          await this.getTodos();
      },

    async editTodo(){
      await this.getTodos();

     await fetch(`http://localhost:8000/api/todos/${this.todo.id}/`, {
          method: 'put',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.todo)
      });
      // this.todo_list.push(await response.json());
      await this.getTodos();
      this.todo = {};
    },

    async deleteTodo(){
      await this.getTodos();

     await fetch(`http://localhost:8000/api/todos/${this.todo.id}/`, {
          method: 'delete',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.todo)
      });
      // this.todo_list.push(await response.json());
      await this.getTodos();
      this.todo = {};
    },

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
