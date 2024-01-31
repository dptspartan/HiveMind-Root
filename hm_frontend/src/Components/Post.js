import React from 'react'

export default function Post({ foundpost }) {
    const { id, user, username, caption, image, no_of_likes} = foundpost;
  return (
    <div>
        <p>{username}</p>
        <img src={`http://127.0.0.1:8000${image}`} alt="Image Description" />
        <p>{caption}</p>
        <p>{no_of_likes}</p>
    </div>
  )
}
