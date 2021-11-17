import Todos from './components/Todos';
import './App.css';
import { useState, useEffect } from "react"
import { Route} from "react-router-dom";
import Form from './pages/Form';

function App(props) {
  
  const url = "http://localhost:8000/todos/"

  const [posts, setPosts] = useState([]);

  const [token, setToken] = useState('')
  // const queryClient = useQueryClient();
  // import { useQueryClient } from "react-query";
  const login = async (username, password) => {
    const response = await fetch("http://localhost:8000/api/token/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        password,
      }),
    });

    const data = await response.json();
    //console.log(data)
    setToken(data.access);
  };

// Function to get list of Todos from API
const getTodos = async () => {
  const response = await fetch(url);
  const data = await response.json();
  setPosts(data);
};

//////////////
// useEffects
//////////////

// useEffect to get list of todos when page loads
useEffect(() => {
  getTodos();
}, []);
  
  
  const addTodo = async () => {
    const body = JSON.stringify({
      subject: "Test", details: "New todo"
    });

    await fetch("http://localhost:8000/todos/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
      },
      body,
    }); 
  }

  const deleteTodo = async () => {
    await fetch("http://localhost:8000/todos/10", {
      method: "delete",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
      },
     
    }); 
  }

  return (
    <div className="App">
      
    <h1>Todos</h1>
      <button onClick={() => login("admin", process.env.REACT_APP_NOT_SECRET_CODE)}>Login</button>
        <Todos/>
        {/* <Route
          exact
          path="/new"
          render={(routerProps) => <Form {...routerProps} posts={posts} />}
        /> */}
      <button onClick={() => addTodo()}>Add</button>
      <button onClick={() => deleteTodo()}>Delete</button>
    
    </div>
  );
}

export default App;
