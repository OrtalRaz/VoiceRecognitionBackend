import React from 'react';
import './HomePage.css';
import '../common/image/ImagesRow.css';
import website_logo from "../pictures/website_logo.png";
import corona_israel from "../pictures/corona/coronaisrael.png"
import tav from "../pictures/corona/tav.png"
import tav2 from "../pictures/corona/tav2.png"
import corona1 from "../pictures/corona/corona1.png"
import corona2 from "../pictures/corona/corona2.png"
import ImagesRow from "../common/image/ImagesRow";
import MenuHeader, {HomeHeader} from "../common/MenuHeader";


function CoronaPage() {
    return (
        <div className="Home">
            <header className="Home-header">
                <br/>
                <HomeHeader/>
                <br/>
                <img src={website_logo} alt="website logo" height={100} width={150}/>
                <br/>
                <MenuHeader/>


                <h1> - CORONA -  </h1>
                <img src={corona_israel} alt="corona" height={300} width={700}/>

                <h1> הדרכון הירוק - כל מה שצריך לדעת </h1>
                <p>
                    החל מ-21 בפברואר המשק חוזר לפעילות נרחבת בכפוף ל"תו הסגול" -
                    מקומות שייפתחו לקהל הרחב תחת הגבלות הקורונה. אפליקציית "רמזור" של משרד הבריאות
                    כבר ניתנת להורדה וכעת אפשר להנפיק באמצעותה "אישור מעבר" שאיתו תוכלו להיכנס
                    למלונות, חדרי כושר, אירועי ספורט ותרבות, בריכות שחייה, מסעדות ועוד.
                </p>

                <ImagesRow images={
                    [{src: tav, name: "tav", height: 200, width: 420},
                        {src: tav2, name: "tav", height: 350, width: 420}]
                }/>

                <p>
                    מי זכאי לתו הירוק? - מתחסנים החל משבוע לאחר החיסון השני,
                    מחלימים בעלי תעודת החלמה. התעודה תונפק לכל מי שהוגדר כמחלים ותהיה בתוקף עד 30.6.2021
                </p>
                <br/>
                <p>
                    איך מציגים את התו הירוק? - כל מי שהתחסן או החלים צריך להוריד את אפליקציית "רמזור" של משרד הבריאות,
                    להזין בה את פרטיו האישיים - וכעבור פרק זמן של כחצי דקה, יונפק אישור מעבר.
                    ברגע שתרצו להשתתף בפעילות כלשהי שמחייבת תו ירוק, הציגו את האישור לסדרן לצד תעודת זהות
                </p>
                <br/>
                <p>
                    מה נותן התו הירוק? - מלבד ההקלות שיתפרסמו מדי שבוע, נושאי התו הירוק פטורים
                    מבידוד לאחר מפגש עם חולה או בחזרה מחו"ל.
                </p>

                <br/>
                <h1> השלב ה-3 של ההקלות: מה ייפתח בראשון ומי יוכל להיכנס? </h1>
                <p>
                    למרות התנגדות גורמי המקצוע במשרד הבריאות, הממשלה אישרה אתמול (שני) שהפעימה השלישית של ההקלות
                    באסטרטגיית היציאה מההגבלות תיכנס לתוקף החל מיום ראשון הקרוב, 7 במרץ. במקביל,
                    אישרה הממשלה קיום כנסים פוליטיים תחת התו הירוק באופן מיידי, 5 ימים לפני שתותר פתיחת המסעדות.
                </p>
                <br/>
                <p>
                    מערכת החינוך - בנוסף לשאר תלמידי מערכת החינוך שחזרו לספסל הלימודים, החל מיום ראשון תלמידי כיתות
                    ז' עד י' ישובו למוסדות החינוך בערים ירוקות וצהובות. גם בערים כתומות שבהן 70% מחוסנים
                    תאושר החזרה ללימודים.
                </p>
                <br/>
                <p>
                    התקהלויות - החל מיום ראשון הקרוב, בערים ירוקות, צהובות וכתומות יהיה ניתן לקיים התקהלויות מכל סוג
                    שהוא עד 20 איש בפנים ו-50 בחוץ. לעומת זאת, הערים האדומות יישארו עם ההגבלה שהייתה קיימת
                    עד היום מאז היציאה מהסגר: כלומר 20 בני אדם בשטח פתוח ורק עד עשרה במקום סגור.
                </p>
                <ImagesRow images={
                    [{src: corona1, name: "Corona", height: 320, width: 420},
                        {src: corona2, name: "Corona", height: 320, width: 420}]
                }/>
                <br/>

            </header>
        </div>
    );
}

export default CoronaPage;