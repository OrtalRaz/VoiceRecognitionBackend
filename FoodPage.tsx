import React from 'react';
import './HomePage.css';
import '../common/image/ImagesRow.css';
import website_logo from "../pictures/website_logo.png";
import dessert1 from "../pictures/food/dessert1.png";
import dessert1r from "../pictures/food/dessert1r.png";
import dessert1i from "../pictures/food/dessert1i.png";
import dessert2 from "../pictures/food/dessert2.png";
import dessert2r from "../pictures/food/dessert2r.png";
import dessert2i from "../pictures/food/dessert2i.png";
import dessert3 from "../pictures/food/dessert3.png";
import dessert3r from "../pictures/food/dessert3r.png";
import dessert3i from "../pictures/food/dessert3i.png";
import chef1 from "../pictures/food/chef1.jpg";
import chef2 from "../pictures/food/chef2.jpg";
import chef3 from "../pictures/food/chef3.jpg";
import ImagesRow from "../common/image/ImagesRow";
import MenuHeader, {HomeHeader} from "../common/MenuHeader";

function FoodPage() {
    return (
        <div className="Home">
            <header className="Home-header">
                <br/>
                <HomeHeader/>
                <br/>
                <img src={website_logo} alt="website logo" height={100} width={150}/>
                <br/>
                <MenuHeader/>

                <h1> - FOOD -  </h1>

                <h1> מתכונים לעוגיות </h1>
                <p> עוגיות שוקולד צ'יפס </p>
                <ImagesRow images={
                    [{src: dessert1i, name: "עוגיות שוקולד צ'יפס - מצרכים", height: 280, width: 400},
                        {src: dessert1, name: "עוגיות שוקולד צ'יפס", height: 280, width: 400},
                        {src: dessert1r, name: "עוגיות שוקולד צ'יפס - מתכון", height: 280, width: 400}]
                }/>
                <br/>

                <p> עוגיות שיבולת שועל </p>
                <ImagesRow images={
                    [{src: dessert2i, name: "עוגיות שיבולת שועל - מצרכים", height: 270, width: 410},
                        {src: dessert2, name: "עוגיות שיבולת שועל", height: 270, width: 410},
                        {src: dessert2r, name: "עוגיות שיבולת שועל - מתכון", height: 270, width: 410}]
                }/>
                <br/>

                <p> עוגיות טחינה וחמאת בוטנים </p>
                <ImagesRow images={
                    [{src: dessert3i, name: "עוגיות טחינה וחמאת בוטנים - מצרכים", height: 180, width: 370},
                        {src: dessert3, name: "עוגיות טחינה וחמאת בוטנים", height: 180, width: 370},
                        {src: dessert3r, name: "עוגיות טחינה וחמאת בוטנים - מתכון", height: 180, width: 370}]
                }/>
                <br/>

                <h1> מסעדות שף מומלצות </h1>
                <img src={chef1} alt="chef" height={200} width={1200}/>
                <img src={chef2} alt="chef" height={200} width={1200}/>
                <img src={chef3} alt="chef" height={200} width={1200}/>
                <br/>


            </header>
        </div>
    );
}


export default FoodPage;