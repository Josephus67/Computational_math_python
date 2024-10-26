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
    lidOpen : false,
    toggleLid : function(lidStatus) {
        this.lidOpen = lidStatus;
    }
}
//console.log(family)
console.log(family.nuclearFamily.children);
console.log(family.lidOpen);
console.log(family.toggleLid(true));
console.log(family.lidOpen);