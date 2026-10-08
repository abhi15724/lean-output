# Changelog

## 2.0.0

### Added
- Complete command set for audit, compress, review, and usage reporting.
- Built-in token audit and local transcript usage utilities.
- Prompt-compression reference with semantic-preservation rules.
- Default configuration file and documented precedence.
- Regression tests for mode persistence, fast-build activation, off mode, and auditing.
- Professional README and clearer project layout.

### Improved
- Reworked mode hook to validate modes, read configuration, handle malformed config safely, and avoid output when disabled.
- Tightened core lean-output and fast-build guidance around correctness, security, accessibility, and verification.
- Clarified that token numbers are heuristic unless measured by a target tokenizer.

### Fixed
- Documentation previously referenced commands/scripts that were not included in the package.
- Help documentation previously described a `config.json` setting that the hook did not actually read.
