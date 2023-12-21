import React, { useState } from 'react';
import Login from './Login';
import Register from './Register';

export default function Form() {
    const [togglesignin, setTogglesignin] = useState(true);
  return (
    <div>
        <button onClick={() => {setTogglesignin(true)}}>Login</button>
        <button onClick={() => {setTogglesignin(false)}}>Register</button>
        {togglesignin ? <Login /> : <Register />}
    </div>
  )
}
