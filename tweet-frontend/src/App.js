import React, {useState, useEffect} from 'react';
import './App.css';

const xhrHandeler = (callback) => {
  const xhr = new XMLHttpRequest()
  const method = 'GET'
  const url = 'something'
  const typeResp = 'JSON'

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

function App() {
  const [tweet, setTweet] = useState([])

  useEffect( () => {
    const callback = (response, status) =>{
      if(status == 200){
        setTweet(response)
      }
      else{
        console.log('There was an error, please try again')
      }
      
    }
    xhrHandeler(callback)

  }, [] )

  return (
    <div className="App">
      {tweet}
    </div>
  );
}

export default App;
