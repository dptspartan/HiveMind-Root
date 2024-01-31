import React from 'react'

export default function Post({ foundpost }) {
    const { id, user, caption, image, no_of_likes} = foundpost;
  return (
    <div>
        <p>{user}</p>
        <img src={`http://127.0.0.1:8000/media/${image}`} alt="Image Description" />
        <p>{caption}</p>
        <p>{no_of_likes}</p>
    </div>
  )
}
