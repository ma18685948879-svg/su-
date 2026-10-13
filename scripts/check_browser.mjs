#!/usr/bin/env node
// Verify the actual local browser, separately from package presence.
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const name = process.argv[2] || 'folio';
if (!['folio', 'guizang-ppt-skill'].includes(name)) {
  console.error('Usage: node scripts/check_browser.mjs [folio|guizang-ppt-skill]');
  process.exit(2);
}
let browser;
try {
  const require = createRequire(path.join(root, '.agents', 'skills', name, 'package.json'));
  const module = await import(pathToFileURL(require.resolve('playwright')).href);
  const { chromium } = module.default || module;
  browser = await chromium.launch({ headless: true, timeout: 15000 });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.setContent('<!doctype html><html><body><p id="probe">Browser readiness check</p></body></html>');
  const box = await page.locator('#probe').boundingBox();
  if (!box || box.width <= 0 || box.height <= 0) throw new Error('Rendered text has no visible geometry');
  console.log(JSON.stringify({ skill: name, browser: 'ready', version: browser.version(), geometry: 'passed', export: 'not tested' }));
} catch (error) {
  console.error(`${name}: browser unavailable. ${error.message.split('\n')[0]}`);
  console.error(`Restore using python scripts/setup_skills.py --skill ${name}. Browser download access and Linux system libraries are required.`);
  process.exitCode = 1;
} finally {
  if (browser) await browser.close();
}
