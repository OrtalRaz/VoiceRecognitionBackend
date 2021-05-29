import React from 'react';
import './HomePage.css';
import website_logo from '../pictures/website_logo.png';
import {HomeHeader} from "../common/MenuHeader";
import Input from "../common/Input";

type RestoringFormProps = {};
type RestoringFormState = {email: string};
interface RestoringFormEventTarget extends HTMLInputElement {name: string}
class RestoringForm extends React.Component<RestoringFormProps, RestoringFormState> {
    constructor(props: RestoringFormProps) {
        super(props);
        this.state = {email: ''}

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event: React.ChangeEvent<RestoringFormEventTarget>) {
        const name = event.target.name;
        const value = event.target.value;
        this.setState<never>({[name]: value});
    }

    handleSubmit(event: React.FormEvent) {
        event.preventDefault();
        alert(`New password will be sent to the email: ${this.state.email}`);
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <Input title="Email" type="text" name="email" value={this.state.email} onChange={this.handleChange}/>
                <input type="submit" value="Submit" />
            </form>
        );
    }
}
function RestoringPage() {
    return (
        <div className="Home">
            <header className="Home-header">
                <br/>
                <HomeHeader/>
                <br/>
                <img src={website_logo} alt="website logo" height={300} width={500}/>
                <br/>
                <RestoringForm/>
            </header>
        </div>
    );
}

export default RestoringPage;
