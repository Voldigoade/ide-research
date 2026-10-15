import { chromium } from "playwright";
import assert from "node:assert/strict";
import { createServer } from "node:http";
import { readdir, readFile, stat } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const site = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../site");
const configuredBase = process.env.IDE_SITE_URL;
const localMode = !configuredBase;
const baseUrl = configuredBase ? `${configuredBase.replace(/\/+$/, "")}/` : "http://127.0.0.1:4173/ide-research/";
const origin = new URL(baseUrl).origin;
const basePath = new URL(baseUrl).pathname.replace(/\/+$/, "");
const mime = {".html":"text/html; charset=utf-8",".css":"text/css; charset=utf-8",".js":"text/javascript; charset=utf-8",".json":"application/json; charset=utf-8",".svg":"image/svg+xml",".xml":"application/xml; charset=utf-8",".txt":"text/plain; charset=utf-8",".png":"image/png"};
const server = createServer(async (req, res) => {
  try {
    let pathname = decodeURIComponent(new URL(req.url, origin).pathname);
    if (pathname === basePath || pathname === `${basePath}/`) pathname = "/";
    else if (pathname.startsWith(`${basePath}/`)) pathname = pathname.slice(basePath.length);
    if (pathname.includes("..")) throw new Error("invalid path");
    let file = path.resolve(site, `.${pathname}`);
    if (!file.startsWith(`${site}${path.sep}`) && file !== site) throw new Error("invalid path");
    if ((await stat(file)).isDirectory()) file = path.join(file, "index.html");
    res.writeHead(200, {"content-type":mime[path.extname(file)] || "application/octet-stream", "cache-control":"no-store"});
    res.end(await readFile(file));
  } catch {
    res.writeHead(404, {"content-type":"text/plain; charset=utf-8"});
    res.end("Not found");
  }
});

async function htmlRoutes(directory, prefix = "") {
  const routes = [];
  for (const entry of await readdir(directory, {withFileTypes:true})) {
    const name = path.join(directory, entry.name);
    const relative = prefix ? `${prefix}/${entry.name}` : entry.name;
    if (entry.isDirectory()) routes.push(...await htmlRoutes(name, relative));
    else if (entry.isFile() && entry.name.endsWith(".html") && relative !== "404.html") {
      routes.push(relative === "index.html" ? "/" : relative.endsWith("/index.html") ? `/${relative.slice(0,-10)}` : `/${relative}`);
    }
  }
  return routes;
}

if (localMode) await new Promise(resolve => server.listen(4173, "127.0.0.1", resolve));
const browser = await chromium.launch({headless:true});
const pageErrors = [];
const consoleErrors = [];
const badResponses = [];
const externalRequests = new Set();
try {
  const page = await browser.newPage({viewport:{width:1280,height:900}});
  page.on("pageerror", error => pageErrors.push(error.message));
  page.on("console", message => { if (message.type() === "error") consoleErrors.push(message.text()); });
  page.on("request", request => { if (new URL(request.url()).origin !== origin) externalRequests.add(request.url()); });
  page.on("response", response => { if (response.status() >= 400) badResponses.push(`${response.status()} ${response.url()}`); });

  const routes = (await htmlRoutes(site)).sort();
  assert.ok(routes.length >= 25, `expected all translated pages, found ${routes.length}`);
  const titles = new Set();
  for (const route of routes) {
    const response = await page.goto(new URL(route.replace(/^\/+/, ""), baseUrl).href, {waitUntil:"networkidle"});
    assert.equal(response.status(), 200, `${route} should return HTTP 200`);
    const info = await page.evaluate(() => {
      const get = selector => document.querySelector(selector)?.content || "";
      return {
        lang: document.documentElement.lang,
        title: document.title.trim(),
        description: get('meta[name="description"]'),
        canonical: document.querySelector('link[rel="canonical"]')?.href || "",
        ogTitle: get('meta[property="og:title"]'),
        ogDescription: get('meta[property="og:description"]'),
        alternates: [...document.querySelectorAll('link[rel="alternate"][hreflang]')].map(link => ({lang:link.hreflang,href:link.href})),
        width: document.documentElement.scrollWidth,
        viewport: document.documentElement.clientWidth,
        textLength: document.body.innerText.trim().length
      };
    });
    assert.ok(["fr","en","es"].includes(info.lang), `${route} must declare its language`);
    assert.ok(info.title.length > 4, `${route} must have a useful title`);
    assert.ok(!titles.has(info.title), `duplicate page title: ${info.title}`);
    titles.add(info.title);
    assert.ok(info.description.length > 20, `${route} must have a useful description`);
    assert.ok(info.ogTitle.length > 4 && info.ogDescription.length > 20, `${route} must have page-specific social metadata`);
    assert.ok(info.textLength > 100, `${route} must render page content`);
    const canonical = new URL(info.canonical);
    assert.equal(canonical.pathname, `${basePath}${route}`.replace(/\/+/g, "/"), `${route} must have a self canonical`);
    const langs = new Set(info.alternates.map(item => item.lang));
    for (const locale of ["fr","en","es","x-default"]) assert.ok(langs.has(locale), `${route} missing hreflang ${locale}`);
    const neutral = route.replace(/^\/(en|es)\//, "/");
    const expected = {fr:neutral,en:`/en${neutral === "/" ? "/" : neutral}`,es:`/es${neutral === "/" ? "/" : neutral}`,"x-default":neutral};
    for (const item of info.alternates) assert.equal(new URL(item.href, canonical).pathname, `${basePath}${expected[item.lang]}`.replace(/\/+/g, "/"), `${route} hreflang ${item.lang} mismatch`);

    await page.setViewportSize({width:390,height:844});
    const mobileWidth = await page.evaluate(() => ({scroll:document.documentElement.scrollWidth, viewport:document.documentElement.clientWidth}));
    if (mobileWidth.scroll > mobileWidth.viewport + 1) {
      const offenders = await page.evaluate(() => [...document.querySelectorAll("body *")].map(el => { const r=el.getBoundingClientRect(); return {tag:el.tagName,cls:typeof el.className === "string" ? el.className : "",id:el.id,text:(el.innerText||"").slice(0,90),left:Math.round(r.left),right:Math.round(r.right),width:Math.round(r.width),scroll:el.scrollWidth,client:el.clientWidth}; }).filter(x => x.right > innerWidth + 1 || x.left < -1 || x.scroll > x.client + 4).sort((a,b)=>(b.right-innerWidth)-(a.right-innerWidth)).slice(0,16));
      console.error("Mobile overflow elements", JSON.stringify(offenders));
    }
    assert.ok(mobileWidth.scroll <= mobileWidth.viewport + 1, `${route} overflows at mobile width: ${mobileWidth.scroll}/${mobileWidth.viewport}`);
    await page.setViewportSize({width:1280,height:900});
    const desktopWidth = await page.evaluate(() => ({scroll:document.documentElement.scrollWidth, viewport:document.documentElement.clientWidth}));
    assert.ok(desktopWidth.scroll <= desktopWidth.viewport + 1, `${route} overflows at desktop width: ${desktopWidth.scroll}/${desktopWidth.viewport}`);
  }

  await page.goto(baseUrl, {waitUntil:"networkidle"});
  const languageButton = page.locator('button[aria-label*="langue"],button[aria-label*="language"],button[aria-label*="idioma"]').first();
  await languageButton.click();
  await page.locator('a.md-select__link[href*="/en/"]').first().click();
  await page.waitForFunction(() => document.documentElement.lang === "en");
  await languageButton.click();
  await page.locator('a.md-select__link[href*="/es/"]').first().click();
  await page.waitForFunction(() => document.documentElement.lang === "es");
  await languageButton.click();
  await page.locator(`a.md-select__link[href="${basePath}/"]`).first().click();
  await page.waitForFunction(() => document.documentElement.lang === "fr");

  const scenarioSelect = page.locator("#scenario-select");
  await page.locator("#scenario-results table tbody tr").first().waitFor();
  const initialRank = await page.locator("#scenario-results tbody tr").first().innerText();
  await scenarioSelect.selectOption("rust");
  await page.waitForFunction(() => document.querySelector("#scenario-select")?.value === "rust");
  const rustRank = await page.locator("#scenario-results tbody tr").first().innerText();
  assert.notEqual(initialRank, rustRank, "Rust scenario must recalculate the ranking");

  await page.goto(new URL("compare/", baseUrl).href, {waitUntil:"networkidle"});
  await page.locator("#compare-results table tbody tr").first().waitFor();
  assert.equal(await page.locator("#compare-controls input:checked").count(), 3);
  const extra = page.locator('#compare-controls input[value="vscodium"]');
  await extra.check();
  assert.equal(await page.locator("#compare-controls input:checked").count(), 4);
  assert.equal(await page.locator("#compare-results thead th").count(), 5);
  await extra.uncheck();

  assert.deepEqual(pageErrors, [], "browser page errors must be absent");
  assert.deepEqual(consoleErrors, [], "browser console errors must be absent");
  assert.deepEqual(badResponses, [], "site resources must not return HTTP errors");
  assert.deepEqual([...externalRequests], [], "site pages must not make third-party requests");
  console.log(`Browser audit passed (${localMode ? "local" : "live"}): ${routes.length} pages, French/English/Spanish navigation, chooser, scenario, comparator, desktop/mobile width, SEO metadata, no console errors or third-party requests.`);
} finally {
  await browser.close();
  if (localMode) await new Promise(resolve => server.close(resolve));
}
