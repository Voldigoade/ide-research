// Shared deterministic scoring helpers for the published chooser.
const ID = (id) => document.getElementById(id);
const DATA_ROOT = new URL("data/", document.currentScript.src);
const SITE_ROOT = new URL("../", document.currentScript.src);
const langs = {
 fr:{stack:"Pile",work:"Workflow",rank:"Rang indicatif",range:"Plage du modèle",mix:"Composition",uncertain:"Les plages se chevauchent: le rang n'est pas une certitude.",sources:"Sources et limites"},
 en:{stack:"Stack",work:"Workflow",rank:"Indicative rank",range:"Model range",mix:"Work mix",uncertain:"Ranges overlap: rank is not a certainty.",sources:"Sources and limits"},
 es:{stack:"Stack",work:"Flujo",rank:"Rango indicativo",range:"Rango del modelo",mix:"Composición",uncertain:"Los rangos se solapan: el puesto no es una certeza.",sources:"Fuentes y límites"}
};
const labels = {
 fr:{rust:"Rust",tauri:"Tauri",web:"TypeScript/React",python:"Python",other:"Autres",databases:"Bases",docker:"Docker",devcontainers:"Dev Containers",wsl:"WSL2",remote:"SSH/remote",git:"Git",terminal:"Terminal",debugging:"Débogage",refactoring:"Code et refactoring",plugins:"Extensions",agents:"Agents IA",security:"Sécurité",privacy:"Confidentialité",performance:"Performance",stability:"Stabilité",windows:"Windows",linux:"Linux",macos:"macOS",cost:"Coût"},
 en:{rust:"Rust",tauri:"Tauri",web:"TypeScript/React",python:"Python",other:"Other",databases:"Databases",docker:"Docker",devcontainers:"Dev Containers",wsl:"WSL2",remote:"SSH/remote",git:"Git",terminal:"Terminal",debugging:"Debugging",refactoring:"Code/refactoring",plugins:"Extensions",agents:"AI agents",security:"Security",privacy:"Privacy",performance:"Performance",stability:"Stability",windows:"Windows",linux:"Linux",macos:"macOS",cost:"Cost"},
 es:{rust:"Rust",tauri:"Tauri",web:"TypeScript/React",python:"Python",other:"Otros",databases:"Bases",docker:"Docker",devcontainers:"Dev Containers",wsl:"WSL2",remote:"SSH/remoto",git:"Git",terminal:"Terminal",debugging:"Depuración",refactoring:"Código/refactorización",plugins:"Extensiones",agents:"Agentes IA",security:"Seguridad",privacy:"Privacidad",performance:"Rendimiento",stability:"Estabilidad",windows:"Windows",linux:"Linux",macos:"macOS",cost:"Coste"}
};
function getLang(panel){ return (panel.dataset.lang || document.documentElement.lang || "en").slice(0,2); }
function parse(candidate, criteria) {
 return Object.fromEntries(candidate.scores.split(",").map((value,index) => [criteria[index].id, value.split("-").map(Number)]));
}
function boundsFor(values, scenario) {
 let stack=[0,0];
 for (const [key,share] of Object.entries(scenario.stack)) {
   const criterion = key === "other" ? ["rust","web","python"] : [key];
   for (let end=0;end<2;end++) stack[end] += criterion.reduce((sum,id)=>sum+values[id][end],0)/criterion.length*share/100;
 }
 const entries=Object.entries(scenario.dimensions), total=entries.reduce((sum,entry)=>sum+entry[1],0);
 let work=[0,0];
 for(const [key,weight] of entries) for(let end=0;end<2;end++) work[end]+=values[key][end]*weight/total;
 const stackWeight=(scenario.stack_weight||55)/100; return [stackWeight*stack[0]+(1-stackWeight)*work[0],stackWeight*stack[1]+(1-stackWeight)*work[1]];
}
function roundedBound(x){ return (Math.round(x*2)/2).toFixed(1); }
function displayRange(range){ return roundedBound(range[0])+" to "+roundedBound(range[1])+" / 10"; }
async function loadData(){
 const [c,e,s]=await Promise.all(["criteria.json","environments.json","scenarios.json"].map(x=>fetch(new URL(x,DATA_ROOT)).then(r=>{if(!r.ok)throw Error("Could not load "+x);return r.json()})));
 return {criteria:c,environments:e,scenarios:s};
}
function renderScenario(panel,data,scenarioId){
 const scenario=data.scenarios.find(x=>x.id===scenarioId), lang=getLang(panel), t=langs[lang]||langs.en, l=labels[lang]||labels.en;
 if(!scenario)return;
 const rows=data.environments.map(env=>({env,range:boundsFor(parse(env,data.criteria),scenario)})).sort((a,b)=>(b.range[0]+b.range[1])-(a.range[0]+a.range[1]));
 const mix=Object.entries(scenario.stack).map(([k,v])=>(l[k]||k)+" "+v+"%").join(" · ");
 const summary=ID("scenario-summary");
 if(summary) summary.textContent=t.mix+": "+mix+". "+t.uncertain;
 const target=ID("scenario-results");
 if(target) target.innerHTML="<div class=\"table-scroll\"><table><thead><tr><th>"+t.rank+"</th><th>Environment</th><th>"+t.range+"</th></tr></thead><tbody>"+rows.map((x,i)=>"<tr><td>"+(i+1)+"</td><th scope=\"row\">"+x.env.name+"</th><td>"+displayRange(x.range)+"</td></tr>").join("")+"</tbody></table></div><p>"+t.sources+": <a href=\"method.md\">"+(lang==="fr"?"méthode":lang==="es"?"método":"method")+"</a>, <a href=\"products.md\">"+(lang==="fr"?"profils":lang==="es"?"perfiles":"profiles")+"</a>.</p>";
}
function renderCompare(panel,data,scenarioId,selected){
 const scenario=data.scenarios.find(x=>x.id===scenarioId), lang=getLang(panel), t=langs[lang]||langs.en, l=labels[lang]||labels.en;
 if(!scenario)return;
 const criteria=data.criteria, products=data.environments.filter(x=>selected.includes(x.id));
 const controls=ID("compare-controls");
 if(controls && controls.childElementCount===0){
   controls.innerHTML=data.environments.map(env=>"<label class=\"check-option\"><input type=\"checkbox\" value=\""+env.id+"\" "+(selected.includes(env.id)?"checked":"")+"> "+env.name+"</label>").join("");
   controls.querySelectorAll("input").forEach(input=>input.addEventListener("change",()=>{
     const checked=[...controls.querySelectorAll("input:checked")].map(x=>x.value);
     if(checked.length<2){input.checked=true;return}
     if(checked.length>4){input.checked=false;return}
     renderCompare(panel,data,ID("compare-scenario").value,checked);
   }));
 }
 const summary=ID("compare-summary");
 if(summary) summary.textContent=products.length+" "+(lang==="fr"?"environnements sélectionnés":lang==="es"?"entornos seleccionados":"environments selected")+". "+t.uncertain;
 const target=ID("compare-results");
 const scoreRow=products.map(env=>"<td>"+displayRange(boundsFor(parse(env,criteria),scenario))+"</td>").join("");
 const body=criteria.map(c=>"<tr><th scope=\"row\">"+(l[c.id]||c.label)+"</th>"+products.map(env=>"<td>"+env.scores.split(",")[criteria.indexOf(c)]+"</td>").join("")+"</tr>").join("");
 if(target) target.innerHTML="<div class=\"table-scroll\"><table><thead><tr><th>Criterion</th>"+products.map(x=>"<th>"+x.name+"</th>").join("")+"</tr></thead><tbody><tr><th scope=\"row\">"+t.range+"</th>"+scoreRow+"</tr>"+body+"</tbody></table></div>";
}
async function init(){
 const panels=[...document.querySelectorAll(".tool-panel")];
 if(!panels.length)return;
 const data=await loadData();
 for(const panel of panels){
   const scenarioSelect=ID("scenario-select"), compareSelect=ID("compare-scenario");
   if(scenarioSelect){renderScenario(panel,data,scenarioSelect.value);scenarioSelect.addEventListener("change",()=>renderScenario(panel,data,scenarioSelect.value))}
   if(compareSelect){
     const initial=["vscode","idea","rustrover"];
     renderCompare(panel,data,compareSelect.value,initial);
     compareSelect.addEventListener("change",()=>renderCompare(panel,data,compareSelect.value,[...ID("compare-controls").querySelectorAll("input:checked")].map(x=>x.value)));
   }
 }
}
document.addEventListener("DOMContentLoaded",()=>init().catch(error=>{const live=document.querySelector('[aria-live="polite"]');if(live)live.textContent="Data unavailable: "+error.message;}));
