import React, { useState } from 'react';
import Login from './Login';
import Register from './Register';

import '../App.css'; 
export default function Form() {
    const [togglesignin, setTogglesignin] = useState(true);
  return (
    <div>
            <nav id="navbar">
            <h1><img id="navbar img" src="./images.png" alt="hey" /> Hivemind</h1>
            </nav>
    <div>
         {togglesignin ? <Login /> : <Register />}
         <div style={{ textAlign: 'center' }}>
         <p >Create a new account</p>
        <button id="button" onClick={() => {setTogglesignin(false)}}>Register</button>
        </div>
        
    </div>
    </div>
  )
}
