import React, { useContext }  from 'react'
import Form from './Form'
import { AuthContext } from '../AuthContext'

export default function MainSign() {
    const { isAuthenticated } = useContext(AuthContext);

    return (
        !isAuthenticated? <div className='mainsignup/in'><Form /></div> : <div>Loged in</div>
      )


}
