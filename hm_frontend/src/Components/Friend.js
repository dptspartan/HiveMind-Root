import React from 'react'
import axios from 'axios';

export default function FriendReqs({ foundfriend }) {
    const { id, username, first_name, last_name} = foundfriend;
  return (
    <div>
        <h1>{username}</h1>
        <p>{first_name} {last_name}</p>
    </div>
  )
}
