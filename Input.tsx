import React, {ChangeEventHandler} from 'react';
import '../common/button/Button.css'

type InputProps = {title: string, type: string, name: string, value: any, onChange: ChangeEventHandler};
function Input(props: InputProps) {
    return (
        <label>
            {props.title}: <input type={props.type} name={props.name} value={props.value} onChange={props.onChange}/>
            <br/>
        </label>
    )
}

export default Input;
