import React, { useContext }  from 'react'
import Form from './Form'
import MainPage from './MainPage';
import { AuthContext } from '../AuthContext'

export default function MainSign() {
    const { isAuthenticated } = useContext(AuthContext);

    return (
        !isAuthenticated? <div className='mainsignup/in'><Form /></div> : <div><MainPage /></div>
      )


}
