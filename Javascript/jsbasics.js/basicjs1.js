family = {
    nuclearFamily: {
        father : "Musah",
        mother : "Bertha",
        children : {
            sons : {
                firstSon: "Josephus",
                secondSon : "Romanus"
            },
            daugthers : {
                firstDaughter : "Keren",
                secondDaughter : "Immaculate",
            }
        }
    },
    lidOpen : false ,
    toggleLid  : function (lidStatus) {
        this.lidOpen = lidStatus
    }
}
//console.log(family)
/*
console.log(family.nuclearFamily.children);
console.log(family.lidOpen);
console.log(family.toggleLid(true));
console.log(family.lidOpen);
*/
//classes

class backPack {
    constructor(
        name,
        color,
        volume,
        pocketNum,
        pocketSize,
        strapLengthR,
        strapLengthL,
        dateAcquired
    ){
        this.name = name;
        this.color = color;
        this.volume = volume;
        this.pocketNum = pocketNum;
         this.pocketSize = pocketSize;
        this.strapLengthR = strapLengthR;
        this.strapLengthL = strapLengthL;
        this.dateAcquired = dateAcquired;
    }
    backPackAge(){
        let now = new Date();
        let acquired = new Date(this.dateAcquired)
        let elapsed = now.getTime() - acquired.getTime();
        let daysAcquired = Math.floor(elapsed/(10000*3600*24));
        return daysAcquired
    }

}

const everydayPack = new backPack(
    "everyday Back Pack",
    "grey",
    30,
    60,
    90,
    5,
    6,
    "December 5,2010 15:00:00 UTC",
);

//console.log(everydayPack);
//console.log(everydayPack.color);

//Date
const dateToday = new Date();
console.log(dateToday);
console.log(dateToday.toDateString());
console.log(dateToday.getDate());
console.log(everydayPack.dateAcquired);
console.log(everydayPack.backPackAge());