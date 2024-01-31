import React, {useState, useContext} from 'react'
import { AuthContext } from '../AuthContext';
import axios from 'axios';

export default function MakePost() {
  const { user } = useContext(AuthContext);
  const [caption, setCaption] = useState('');
  const [image, setImage] = useState(null);
  const [message, setMessage] = useState('')
  const handleCaptionChange = (e) => {
    setCaption(e.target.value);
  };

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setImage(file);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(image)
    // You can add your logic here to handle form submission (e.g., sending data to a server)
    // For a basic example, you can just log the form data to the console
    try{
      const formData = new FormData();
        formData.append('user_id', user);
        formData.append('caption', caption);
        formData.append('image', image);
      const response = axios.post('http://127.0.0.1:8000/api/makePost/', formData,
              {
                  headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                  },
              }
              );
      setMessage(['Posted'])
    }catch(error){
      setMessage('Unable to Post')
    }
  };
  return (
    <div className="App">
      <h2>Create a Post</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="caption">Caption:</label>
        <textarea
          id="caption"
          name="caption"
          rows="4"
          cols="50"
          value={caption}
          onChange={handleCaptionChange}
          required
        ></textarea>

        <label htmlFor="image">Image:</label>
        <input
          type="file"
          id="image"
          name="image"
          accept="image/jpeg,image/png,image/gif"
          onChange={handleImageChange}
          required
        />
        <button type="submit">Submit</button>
      </form>
      <p>{message}</p>
    </div>
  )
}
