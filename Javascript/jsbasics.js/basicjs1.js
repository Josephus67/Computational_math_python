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
    ){
        this.name = name;
        this.color = color;
        this.volume = volume;
        this.pocketNum = pocketNum;
         this.pocketSize = pocketSize;
        this.strapLengthR = strapLengthR;
        this.strapLengthL = strapLengthL;
    }

}

const everydayPack = new backPack(
    "everyday Back Pack",
    "grey",
    30,
    60,
    90,
    5,
    6
);

console.log(everydayPack);
console.log(everydayPack.color);