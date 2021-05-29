import React from 'react';
import {Link} from 'react-router-dom';
import '../button/Button.css';


type ButtonProps = { text: string };

function Button(props: ButtonProps) {
    return <button>{props.text}</button>
}

type LinkButtonProps = { text: string, to: string };

function LinkButton(props: LinkButtonProps) {
    return (
        <Link to={props.to}>
            <Button text={props.text}/>
        </Link>
    )
}


type SideLinkButtonProps = { text: string, to: string };

function SideLinkButton(props: SideLinkButtonProps) {
    return (
        <Link to={props.to}>
            <Button text={props.text}/>
        </Link>
    )
}

export {LinkButton, SideLinkButton};