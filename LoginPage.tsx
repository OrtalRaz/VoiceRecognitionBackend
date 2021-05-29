import React, {useState} from 'react';
import {useHistory} from "react-router-dom";
import {login} from "../client";
import Input from "../common/Input";
import {HomeHeader} from "../common/MenuHeader";
import website_logo from '../pictures/website_logo.png';
import './HomePage.css';

interface LoginFormEventTarget extends HTMLInputElement {
    name: string
}

const LoginForm = () => {
    const [state, setState] = useState({username: '', password: ''});

    const history = useHistory();

    const handleChange = (event: React.ChangeEvent<LoginFormEventTarget>) => {
        const name = event.target.name;
        const value = event.target.value;
        setState({...state, [name]: value});
    }

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        login(state.username, state.password)
            .then(() => alert(`Logged in successfully!`))
            .then(() => history.push('/'))
            .catch(error => alert(`Failed logging in: ${error.message}.`))
    }

    return (
        <form onSubmit={handleSubmit}>
            <Input title="Username" type="text" name="username" value={state.username} onChange={handleChange}/>
            <Input title="Password" type="password" name="password" value={state.password} onChange={handleChange}/>
            <input type="submit" value="Log In"/>
        </form>
    );
}

function LoginPage() {
    return (
        <div className="Home">
            <header className="Home-header">
                <br/>
                <HomeHeader/>
                <br/>
                <img src={website_logo} alt="website logo" height={300} width={500}/>
                <br/>
                <LoginForm/>
            </header>
        </div>
    );
}

export default LoginPage;
