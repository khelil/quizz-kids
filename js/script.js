// transforme Caracteristiques_des_persos.csv en tableau
// retourne le tableau
var caracteristics_index_name = [];
function get_caracteristics() {
  var persos = [];
  return dfd
    .readCSV("https://raw.githubusercontent.com/khelil/quizz-kids/master/datas/Caracteristiques_des_persos.csv")
    .then((df) => {
      for (var i = 0; i < df.$data.length; i++) {
        var caracteristics = {};
        for (var j = 0; j < df.$columns.length; j++) {
          caracteristics[df.$columns[j]] = df.$data[i][j];
        }
        persos.push(caracteristics);
      }
      persos.forEach((perso) => {
        caracteristics_index_name[perso["Name"]] = { Courage: perso["Courage"], Ambition: perso["Ambition"], Intelligence: perso["Intelligence"], Good: perso["Good"] };
      });
    })
    .catch((err) => {
      console.log(err);
    });
}

// transforme Characters.csv en tableau
// retourne le tableau
var persos_index_name = [];
function get_csv_persos() {
  var persos = [];
  return dfd
    .readCSV("https://raw.githubusercontent.com/khelil/quizz-kids/master/datas/Characters.csv")
    .then((df) => {
      for (var i = 0; i < df.$data.length; i++) {
        var caracteristics = {};
        for (var j = 0; j < df.$columns.length; j++) {
          caracteristics[df.$columns[j]] = df.$data[i][j];
        }
        persos.push(caracteristics);
      }
      persos_index_name = {};
      persos.forEach((perso) => {
        persos_index_name[perso["Name"]] = { House: perso["House"] };
      });
    })
    .catch((err) => {
      console.log(err);
    });
}

// calcul la distance euclidienne entre deux persos
// retourne la distance
function calc_distance(perso1, perso2) {
  return Math.sqrt((parseInt(perso1["Courage"]) - parseInt(perso2["Courage"])) ** 2) + (parseInt(perso1["Ambition"]) - parseInt(perso2["Ambition"])) ** 2 + (parseInt(perso1["Intelligence"]) - parseInt(perso2["Intelligence"])) ** 2 + (parseInt(perso1["Good"]) - parseInt(perso2["Good"])) ** 2;
}

// calcul la distance euclidienne entre un perso inconnu
// et la liste des persos d'un dict
// retourne un nouveau dict avec une prop distance
function ajout_distance(persos, perso_inconnu) {
  Object.entries(persos).forEach(([index, perso]) => {
    persos[index]["Distance"] = calc_distance(perso_inconnu, persos[index]);
  });
  return persos;
}

// renvoi la liste des kppv
// retourne un tableau
function get_kppv(persos, nbre_voisin) {
  nbre_voisin = parseInt(nbre_voisin);
  liste_voisins = [];
  persos_array = [];
  // on crée un tableau avec uniquement pour le tri
  Object.entries(persos).forEach(([index, perso]) => {
    persos_array.push({ name: index, distance: perso["Distance"], House: perso["House"] });
  });
  // on trie
  persos_array.sort(function (a, b) {
    return a.distance - b.distance;
  });
  return persos_array.slice(0, nbre_voisin);
}

// renvoi la meilleure distance
function meilleur_distance(persos) {
  distances = [];
  persos.forEach((perso) => {
    distance = parseInt(perso["distance"]);
    if (distances[distance]) {
      distances[distance] += 1;
    } else {
      distances[distance] = 1;
    }
  });
  //console.log(distances);
  max = 0;
  best_distance = 0;
  Object.entries(distances).forEach(([distance, nbre]) => {
    if (nbre > max) {
      max = nbre;
      best_distance = distance;
    }
  });
  return best_distance;
}

var questions = [];
function get_questions() {
  return dfd
    .readCSV("https://raw.githubusercontent.com/khelil/quizz-kids/master/datas/Questions_choixpeau_magique.csv")
    .then((df) => {
      for (var i = 0; i < df.$data.length; i++) {
        var question = {};
        for (var j = 0; j < df.$columns.length; j++) {
          let column_name = df.$columns[j].trim();
          column_name = column_name.replace(/"/g, "");
          question[column_name] = df.$data[i][j];
        }
        questions.push(question);
      }
    })
    .catch((err) => {
      console.log(err);
    });
}

function create_questions(questions) {
  Object.entries(questions).forEach(([index, value]) => {
    questions_container = document.getElementById("questions");
    //
    question_container = document.createElement("div");
    question_container.id = "question-" + index;
    question_container.classList.add("my-4");
    question_title = document.createElement("h2");
    question_title.classList.add("text-2xl");
    question_title.classList.add("mb-4");
    question_title.append(value["Questions"]);
    question_container.append(question_title);
    //
    response_1_element = document.createElement("li");
    response_1_element.append(value["reponse 1"] + value["bareme_reponse_1"]);
    //
    response_2_element = document.createElement("li");
    response_2_element.append(value["reponse 2"] + value["bareme_reponse_2"]);
    //
    response_3_element = document.createElement("li");
    response_3_element.append(value["reponse 3"] + value["bareme_reponse_3"]);
    //
    responses_container = document.createElement("ul");
    responses_container.id = "responses-" + index;
    responses_container.append(response_1_element);
    responses_container.append(response_2_element);
    responses_container.append(response_3_element);
    //
    question_container.append(responses_container);
    //
    questions_container.append(question_container);
    separator = document.createElement("hr");
    questions_container.append(separator);
    //
  });
}

async function launch() {
  var persos = [];
  await get_caracteristics();
  await get_csv_persos();
  // fusionne les deux dictionnaires
  Object.entries(caracteristics_index_name).forEach(([index, value]) => {
    persos[index] = { ...persos_index_name[index], ...value };
  });
  //
  var persos_distance = ajout_distance(persos, { Courage: 3, Ambition: 4, Intelligence: 2, Good: 1 });
  var kppv = get_kppv(persos_distance, 20);
  var best_distance = meilleur_distance(kppv);
  //
  await get_questions();
  create_questions(questions);
  console.log(questions);
}

window.addEventListener("load", function (event) {
  launch();
});
