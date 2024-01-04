import React from 'react'
import axios from 'axios';

export default function FriendReqs({ foundrequest }) {
    const { id, request_from} = foundrequest;
    const handle_accept = async(event) => {
      event.preventDefault();
      try {
          const formData = new FormData();
          formData.append('request_to_accept', id);
          const response = await axios.post('http://127.0.0.1:8000/api/acceptRequest/', formData,
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
  }
  return (
    <div>
        <p>Request From: {request_from}</p>

            <button onClick={handle_accept}>Accept</button>
    </div>
  )
}
