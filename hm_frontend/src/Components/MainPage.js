import React, {useState, useEffect, useContext} from 'react'
import UserSearch from './UserSearch'
import FriendReqs from './FriendReqs'
import MakePost from './MakePost'
import Friend from './Friend'
import axios from 'axios'
import { AuthContext } from '../AuthContext'


export default function MainPage() {
  const [seefrndReqs, setSeefrndReqs] = useState(false)
  const [friendRequests, setFriendRequests] = useState([]);
  const [friends, setFriends] = useState([]);
  const { user } = useContext(AuthContext);

  useEffect(()=> {
    const fetchFriendRequest = async () => {
      const formData = new FormData();
      formData.append('user_id', user);
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/getfriendRequest/', formData,
            {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
            }
            );
        console.log(response.data);
        setFriendRequests(response.data.requests);
      } catch (error) {
        console.error(error.response.data.message);
      }
    };
    const fetchFriends = async () => {
      const formData = new FormData();
      formData.append('user_id', user);
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/myFriends/', formData,
            {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
            }
            );
        console.log(response.data);
        setFriends(response.data.friends);
      } catch (error) {
        console.error(error.response.data.message);
      }
    };

    // Call the fetchUserData function when the component mounts
    fetchFriendRequest();
    fetchFriends();
  }, [])
  return (
    <>
      <UserSearch />
      <div id='mainpage'>
        <button onClick={()=>{setSeefrndReqs(!seefrndReqs)}}>Friend Requests</button>
        {seefrndReqs? <div>
          {friendRequests.map((request) => (
          <FriendReqs key={request.id} foundrequest={request} />
          ))}
        </div> : <></>}
        <div className='Friends'>
          {friends.map((friend) => (
          <Friend key={friend.id} foundfriend={friend} />
          ))}
        </div>
        <MakePost />
    </div>
    </>
  )
}
