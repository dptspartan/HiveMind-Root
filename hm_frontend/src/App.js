import React, { useState, useContext } from 'react';
import MainSign from './Components/MainSign';
import { UserAuthProvider } from './AuthContext';


function App() {
  //const { isAuthenticated, user } = useContext(AuthContext);
  return (
    <>
    <UserAuthProvider>
      <MainSign />
    </UserAuthProvider>
    </>
  );
}

export default App;