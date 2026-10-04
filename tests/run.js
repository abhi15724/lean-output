'use strict';
const { spawnSync } = require('child_process');
const fs = require('fs'), os = require('os'), path = require('path'), assert = require('assert');
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'lean-'));
const env = { ...process.env, LEAN_FLAG_FILE: path.join(tmp, 'flag'), LEAN_CONFIG: path.join(tmp, 'cfg.json') };
delete env.LEAN_DEFAULT_MODE;
const hook = (f, input) => {
  const r = spawnSync('node', [path.join(__dirname, '..', 'hooks', f)], { input: input || '', env, encoding: 'utf8' });
  assert.strictEqual(r.status, 0, r.stderr);
  return r.stdout ? JSON.parse(r.stdout).hookSpecificOutput : null;
};
const prompt = (p) => hook('lean-prompt.js', JSON.stringify({ prompt: p }));

let o = hook('lean-activate.js');
assert.strictEqual(o.hookEventName, 'SessionStart');
assert(o.additionalContext.includes('[standard]') && o.additionalContext.includes('first rung'));

o = prompt('how do I sort a list?');
assert(o.additionalContext.startsWith('[lean-output:standard]'));

o = prompt('/lean ultra');
assert(o.additionalContext.includes('now ultra'));
assert(hook('lean-activate.js').additionalContext.includes('[ultra]'));

o = prompt('/lean-output:lean off');
assert(o.additionalContext.includes('now off'));
assert.strictEqual(hook('lean-activate.js'), null);
assert.strictEqual(prompt('anything'), null);

o = prompt('/lean');                       // off -> back on at default
assert(o.additionalContext.includes('now standard'));
o = prompt('lean lite');
assert(o.additionalContext.includes('now lite'));

fs.writeFileSync(env.LEAN_FLAG_FILE, 'garbage');   // bad flag falls back to default
assert(prompt('hi').additionalContext.startsWith('[lean-output:standard]'));
fs.unlinkSync(env.LEAN_FLAG_FILE);
fs.writeFileSync(env.LEAN_CONFIG, '{"defaultMode":"ultra"}');
assert(prompt('hi').additionalContext.startsWith('[lean-output:ultra]'));

assert.doesNotThrow(() => hook('lean-prompt.js', 'not json'));  // never blocks
console.log('all hook tests passed');
