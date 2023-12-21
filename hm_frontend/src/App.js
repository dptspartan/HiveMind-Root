import React, { useState, useContext } from 'react';
import MainSign from './Components/MainSign';
import { UserAuthProvider } from './AuthContext';
import HelloWorld from "./Components/HelloWorld"

function App() {
  //const { isAuthenticated, user } = useContext(AuthContext);
  return (
    <UserAuthProvider>
      <MainSign />
    </UserAuthProvider>
  );
}

export default App;