import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1122,'height':1000}, device_scale_factor=2)
        await pg.goto('file://'+sys.argv[1]); await pg.wait_for_timeout(500)
        el = await pg.query_selector('.pagina')
        await el.screenshot(path=sys.argv[2])
        await b.close()
asyncio.run(main())
