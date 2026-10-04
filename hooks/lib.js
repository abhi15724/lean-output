'use strict';
const fs = require('fs');
const os = require('os');
const path = require('path');

const MODES = ['lite', 'standard', 'ultra', 'off'];
const MODE_LINE = {
  lite: 'Mode lite: trim filler only; normal prose and structure.',
  standard: 'Mode standard: answer first, no preamble/recap/closing; tight structure.',
  ultra: 'Mode ultra: terse, fragments allowed, assume defaults instead of asking, one-line rationale; code and results first.',
};

const claudeDir = process.env.CLAUDE_CONFIG_DIR || path.join(os.homedir(), '.claude');
const FLAG = process.env.LEAN_FLAG_FILE || path.join(claudeDir, '.lean-output-mode');

function configPath() {
  if (process.env.LEAN_CONFIG) return process.env.LEAN_CONFIG;
  if (process.platform === 'win32') {
    return path.join(process.env.APPDATA || path.join(os.homedir(), 'AppData', 'Roaming'), 'lean-output', 'config.json');
  }
  return path.join(process.env.XDG_CONFIG_HOME || path.join(os.homedir(), '.config'), 'lean-output', 'config.json');
}

const valid = (m) => (typeof m === 'string' && MODES.includes(m.toLowerCase()) ? m.toLowerCase() : null);

function defaultMode() {
  const env = valid(process.env.LEAN_DEFAULT_MODE);
  if (env) return env;
  try {
    const cfg = JSON.parse(fs.readFileSync(configPath(), 'utf8'));
    const m = valid(cfg.defaultMode);
    if (m) return m;
  } catch (_) { /* no config */ }
  return 'standard';
}

function readMode() {
  try {
    const m = valid(fs.readFileSync(FLAG, 'utf8').trim());
    if (m) return m;
  } catch (_) { /* no flag */ }
  return defaultMode();
}

function writeMode(m) {
  fs.mkdirSync(path.dirname(FLAG), { recursive: true });
  fs.writeFileSync(FLAG, m);
}

function rules(mode) {
  const core = fs.readFileSync(path.join(__dirname, '..', 'rules', 'core.md'), 'utf8').trim();
  return `LEAN-OUTPUT ACTIVE [${mode}]\n${core}\n${MODE_LINE[mode]}`;
}

function reminder(mode) {
  return `[lean-output:${mode}] answer first; no preamble/recap/closing; full detail if asked; never cut correctness or safety.`;
}

// "/lean ultra", "/lean-output:lean off", "/lean", or plain "lean ultra"
function parseSwitch(prompt) {
  const p = String(prompt || '').trim();
  let m = p.match(/^\/(?:lean-output:)?lean(?:\s+(lite|standard|ultra|off))?$/i);
  if (m) return { mode: m[1] ? m[1].toLowerCase() : null };
  m = p.match(/^lean\s+(lite|standard|ultra|off)$/i);
  if (m) return { mode: m[1].toLowerCase() };
  return null;
}

function emit(event, text) {
  process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: event, additionalContext: text } }));
}

module.exports = { MODES, FLAG, configPath, defaultMode, readMode, writeMode, rules, reminder, parseSwitch, emit };
