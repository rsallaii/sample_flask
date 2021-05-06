// get players data and create unique season dropdown
const url = "/static/data/players.json";
d3.json(url).then(function(data) {

  console.log(data);

  let list = data.map(d => d["Season"])
    .filter((value, index, self) => self.indexOf(value) === index)

  d3.select("#inputSeason").html("");

  var selection = d3.select("#inputSeason").selectAll("option").data(list);

  selection.enter()
    .append("option")
    .attr("value", d=>d)
    .text(d=>d)
    .merge(selection);

  selection.exit().remove();

});

// create event listeners for Season and Team
d3.select("#inputSeason").on("change", getSeason);
d3.select("#inputTeam").on("change", getTeam);

// create event handler functions
function getSeason() {
    let season = this.options[this.selectedIndex].value;
    create_team(season);
};

function getTeam() {
  let season = document.getElementById("inputSeason")
  season = season.options[season.selectedIndex].value

  let team = this.options[this.selectedIndex].value;
  create_player(season, team);
};

// create dropdown team
function create_team(season) {
  d3.json(url).then(function(data) {

    let col1 = "Season";
    let col2 = "Team";

    let list = data.filter( d => d[col1] === season);


    list = list.map(d => d[col2])
    .filter((value, index, self) => self.indexOf(value) === index)

    create_player(season, list[0]);
    
    d3.select("#input"+col2).html("");

    var selection = d3.select("#input"+col2).selectAll("option")
          .data(list);

    selection.enter()
      .append("option")
      .attr("value", d=>d)
      .text(d=>d)
      .merge(selection);

    selection.exit().remove();

  });
};

// create dropdown player
function create_player(season, team) {
  d3.json(url).then(function(data) {

    let col1 = "Season";
    let col2 = "Team";
    let col3 = "Player";

    console.log(data)
    console.log(season, team)
    let list = data.filter(d => d[col1] === season && d[col2] === team);
    console.log(list)

    list = list.map(d => d[col3])
      .filter((value, index, self) => self.indexOf(value) === index)

    console.log(list)
    
    d3.select("#input"+col3).html("");

    var selection = d3.select("#input"+col3).selectAll("option")
          .data(list);

    selection.enter()
      .append("option")
      .attr("value", d=>d)
      .text(d=>d)
      .merge(selection);

    selection.exit().remove();
  });
};

// init dropdowns team and player
create_team("2001");
create_player("2001", "A");