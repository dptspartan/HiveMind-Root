import React, { useState, useContext } from 'react'
import axios from 'axios';
import SearchedUser from './SearchedUser';
import { AuthContext } from '../AuthContext';
import '../App.css'

export default function UserSearch() {
    const { user } = useContext(AuthContext);
    const [searchText, setSearchText] = useState('');
    const [searchResults, setSearchResults] = useState([]);
    const [showResult, setShowResult] = useState(false);
    const hideSearchResult = async (event) => {
        event.preventDefault(false)
        setShowResult(false)
    }
    const handle_userSearch = async(event) => {
        event.preventDefault()
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
            setSearchResults(response.data.Users);
            setShowResult(true)
        } catch (error) {
            setSearchResults([])
            setShowResult(false)
        }
    }
    return (
    <>
    <div id='top-bar'>
    <div id='searchbar'>
        <form onSubmit={handle_userSearch}>
        <input id='searchbar-text' type='text' placeholder='Username' onChange={(e) => {setSearchText(e.target.value)}} />
        <input id='searchbar-button' type='submit' value='🔍' />
        </form>

    </div>
    </div>
    { showResult?
    <div id='searchresult'>
    {searchResults.map((user) => (
        <SearchedUser key={user.id} founduser={user} />
        ))}
    
    <button id='searchResultHide' type='button' onClick={hideSearchResult} ><p>^</p></button>
    </div>: <></>
    }
    </>
  )
}
