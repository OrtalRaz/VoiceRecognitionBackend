import React, {useState} from 'react';
import {useHistory} from 'react-router-dom';
import {createUser} from "../client";
import Input from "../common/Input";
import {HomeHeader} from "../common/MenuHeader";
import website_logo from '../pictures/website_logo.png';
import './HomePage.css';


const SignUpForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');

    const history = useHistory();

    const handleUsername = (event: React.ChangeEvent<HTMLInputElement>) => setUsername(event.target.value);
    const handlePassword = (event: React.ChangeEvent<HTMLInputElement>) => setPassword(event.target.value);
    const handleEmail = (event: React.ChangeEvent<HTMLInputElement>) => setEmail(event.target.value);

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        createUser(username, password, email)
            .then(user => alert(`User created with ID ${user.user_id}`))
            .then(() => history.push('/login'))
            .catch(error => alert(`Failed creating user: ${error.message}.`))
    }

    return (
        <form onSubmit={handleSubmit}>
            <Input title="Username" type="text" name="username" value={username} onChange={handleUsername}/>
            <Input title="Password" type="text" name="password" value={password} onChange={handlePassword}/>
            <Input title="Email" type="text" name="email" value={email} onChange={handleEmail}/>
            <input type="submit" value="Submit"/>
        </form>
    )
}


function SignUpPage() {
    return (
        <div className="Home">
            <header className="Home-header">
                <br/>
                <HomeHeader/>
                <br/>
                <img src={website_logo} alt="website logo" height={300} width={500}/>
                <br/>
                <SignUpForm/>
            </header>
        </div>
    );
}

export default SignUpPage;
