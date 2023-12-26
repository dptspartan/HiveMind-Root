import React, { useState, useContext } from 'react'
import axios from 'axios';
import SearchedUser from './SearchedUser';
import { AuthContext } from '../AuthContext';

export default function UserSearch() {
    const { user } = useContext(AuthContext);
    const [searchText, setSearchText] = useState('');
    const [searchResults, setSearchResults] = useState([]);
    const handle_userSearch = async(event) => {
        event.preventDefault();
        try {
            const formData = new FormData();
            formData.append('searchText', searchText);
            formData.append('user', user);
            const response = await axios.post('http://127.0.0.1:8000/api/searchuser/', formData,
            {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
            }
            );
            console.log(response.data.Users);
            setSearchResults(response.data.Users);
        } catch (error) {
            console.error(error.response.data.message);
        }
    }
    return (
    <div>
        <h1>Add Friends</h1>
        <form onSubmit={handle_userSearch}>
            <input type='text' placeholder='Username' onChange={(e)=>setSearchText(e.target.value)} />
            <input type="submit" />
        </form>
        {searchResults.map((user) => (
        <SearchedUser key={user.id} founduser={user} />
      ))}
    </div>
  )
}
