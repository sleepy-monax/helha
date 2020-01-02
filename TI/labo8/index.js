let list_areas = {};
var language = "fr";
var accidents = {}

var list_box_text = {}
var list_box_data = {}
var texts = {}
var rows = []
var clusterize;

function populate_list_box_from_rest(id, url) {
    let listbox = document.getElementById(id);
    listbox.innerHTML = "";

    let el = document.createElement("option");

    el.textContent = "-";
    el.value = -1;

    listbox.appendChild(el);
    texts[id] = {};

    fetch(url).then(res => res.json()).then((data) => {
        list_box_data[id] = data;

        for (const key in data) {
            let el = document.createElement("option");

            el.textContent = data[key][language];
            el.value = key;

            texts[id][Math.trunc(key)] = data[key];

            listbox.appendChild(el);
        }
    });
}

function populate_list_box_from_cache(id, url) {
    let listbox = document.getElementById(id);
    listbox.innerHTML = "";

    let el = document.createElement("option");

    el.textContent = "-";
    el.value = -1;

    listbox.appendChild(el);
    texts[id] = {};

    for (const key in list_box_data[id]) {
        let el = document.createElement("option");

        el.textContent = list_box_data[id][key][language];
        el.value = key;

        texts[id][Math.trunc(key)] = list_box_data[id][key];

        listbox.appendChild(el);
    }
}

var properties = ["dayofweek", "area", "colltype", "lightcond", "roadtype", "province", "region", "commune"]

function display_list() {
    document.getElementById("status").innerText = "Generating list...";

    language = document.getElementById("list-language").value;

    rows = [];

    if (language == 'fr') {
        rows = [`<tr>
<th>Date</th>
<th>Heure</th>
<th>Jour de la semaine</th>
<th></th>
<th>Type</th>
<th>Moment de la journée</th>
<th>Route</th>
<th>Province</th>
<th>Region</th>
<th>Commune</th>
</tr>`]
    } else {
        rows = [`<tr>
<th>Datum</th>
<th>Tijd</th>
<th>Dagvan de week </th>
<th></th>
<th>Type</th>
<th>Tijdstipvan de dag</th>
<th>Route</th>
<th>Provincie</th>
<th>Regio</th>
<th>Stad</th>
</tr>`]
    }

    let filters = {};
    let date = document.getElementById("input-date").value == "" ? "" : new Date(document.getElementById("input-date").value).toLocaleDateString();

    for (prop in properties) {
        prop = properties[prop]

        let sel = document.getElementById("list-" + prop);
        filters[prop] = sel.value;
    }

    for (const acc in accidents) {
        let should_be_showed = true;

        for (prop in properties) {
            prop = properties[prop]

            let sel = document.getElementById("list-" + prop);
            filters[prop] = sel.value;


            if (date != "" && new Date(((accidents[acc]["day"] * 24 * 60 * 60) - 2208988800) * 1000).toLocaleDateString() != date) {
                should_be_showed = false;
                break;
            }

            if (filters[prop] != -1 && accidents[acc][prop] != filters[prop]) {
                should_be_showed = false;
                break;
            }
        }

        if (should_be_showed) {
            var tr = document.createElement('tr');

            let td = document.createElement('td')
            let date = new Date(((accidents[acc]["day"] * 24 * 60 * 60) - 2208988800) * 1000)

            td.innerText = date.toLocaleDateString();
            tr.appendChild(td);

            td = document.createElement('td')
            td.innerText = accidents[acc]["hour"] + "h";
            tr.appendChild(td);

            for (prop in properties) {
                prop = properties[prop]

                td = document.createElement('td');

                td.innerText = texts["list-" + prop][accidents[acc][prop]][language];

                tr.appendChild(td);
            }

            rows.push(tr.outerHTML)
        }

    }

    if (clusterize) {
        clusterize.update(rows);

    } else {
        clusterize = new Clusterize({
            rows: rows,
            scrollId: 'table-scroll',
            contentId: 'table-content',
        });

    }


    document.getElementById("status").innerText = "Done!";
}

console.log(document.getElementById("input-date").value);

function reload_view() {
    language = document.getElementById("list-language").value;
    populate_list_box_from_cache("list-area", "/api/query/list-areas.php");
    populate_list_box_from_cache("list-colltype", "/api/query/list-colltype.php");
    populate_list_box_from_cache("list-commune", "/api/query/list-communes.php");
    populate_list_box_from_cache("list-dayofweek", "/api/query/list-dayofweek.php");
    populate_list_box_from_cache("list-lightcond", "/api/query/list-lightcond.php");
    populate_list_box_from_cache("list-province", "/api/query/list-provinces.php");
    populate_list_box_from_cache("list-region", "/api/query/list-regions.php");
    populate_list_box_from_cache("list-roadtype", "/api/query/list-roadtypes.php");
    display_list();
}

language = document.getElementById("list-language").value;

populate_list_box_from_rest("list-area", "/api/query/list-areas.php");
populate_list_box_from_rest("list-colltype", "/api/query/list-colltype.php");
populate_list_box_from_rest("list-commune", "/api/query/list-communes.php");
populate_list_box_from_rest("list-dayofweek", "/api/query/list-dayofweek.php");
populate_list_box_from_rest("list-lightcond", "/api/query/list-lightcond.php");
populate_list_box_from_rest("list-province", "/api/query/list-provinces.php");
populate_list_box_from_rest("list-region", "/api/query/list-regions.php");
populate_list_box_from_rest("list-roadtype", "/api/query/list-roadtypes.php");

fetch("/api/query/all.php").then(res => res.json()).then((data) => { accidents = data; }).then(_ => display_list());
