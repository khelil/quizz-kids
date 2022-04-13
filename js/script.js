window.addEventListener("load", function (event) {
  // console.log("Toutes les ressources sont chargées !");
  // const reader = new FileReader();
  // reader.onload = function (event) {
  //   console.log(event.target.result); // the CSV content as string
  // };
  dfd
    .readCSV("https://gitlab.com/evil.benos/choixpeau-magique/-/raw/main/Questions_choixpeau_magique.csv")
    .then((df) => {
      //do something like display descriptive statistics
      //df.describe().print();
      console.log(df);
    })
    .catch((err) => {
      console.log(err);
    });
});

// var btn = document.querySelector("form");
// var txt = document.querySelector("p");

// btn.addEventListener("click", updateBtn);

// // load csv character and caracteristic
