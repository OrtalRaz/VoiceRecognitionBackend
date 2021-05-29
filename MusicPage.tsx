import React from 'react';
import './HomePage.css';
import '../common/image/ImagesRow.css';
import website_logo from "../pictures/website_logo.png";
import justinbieber from "../pictures/music/justinbieber.png";
import demilovato from "../pictures/music/demilovato.png";
import drake from "../pictures/music/drake.png";
import edenhason from "../pictures/music/edenhason.png";
import oliviarodrigo from "../pictures/music/oliviarodrigo.png";
import oshercohen from "../pictures/music/oshercohen.png";
import postmalone from "../pictures/music/postmalone.jpg";
import billieeilish from "../pictures/music/billieeilish.jpg";
import tatemcrae from "../pictures/music/tatemcrae.png";
import randanker from "../pictures/music/randanker.png";

import ImagesRow from "../common/image/ImagesRow";
import MenuHeader, {HomeHeader} from "../common/MenuHeader";

function MusicPage() {
    return (
        <div className="Home">
            <header className="Home-header">
                <br/>
                <HomeHeader/>
                <br/>
                <img src={website_logo} alt="website logo" height={100} width={150}/>
                <br/>
                <MenuHeader/>

                <h1> - MUSIC -  </h1>

                <h1> 2021 New Songs </h1>
                <p>
                    drivers license - Olivia Rodrigo |
                    what's next - Drake |
                    Hold On - Justin Bieber |
                    Dancing With the Devil - Demi Lovato |
                    bad ones - Tate MCrae |
                    בית משוגעים - רן דנקר |
                    גדל לי קצת זקן - עדן חסון |
                    אני אוהב אותך - אושר כהן |


                </p>
                <ImagesRow images={
                    [{src: justinbieber, name: "justin bieber", height: 200, width: 200},
                        {src: demilovato, name: "demi lovato", height: 200, width: 200},
                        {src: drake, name: "drake", height: 200, width: 200},
                        {src: edenhason, name: "eden hason", height: 200, width: 200}]
                }/>
                <ImagesRow images={
                    [{src: oliviarodrigo, name: "olivi arodrigo", height: 200, width: 200},
                        {src: oshercohen, name: "osher cohen", height: 200, width: 200},
                        {src: tatemcrae, name: "tatemcrae", height: 200, width: 200},
                        {src: randanker, name: "ran danker", height: 200, width: 200}]

                }/>

                <br/>
                <h1> אירועים קרובים </h1>
                <h1> בילי אייליש </h1>
                <img src={billieeilish} alt="billie eilish" height={300} width={500}/>
                <p> יום ד', 26 במאי - Sofia, בולגריה - Music Jam Club </p>
                <p> יום א', 30 במאי - Água Branca, São Paulo, ברזיל - Allianz Parque </p>
                <p> יום ו', 17 בספט' -  Las Vegas, NV, ארה"ב - Life is Beautiful Festival </p>
                <p> יום ו', 31 בדצמ' - Cologne, גרמניה - lanxess arena </p>

                <br/>
                <h1> Post Malone </h1>
                <img src={postmalone} alt="post malone" height={300} width={500}/>
                <p> יום א', 1 באוגוסט - Montreal, Quebec, קנדה - Parc Jean-Drapeau </p>
                <p> יום שבת, 28 באוגוסט - Reading, בריטניה - Reading Festival </p>
                <p> יום א', 29 באוגוסט - Bramham Lane, Wetherby, בריטניה - Bramham Park </p>
                <p> יום א', 13 במרץ - Ontario, CA, ארה"ב - Toyota Arena </p>

            </header>
        </div>
    );
}


export default MusicPage;