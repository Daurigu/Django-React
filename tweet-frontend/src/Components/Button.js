import React, {useState} from 'react'

function Button(props){
    const [amount, setAmount] = useState(0)
    const [like, setLike] = useState(false)

    let likeUnlike = () =>{
        if (like){
            setAmount(amount - 1)
            setLike(false)
        }
        else{
            setAmount(amount + 1)
            setLike(true)
        }
    }

    return(
        <div className=''>
            <button className=' btn btn-outline-success '  type="submit" onClick={likeUnlike}> 
                {props.props.name === 'Like' ? amount : null } 
                {like ? props.props.unName: props.props.name}
            </button>
        </div>  
    )
}


export default Button