import React, {useState, useEffect} from 'react';
import './App.css';
import TweetLayout from './Components/TweetLayout';
import TweetForm from './Components/TweetForm/TweetForm'

const xhrHandeler = (callback) => {
  const xhr = new XMLHttpRequest()
  const method = 'GET'
  const url = 'http://localhost:8000/api/alltweets'
  const typeResp = 'json'

  xhr.responseType = typeResp
  xhr.open(method, url)
  xhr.onload = () => {
    callback(xhr.response, xhr.status)
  }
  xhr.onerror = () => {
    callback({message: 'there was an error, please try again'}, xhr.status)
  }

  xhr.send()
}


//-------------------------------------------
//----------------- APP ---------------------
//-------------------------------------------

function App() {
  const [tweet, setTweet] = useState([])

  useEffect( () => {
    const callback = (response, status) =>{
      if(status === 200){
        console.log('connection created')
        setTweet(response)
      }
      else{
        console.log(response.message)
        setTweet('Nada Loko')
      }
      
    }
    xhrHandeler(callback)

  }, [] )


  return (
    <div className="App container">
    

      <TweetForm parentCallback={event => setTweet(tweet.concat(event))}/>
      {tweet.map( (item)=> {
        return <TweetLayout id={item.id} content={item.content} />
      })}
 
      
    </div>
  )
}

export default App;
