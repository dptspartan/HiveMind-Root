import React, { useState } from 'react';
import axios from 'axios';

export default function Register() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const handle_login = async (event) => {
        event.preventDefault();
        try {
            const formData = new FormData();
            formData.append('username', username);
            formData.append('password', password);
            formData.append('email', email);
            formData.append('first_name', firstName);
            formData.append('last_name', lastName)
            const response = await axios.post('http://127.0.0.1:8000/api/register/', formData,
            {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
            }
            );

            console.log(response.data.message);
        } catch (error) {
            console.error(error.response.data.message);
        }
    };
    return (
    <div id="login-container">
    <div id="login-header">
      <h1>Register Form</h1>
      </div>
        <form id="login-form" onSubmit={handle_login}>
            <label>Username</label>
            <input type='text' placeholder='Username' onChange={(e)=>setUsername(e.target.value)} />
            <label>Password</label>
            <input type='text' placeholder='Password' onChange={(e)=>setPassword(e.target.value)} />
            <label>FirstName</label>
            <input type='text' placeholder='First Name' onChange={(e)=>setFirstName(e.target.value)} />
            <label>LastName</label>
            <input type='text' placeholder='Last Name' onChange={(e)=>setLastName(e.target.value)} />
            <label>Email</label>
            <input type='text' placeholder='E-mail' onChange={(e)=>setEmail(e.target.value)} />
            <button type="submit">Register</button>
        </form>
    </div>

  )
}

