#!/usr/bin/env python3
"""Coal Haul check: runs the game's own self-check (the same as /check in the game's chat)
in a test browser, on a new game, and prints what passed and what failed.

  python3 tools/check.py              # check index.html next to this folder
  python3 tools/check.py --shots DIR  # also save a picture of the map after the check
  python3 tools/check.py --keep-save  # also keep this version's save in tools/saves/ (do it once per version pushed)

It also loads every save file in tools/saves/ (old versions of the game) and checks that
each one loads without errors, so a change that breaks old saves is caught.
Exit code 0: everything passed. 1: something failed. 2: the check could not run.

Needs: pip install playwright, and Chrome or Chromium (set CHROME=/path/to/chrome if it
is not found by itself).
"""
import asyncio, glob, json, os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME = 'file://' + os.path.join(ROOT, 'index.html')


def chrome_path():
    for p in [os.environ.get('CHROME'), shutil.which('google-chrome'), shutil.which('chromium'),
              shutil.which('chromium-browser')]:
        if p:
            return p
    return None


async def new_page(b, errs):
    pg = await b.new_page(viewport={'width': 1200, 'height': 900})
    pg.on('pageerror', lambda e: errs.append(str(e)))
    return pg


async def main():
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print('Playwright is missing: pip install playwright')
        return 2
    shots = sys.argv[sys.argv.index('--shots') + 1] if '--shots' in sys.argv else None
    ok = True
    async with async_playwright() as p:
        exe = chrome_path()
        b = await p.chromium.launch(**({'executable_path': exe} if exe else {}), args=['--no-sandbox'])
        # 1. the self-check on a new game
        errs = []
        pg = await new_page(b, errs)
        await pg.goto(GAME)
        await pg.wait_for_timeout(800)
        await pg.click('#mm-new')
        await pg.wait_for_timeout(300)
        await pg.click('button[data-c]')
        await pg.wait_for_timeout(1500)
        res = await pg.evaluate("async()=>{const R=await runChecks({restore:false});const L=chkLines(R);return {ver:R.ver,sum:L.sum,fails:L.fails,ok:L.ok,groups:R.groups}}")
        print('Coal Haul v%s check' % res['ver'])
        for g, v in res['groups'].items():
            n = v['pass'] + len(v['fail'])
            print('  %s %-10s %d/%d' % ('✓' if not v['fail'] else '✗', g, v['pass'], n))
        for f in res['fails']:
            print('  ✗ ' + f)
        for e in errs:
            print('  ✗ page error: ' + e)
        ok = res['ok'] and not errs
        if '--keep-save' in sys.argv:
            # a save of this version, every building built: later versions must still load it
            d = await pg.evaluate("()=>{const d=gameSave();d.name='check v'+VER;return JSON.stringify(d)}")
            os.makedirs(os.path.join(ROOT, 'tools', 'saves'), exist_ok=True)
            fn = os.path.join(ROOT, 'tools', 'saves', 'v%s.json' % res['ver'])
            open(fn, 'w', encoding='utf-8').write(d)
            print('  kept the save %s (%d KB)' % (os.path.relpath(fn, ROOT), len(d) // 1024))
        if shots:
            os.makedirs(shots, exist_ok=True)
            await pg.screenshot(path=os.path.join(shots, 'after-check.png'))
        await pg.close()
        # 2. every old save loads
        saves = sorted(glob.glob(os.path.join(ROOT, 'tools', 'saves', '*.json')))
        for f in saves:
            errs = []
            pg = await new_page(b, errs)
            await pg.goto(GAME)
            await pg.wait_for_timeout(600)
            raw = open(f, encoding='utf-8').read()
            await pg.evaluate("raw=>loadFrom(raw)", raw)
            await pg.wait_for_timeout(2500)
            st = await pg.evaluate("()=>({menu:MENU,n:Object.keys(veh).length})")
            good = not errs and not st['menu']
            print('  %s old save %s' % ('✓' if good else '✗', os.path.basename(f)) + ('' if good else ': ' + '; '.join(errs[:3] or ['did not start'])))
            ok = ok and good
            await pg.close()
        await b.close()
    print('Everything passed.' if ok else 'Something failed.')
    return 0 if ok else 1


if __name__ == '__main__':
    try:
        sys.exit(asyncio.run(main()))
    except Exception as e:
        print('The check could not run: %s' % e)
        sys.exit(2)
