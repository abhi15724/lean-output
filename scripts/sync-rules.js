#!/usr/bin/env node
'use strict';
// Generates the instruction-only copies for other agents from rules/core.md.
// Usage: node scripts/sync-rules.js [--check]
const fs = require('fs');
const path = require('path');
const root = path.join(__dirname, '..');
const core = fs.readFileSync(path.join(root, 'rules', 'core.md'), 'utf8').trim();
const body = `# lean-output: the editor\n\n${core}\n`;
const files = {
  'AGENTS.md': body,
  '.github/copilot-instructions.md': body,
  '.clinerules/lean-output.md': body,
  '.cursor/rules/lean-output.mdc': `---\ndescription: lean-output, maximum value per token\nalwaysApply: true\n---\n\n${body}`,
  '.windsurf/rules/lean-output.md': `---\ntrigger: always_on\n---\n\n${body}`,
};
const check = process.argv.includes('--check');
let stale = 0;
for (const [rel, text] of Object.entries(files)) {
  const p = path.join(root, rel);
  if (check) {
    if (!fs.existsSync(p) || fs.readFileSync(p, 'utf8') !== text) { console.error('STALE: ' + rel); stale++; }
  } else {
    fs.mkdirSync(path.dirname(p), { recursive: true });
    fs.writeFileSync(p, text);
    console.log('wrote ' + rel);
  }
}
if (check) process.exit(stale ? 1 : 0);
