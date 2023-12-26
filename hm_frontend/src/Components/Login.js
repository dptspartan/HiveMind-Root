import React, { useState, useContext } from 'react';
import axios from 'axios';
import { AuthContext } from '../AuthContext';



function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const {setIsAuthenticated, setUser} = useContext(AuthContext);
    const handle_login = async (event) => {
        event.preventDefault();
        try {
            const formData = new FormData();
            formData.append('username', username);
            formData.append('password', password);
            const response = await axios.post('http://127.0.0.1:8000/api/login/', formData,
            {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
            }
            );
            const out = response.data;
            console.log(out.user)
            setUser(out.user)
            setIsAuthenticated(true)
        } catch (error) {
            console.error(error.response.data.message);
        }
    };
    return (
    <div>
        <h1>Login</h1>
        <form onSubmit={handle_login}>
            <input type='text' placeholder='Username' onChange={(e)=>setUsername(e.target.value)} />
            <input type='text' placeholder='Password' onChange={(e)=>setPassword(e.target.value)} />
            <input type="submit" />
        </form>
    </div>
  )
}
export default Login;
