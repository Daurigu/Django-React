import React, {useEffect} from 'react'
import Button from './Button'

function TweetLayout(props) {
  //const [tweet, setTweet] = useState([])

  let button = {
    name:'Like',
    unName: 'Unlike',
    action:'like'
  }

  let buttonRt = {
    name:'Retweet',
    unName: 'DeRetweet',
    action:'Retweet'
  }


  return (
    <div id='TweetLayout'>

      <div className='m-3 rounded bg-dark shadow'>

        <div className='row p-1'>
          <div className='col text-light'>
            {props.id} - {props.content}
          </div>
        </div>
        <div className='row btn btn-group' >
          <Button props={button}/>
          <Button props={buttonRt}/>
        </div>
        
      </div>

    </div>
  );
}

export default TweetLayout;