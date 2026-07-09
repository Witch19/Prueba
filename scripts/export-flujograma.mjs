import puppeteer from 'puppeteer';
import { fileURLToPath } from 'url';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '..');
const htmlPath = path.join(root, 'docs', 'flujograma-para-enviar.html');
const pngPath = path.join(root, 'docs', 'flujograma-presupuesto.png');
const pdfPath = path.join(root, 'docs', 'flujograma-presupuesto.pdf');

const browser = await puppeteer.launch({
  headless: true,
  args: ['--no-sandbox', '--disable-setuid-sandbox']
});

const page = await browser.newPage();
await page.setViewport({ width: 1400, height: 900, deviceScaleFactor: 2 });
await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0', timeout: 60000 });
await page.waitForFunction(() => document.body.dataset.ready === 'true', { timeout: 60000 });
await new Promise((r) => setTimeout(r, 1000));

const height = await page.evaluate(() => document.body.scrollHeight);
await page.setViewport({ width: 1400, height, deviceScaleFactor: 2 });

await page.screenshot({ path: pngPath, fullPage: true, type: 'png' });
await page.pdf({
  path: pdfPath,
  width: '1400px',
  height: `${height}px`,
  printBackground: true,
  margin: { top: '10mm', right: '10mm', bottom: '10mm', left: '10mm' }
});

await browser.close();
console.log('PNG:', pngPath);
console.log('PDF:', pdfPath);
