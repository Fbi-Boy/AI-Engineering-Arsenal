# Frontend Feature Quality Checklist

Use the checklist items that apply to the feature. Record exclusions when they materially affect risk.

## Product behavior
- [ ] User outcome and acceptance criteria are clear.
- [ ] Loading, success, empty, validation, and failure states are covered.
- [ ] Duplicate submissions and stale responses are considered.
- [ ] Navigation, browser history, and refresh behavior are correct.
- [ ] Permission denial and expired authentication are handled.

## Architecture and maintainability
- [ ] Existing framework, routes, component patterns, and styling conventions are followed.
- [ ] Shared components and tokens are reused.
- [ ] State has a clear owner and no unnecessary duplicate source of truth.
- [ ] Components have focused responsibilities.
- [ ] Dependencies are justified and maintained.
- [ ] Types and API contracts are aligned.

## Accessibility
- [ ] Semantic HTML elements are used for their intended purpose.
- [ ] Inputs have programmatic labels and instructions.
- [ ] Keyboard users can reach and operate all interactive controls.
- [ ] Focus is visible and managed for dialogs / dynamic navigation.
- [ ] Errors are associated with the relevant fields and announced appropriately.
- [ ] Contrast and status are not conveyed by color alone.
- [ ] Motion is not essential where reduced-motion preferences apply.
- [ ] Heading order and landmarks support navigation.

## Responsive and visual quality
- [ ] Layout works at target viewport sizes.
- [ ] Content reflows without unintended horizontal scrolling.
- [ ] Long labels, validation messages, and empty states fit.
- [ ] Touch targets and spacing are usable on supported devices.
- [ ] Zoom and text scaling do not hide content.
- [ ] Loading / disabled states do not cause layout instability.

## Security and privacy
- [ ] Client input is validated again by the server.
- [ ] UI visibility is not treated as authorization.
- [ ] No private token or secret enters the client bundle.
- [ ] Sensitive values are not logged or exposed in URLs.
- [ ] Output renders untrusted text safely; dangerous HTML is not inserted unsanitized.
- [ ] File uploads, redirects, and external links are constrained where relevant.

## Verification
- [ ] Tests assert observable behavior and meaningful failures.
- [ ] Edge and error paths are tested.
- [ ] Lint, type-check, and build results are recorded.
- [ ] Browser console / runtime errors are checked where available.
- [ ] Manual checks and unverified areas are explicitly listed.
