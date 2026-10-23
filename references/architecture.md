# Architecture Design and Layering Choices

Use this reference for new application frameworks or business modules, boundary refactoring, and layering reviews. Preserve the chosen structure for local changes; reconsider only affected responsibilities, collaboration, or dependency directions that actually change. Incorporate conclusions into the current Superpowers design/plan instead of creating another workflow or document set.

## Derive Responsibilities from Business Needs and Constraints

Trace one main operation through inputs, rules, state changes, data/external side effects, results, and failures. Extract the factors that actually affect module boundaries:

| Design input | Determine |
|---|---|
| Business workflow and invariants | Preconditions for operations, rules that must always hold, and the state required after failures |
| Data and transaction ownership | Owners of rules and state, write responsibility, atomic changes, and external actions that cannot be rolled back |
| Callers and real variation | How pages, background jobs, and other callers reuse an operation; dependencies with existing alternative implementations and their differences |
| Constraints affecting the design | Actual latency, concurrency, consistency, permission, testability, or deployment needs, and existing project conventions |

Discuss only supported constraints that affect the current choice; do not invent numerical targets. State assumptions for information that does not block the choice, and ask only when essential business intent is unclear. A few sentences can suffice for a small project.

## Modules and Public Interfaces

Organize modules by business capability before deciding their internal technical layers. Business organization and technical layering can coexist; a module may begin with a few functions.

For important affected modules, describe the following in a short paragraph or table row rather than imposing a template on every file:

| Area | Design considerations |
|---|---|
| Responsibility and ownership | Business capability, owned rules/state, and division of work with neighboring modules |
| Public interface | Operations, business inputs/outputs, preconditions, invariants, errors, and required call order; include only configuration/performance constraints callers need |
| Internal implementation | Hide data mappings, algorithm steps, supplier protocols, and other internals so callers need not assemble internal workflows |
| Side effects and transactions | Database writes or external calls, transaction start/commit ownership, and failure, timeout, and duplicate-call behavior |
| Dependencies and variation | Permitted public capabilities, and the module that should primarily change for a typical business-rule or external-implementation change |

In-process modules collaborate through public operations; callers neither mutate another module's internal state nor bypass its rules. When cross-module changes must be atomic in one database, an explicit use case coordinates a shared transaction; directory layering does not justify remote calls. Respect communication contracts between existing independent applications rather than bypassing them through imports of another application's internal packages.

## Choose the Smallest Sufficient Pattern

| Actual condition | Appropriate organization and layering |
|---|---|
| Simple reads/writes and limited validation | Separate API, business functions, and data-access responsibilities; allow a few files and concrete dependencies, omitting forwarding layers without behavior |
| Several business capabilities with independent rules and reasons to change | A modular monolith organized by business capability, with public operations between modules and internal layers as needed |
| Complex rules, state transitions, or multi-step transactions | Use cases own workflow and transactions; pure rule modules own calculations and invariants; extract actual complexity without requiring full DDD |
| External dependencies already have real multiple implementations and callers need common semantics | Define a port shaped by caller needs at that boundary, let adapters handle protocols, and bind implementations at the composition entry point; leave other modules as they are |

These conditions can coexist and patterns can be combined locally; they are not a mandatory project growth ladder. For a single external implementation, inject a concrete function/object first rather than creating ports for hypothetical suppliers or reuse. Splitting independent services additionally requires real deployment, fault-isolation, or team-ownership grounds; directory counts are not evidence.

Explain how the choice meets business constraints, its main costs, and why layers are added or omitted. Reuse comparisons already made during Superpowers design. Local transaction rollback does not undo external side effects: define execution timing, resulting states, and recovery ownership. See the [HTTP reference](http.md) for timeout and replay semantics.

## Distinguish Calls from Source Dependencies

A runtime arrow means a call; a source arrow means an import or dependency on a type definition. Describe both separately with arrows or a table for the proposal. One unlabeled call chain cannot stand in for both.

| Selected part | Runtime call example | Allowed source dependencies |
|---|---|---|
| Lightweight layering | API calls business functions, which call data-access functions | `api → business → data_access`; simple queries may use `api → data_access`; data access does not import routes or use cases |
| Separate pure rules | A use case obtains business data, calls rules, then saves results | `use_case → rules`; rules depend only on business values and necessary pure utilities, not HTTP, ORM, configuration loading, or application entry points |
| Local ports and adapters | A use case calls the currently bound adapter through a port | `use_case → port ← adapter`; the composition entry point imports use cases and adapters; use cases do not import concrete adapters; ports do not depend on supplier SDKs or database drivers |

Apply only the rules for the chosen pattern. Ports may use pure business types; adapters map external formats to the interface's required results and errors. The composition entry point creates and binds concrete resources; business operations accept prepared dependencies.

For frontend import directions and state ownership, follow the [frontend reference](frontend.md#responsibilities-and-dependencies). Coordinate workflows through relevant public feature capabilities or the composition layer; a backend port does not justify wrapping every frontend request in another layer.

Avoid circular imports in every pattern. Shared capabilities must not import business modules. Business modules use agreed public entry points instead of deep-importing each other's internals. List allowed and forbidden dependencies for the proposal and map them to existing lint, architecture tests, or dependency checks. If no tool exists, explain the actual inspection method; separate directories alone do not verify boundaries.

## Check Whether the Design Helps

- **Understandable interfaces:** Can callers understand operations and errors through public interfaces without reading internal SQL, protocols, or steps?
- **Localized change:** Choose a plausible business-rule or external-implementation change and identify affected modules and reasons. Reconsider ownership if several callers duplicate the same rule.
- **Layers carry behavior:** Consider merging a layer if removing it loses no constraint or encapsulation and makes calls clearer. A module is justified when it prevents important rules from scattering across callers. Do not judge module depth by line count.
- **Verifiable through interfaces:** Test normal results, invariants, transaction failures, and permission scope through public business operations. Where ports are justified, verify adapters share the contract and internals can change without caller knowledge.

Put business rationale, important module interfaces, choices and costs, both relationship types, and acceptance checks into the relevant sections of the existing design. During implementation, follow the main skill's documentation and verification rules; during review, report only supported findings. Explain why boundaries exist rather than merely presenting a directory tree.
