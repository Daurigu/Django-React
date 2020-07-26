import React from 'react'

function TweetForm(props){

    let formatTweet = (value) => {
        return(
            {
                id: 123214,
                content: value
            }
        )
    }

    let formRef = React.createRef()
    let formHandeler = (event) =>{
        event.preventDefault()

        console.log(event)
        console.log(formRef.current.value)
        console.log(formatTweet(formRef.current.value))
        
        props.parentCallback(formatTweet(formRef.current.value))
        formRef.current.value = ''
    }

    return <div className='rounded m-3'>
        <form  onSubmit={formHandeler} >
            <textarea ref={formRef} required={true} name="Tweet" className='form-control'></textarea>
            <button type="submit" className='btn btn-outline-success m-3'>Tweet</button>
        </form>
    </div>

}

export default TweetForm