# Accessibility and Browser Coverage

## Accessibility checks
Verify the semantics users and assistive technologies rely on:
- Correct element roles and accessible names.
- Labels associated with inputs and instructions associated with controls.
- Required / invalid state communicated programmatically.
- Keyboard access to interactive elements and a visible focus indicator.
- Logical focus order and focus restoration after dialogs or navigation.
- Error messages connected to the relevant controls.
- Status messages and updates communicated without relying only on color.
- Alternative text or equivalent descriptions for meaningful visual content.

Automated accessibility checks are useful but incomplete. Combine them with keyboard review and manual assessment for complex interactions.

## Responsive coverage
Choose viewports from actual product breakpoints and supported devices. Check:
- Content reflow without unintended horizontal scrolling.
- Usable controls and touch targets.
- Navigation and dialog behavior at narrow widths.
- Text zoom / scaling where required.
- Tables, media, and long labels under constrained width.
- No content clipped by fixed heights or overlays.

Do not infer all device coverage from one desktop viewport.

## Browser matrix
Document browser engine, version policy, viewport, device scale, locale, timezone, and relevant feature support. Prioritize browsers from product analytics or an explicit support policy. Mark unsupported or unavailable browsers as not tested, not passed.

## Evidence hygiene
Screenshots, videos, traces, and HAR files may contain names, email addresses, private routes, cookies, or tokens. Use synthetic accounts, sanitize outputs, and review artifacts before attaching them to an issue or pull request.
