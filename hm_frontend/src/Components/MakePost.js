import React, {useState, useContext} from 'react'
import { AuthContext } from '../AuthContext';
import axios from 'axios';

export default function MakePost() {
  const { user } = useContext(AuthContext);
  const [caption, setCaption] = useState('');
  const [image, setImage] = useState(null);

  const handleCaptionChange = (e) => {
    setCaption(e.target.value);
  };

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setImage(file);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // You can add your logic here to handle form submission (e.g., sending data to a server)
    // For a basic example, you can just log the form data to the console
    try{
      const data = {'user_id': user,
              'caption': caption,
              'image': image}
      const response = axios.post('http://127.0.0.1:8000/api/makePost/', data,
              {
                  headers: {
                      'Content-Type': 'application/json',
                  },
              }
              );
      console.log(response.data);
    }catch(error){
      console.error(error.response.data.message);
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
          accept="image/*"
          onChange={handleImageChange}
          required
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  )
}
