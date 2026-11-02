# Frontend Test Strategy

## Select the appropriate layer
- **Pure logic tests:** state reducers, formatters, validators, and utilities without rendering.
- **Component / DOM tests:** user interaction, accessible semantics, conditional rendering, and local state.
- **Browser integration tests:** routing, browser APIs, network interaction, storage, and multi-component behavior.
- **End-to-end tests:** a small number of critical journeys across the assembled application and real test backend.

Keep most permutations in fast, focused tests. Use browser tests for cross-boundary confidence rather than reproducing every branch at the slowest level.

## Scenario matrix
For each page or journey, consider:
- Initial render and navigation entry points.
- Loading and delayed responses.
- Success, empty, and partial data.
- Client-side and server-side validation errors.
- Authentication expiry and permission denial.
- Timeout, network interruption, retry, and duplicate submission.
- Browser refresh, direct URL entry, and back / forward behavior.
- Responsive layout and supported browser differences.
- Keyboard-only interaction and focus state.

## Network strategy
Use deterministic fixtures or a controlled test API. Make each fixture describe the relevant request and response contract. Test the UI response to status classes and payload shapes that the frontend promises to handle.

Mocks do not prove backend correctness. Keep contract tests or backend integration tests responsible for the server behavior. Never point routine test automation at a production endpoint.

## Locators and assertions
Prefer role + accessible name, label, placeholder only when semantically appropriate, and visible text. Prefer state-aware assertions that wait for the UI to reach the expected state. Avoid CSS selectors or DOM paths unless the underlying element has no useful semantic contract.

## Visual verification
Use visual snapshots only when the team maintains stable baselines, representative viewports, font / rendering configuration, and a review process for intentional changes. A screenshot diff is evidence of pixels, not proof of usability or accessibility.

## Flakiness triage
Compare isolated and parallel runs. Inspect animations, timers, network waits, shared state, browser context reuse, unstable selectors, and backend test data. Prefer waiting for a known user-visible condition instead of increasing timeouts indiscriminately.
