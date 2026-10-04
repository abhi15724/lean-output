'use strict';
// UserPromptSubmit: handle mode switches, then inject a one-line reminder (cheap per turn).
const { readMode, writeMode, defaultMode, reminder, parseSwitch, emit } = require('./lib');
let raw = '';
process.stdin.on('data', (c) => (raw += c));
process.stdin.on('end', () => {
  try {
    const data = raw ? JSON.parse(raw) : {};
    const sw = parseSwitch(data.prompt);
    let mode = readMode();
    let note = '';
    if (sw) {
      if (sw.mode) mode = sw.mode;
      else if (mode === 'off') mode = defaultMode() === 'off' ? 'standard' : defaultMode();
      writeMode(mode);
      note = `lean-output mode is now ${mode}. Confirm in one short line.\n`;
    }
    if (mode === 'off') {
      if (note) emit('UserPromptSubmit', note.trim());
      return;
    }
    emit('UserPromptSubmit', note + reminder(mode));
  } catch (_) { /* never block a prompt */ }
});
