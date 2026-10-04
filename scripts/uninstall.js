#!/usr/bin/env node
'use strict';
// Removes state lean-output writes outside the plugin folder. Run BEFORE removing the plugin.
const fs = require('fs');
const { FLAG, configPath } = require('../hooks/lib');
for (const p of [FLAG, configPath()]) {
  try { fs.unlinkSync(p); console.log('removed ' + p); } catch (_) { console.log('not present: ' + p); }
}
