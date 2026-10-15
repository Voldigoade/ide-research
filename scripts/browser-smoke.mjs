import { chromium } from "playwright";
import assert from "node:assert/strict";
import { createServer } from "node:http";
import { readFile, stat } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const site = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../site");
const mime = {".html":"text/html; charset=utf-8",".css":"text/css; charset=utf-8",".js":"text/javascript; charset=utf-8",".json":"application/json; charset=utf-8",".svg":"image/svg+xml"};
const server=createServer(async(req,res)=>{
  try {
    let pathname=decodeURIComponent(new URL(req.url,"http://localhost").pathname);
    if(pathname.includes("..")) throw new Error("invalid path");
    let file=path.join(site,pathname);
    if((await stat(file)).isDirectory()) file=path.join(file,"index.html");
    res.writeHead(200,{"content-type":mime[path.extname(file)]||"application/octet-stream"});
    res.end(await readFile(file));
  } catch {res.writeHead(404);res.end("Not found");}
});
await new Promise(resolve=>server.listen(4173,"127.0.0.1",resolve));
const browser=await chromium.launch({headless:true});
try {
 const page=await browser.newPage();
 const errors=[]; const external=[];
 page.on("pageerror",e=>errors.push(e.message));
 page.on("request",r=>{if(!r.url().startsWith("http://127.0.0.1:4173/"))external.push(r.url());});
 await page.goto("http://127.0.0.1:4173/",{waitUntil:"networkidle"});
 await page.getByRole("heading",{name:/IDE Research/i}).waitFor();
 await page.locator("#scenario-results table tbody tr").first().waitFor();
 const initial=await page.locator("#scenario-results tbody tr").first().innerText();
 await page.locator("#scenario-select").selectOption("rust");
 await page.waitForFunction(()=>document.querySelector("#scenario-summary").textContent.includes("55%")||document.querySelector("#scenario-summary").textContent.includes("75%"));
 const rust=await page.locator("#scenario-results tbody tr").first().innerText();
 assert.notEqual(initial,rust,"Rust scenario should recalculate the ranking");
 await page.goto("http://127.0.0.1:4173/compare/",{waitUntil:"networkidle"});
 await page.locator("#compare-results table tbody tr").first().waitFor();
 assert.equal(await page.locator("#compare-controls input:checked").count(),3);
 assert.deepEqual(errors,[]);
 assert.deepEqual(external,[],"the site must not make external requests");
} finally {
 await browser.close();
 await new Promise(resolve=>server.close(resolve));
}
console.log("Browser smoke passed: chooser, Rust-specific scenario, comparator, and no external requests.");
