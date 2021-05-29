import React from 'react';
import {LinkButton} from "../common/button/Button";
import website_logo from '../pictures/website_logo.png';
import './HomePage.css';

function HomePage() {
    return (
        <div className="Home">
            <header className="Home-header">
                <br/>
                <img src={website_logo} alt="website logo" height={300} width={500}/>
                <p>
                    WELCOME TO THE NEWS WEBSITE
                </p>
                <div className="column">
                    <LinkButton text="LOG IN" to='/login'/>
                </div>
                <div className="column">
                    <LinkButton text="SIGN UP" to='/signup'/>
                </div>
                <div className="column">
                    <LinkButton text="FORGOT MY PASSWORD" to='/restoring'/>
                </div>
                <div className="column">
                    <LinkButton text="CHANGE MY PASSWORD" to='/changing'/>
                </div>
            </header>
        </div>
    );
}

export default HomePage;
