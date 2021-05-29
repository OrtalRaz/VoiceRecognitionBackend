import React from 'react';
import './HomePage.css';
import website_logo from '../pictures/website_logo.png';
import {HomeHeader} from "../common/MenuHeader";
import Input from "../common/Input";

type ChangingFormProps = {};
type ChangingFormState = {username: string, password: string, newPassword: string};
interface ChangingFormEventTarget extends HTMLInputElement {name: string}
class ChangingForm extends React.Component<ChangingFormProps, ChangingFormState> {
    constructor(props: ChangingFormProps) {
        super(props);
        this.state = {username: '', password: '', newPassword: ''}

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event: React.ChangeEvent<ChangingFormEventTarget>) {
        const name = event.target.name;
        const value = event.target.value;
        this.setState<never>({[name]: value});
    }

    handleSubmit(event: React.FormEvent) {
        event.preventDefault();
        alert(`Password is changed`);
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <Input title="Username" type="text" name="username" value={this.state.username} onChange={this.handleChange}/>
                <Input title="Password" type="text" name="password" value={this.state.password} onChange={this.handleChange}/>
                <Input title="New Password" type="text" name="newPassword" value={this.state.newPassword} onChange={this.handleChange}/>
                <input type="submit" value="Submit" />
            </form>
        );
    }
}

function ChangingPage() {
    return (
        <div className="Home">
            <header className="Home-header">
                <br/>
                <HomeHeader/>
                <br/>
                <img src={website_logo} alt="website logo" height={300} width={500}/>
                <br/>
                <ChangingForm/>
            </header>
        </div>
    );
}

export default ChangingPage;
