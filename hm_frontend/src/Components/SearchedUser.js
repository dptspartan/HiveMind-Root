import React, { useState, useContext } from 'react'
import axios from 'axios';
import { AuthContext } from '../AuthContext';

export default function SearchedUser({founduser}) {
    const { user } = useContext(AuthContext);
    const { id, username, first_name, last_name, friend_status} = founduser;
    const [frndsStatus, setFrndStatus] = useState(friend_status);
    const handle_addFriend = async(event) => {
        event.preventDefault()
        console.log(frndsStatus)
        if (friend_status === 'Add Friend'){
            try {
                const formData = new FormData();
                formData.append('from_user', user);
                formData.append('to_user', id);
                const response = await axios.post('http://127.0.0.1:8000/api/sendfriendRequest/', formData,
                {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                }
                );
                setFrndStatus("Request Sent");
            } catch (error) {
                console.error(error.response.data.message);
            }
        }
    }
    return (
        <div id='searchedUser'>
            <h4>{username} </h4>
            <button onClick={handle_addFriend}>{frndsStatus}</button>
            <br id='break' />
        </div>
    )
}
