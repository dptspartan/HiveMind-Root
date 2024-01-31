import React from 'react'

export default function Post({ foundpost }) {
    const { id, user, caption, image, no_of_likes} = foundpost;
  return (
    <div>
        <p>{user}</p>
        <img src={`https://github.com/dptspartan/HiveMind-Root/blob/371156c82cb76c7c663cf1957946a4189cb3c978/HM_backend/media/${image}`} alt="Image Description" />
        <p>{caption}</p>
        <p>{no_of_likes}</p>
    </div>
  )
}
