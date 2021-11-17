
// import { useQuery, useQueryClient } from "react-query";
import { useState, useEffect } from "react";


function Todos() {
    const [todos, setTodos] = useState([]);
  
    // const queryClient = useQueryClient();
    // const { status, data } = useQuery("todos", fetchTodo);
  
    useEffect(() => {
      const fetchTodo = async () => {
        const response = await fetch("http://localhost:8000/todos/");
        const todos = await response.json();
        setTodos(todos)
      };
  
      fetchTodo();
    }, [])
  
   //if i fetch ("http://localhost:8000/todo/"). typo in address u see the below status;
    // if (status === "loading") {
    //   return <span>Loading...</span>;
    // }
  
    // if (status === "error") {
    //   return <span>Error</span>;
    // }
   
    return (
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>{todo.subject}</li>
        ))}
      </ul>
    );
  }
  
  export default Todos;
  