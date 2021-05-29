import React from 'react';
import './HomePage.css';
import '../common/image/ImagesRow.css';
import website_logo from "../pictures/website_logo.png";

import masada1 from "../pictures/travel/masada1.jpg";
import masada2 from "../pictures/travel/masada2.jpg";
import masada3 from "../pictures/travel/masada3.jpg";
import museum1 from "../pictures/travel/museum1.jpg";
import museum2 from "../pictures/travel/museum2.jpg";
import museum3 from "../pictures/travel/museum3.jpg";
import reserve1 from "../pictures/travel/reserve1.jpg";
import reserve2 from "../pictures/travel/reserve2.jpg";
import dubai1 from "../pictures/travel/dubai1.jpg";
import dubai2 from "../pictures/travel/dubai2.jpg";
import netherlands1 from "../pictures/travel/netherlands1.jpg";
import netherlands2 from "../pictures/travel/netherlands2.jpg";
import rome1 from "../pictures/travel/rome1.jpg";
import rome2 from "../pictures/travel/rome2.jpg";

import ImagesRow from "../common/image/ImagesRow";
import MenuHeader, {HomeHeader} from "../common/MenuHeader";

function TravelPage() {
    return (
        <div className="Home">
            <header className="Home-header">
                <br/>
                <HomeHeader/>
                <br/>
                <img src={website_logo} alt="website logo" height={100} width={150}/>
                <br/>
                <MenuHeader/>

                <h1> - TRAVEL - </h1>

                <h1> אטרקציות בישראל </h1>
                <p> גן לאומי מצדה </p>
                <ImagesRow images={
                    [{src: masada1, name: "masada", height: 280, width: 400},
                        {src: masada2, name: "masada", height: 280, width: 400},
                        {src: masada3, name: "masada", height: 280, width: 400}]
                }/>
                <br/>

                <p> מוזיאון ישראל </p>
                <ImagesRow images={
                    [{src: museum1, name: "museum", height: 270, width: 410},
                        {src: museum2, name: "museum", height: 270, width: 410},
                        {src: museum3, name: "museum", height: 270, width: 410}]
                }/>
                <br/>

                <p> שמורת עין גדי </p>
                <ImagesRow images={
                    [{src: reserve1, name: "reserve", height: 180, width: 370},
                        {src: reserve2, name: "reserve", height: 180, width: 370}]
                }/>
                <br/>

                <h1>אתרי תיירות בחו"ל </h1>
                <p> רייקסמוזיאום - הולנד </p>
                <ImagesRow images={
                    [{src: netherlands1, name: "netherlands", height: 180, width: 370},
                        {src: netherlands2, name: "netherlands", height: 180, width: 370}]
                }/>
                <p> מוזיאון אומנות </p>
                <br/>

                <p> קולוסיאום - איטליה </p>
                <ImagesRow images={
                    [{src: rome1, name: "rome", height: 180, width: 370},
                        {src: rome2, name: "rome", height: 180, width: 370}]
                }/>
                <p> זירת גלדיאטורים רומית עתיקה </p>
                <br/>

                <p> בורג' ח'ליפה - דובאי </p>
                <ImagesRow images={
                    [{src: dubai1, name: "dubai", height: 180, width: 370},
                        {src: dubai2, name: "dubai", height: 180, width: 370}]
                }/>
                <p> גורד השחקים הגבוה בעולם </p>
                <br/>


            </header>
        </div>
    );
}

export default TravelPage;