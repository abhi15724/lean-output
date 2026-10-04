'use strict';
// SessionStart: inject the full ruleset once at the active mode.
const { readMode, rules, emit } = require('./lib');
try {
  const mode = readMode();
  if (mode !== 'off') emit('SessionStart', rules(mode));
} catch (_) { /* never block a session */ }
